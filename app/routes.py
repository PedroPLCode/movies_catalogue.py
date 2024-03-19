from flask import render_template, url_for, request, redirect, flash
import random
import datetime
from app import tmdb_client
from app import app, db
from app.models import Favorite
from app.utils import *

app.secret_key = b'my-secret'
LIST_TYPES = ['top_rated', 'upcoming', 'popular', 'now_playing']
prev_path = ''

@app.errorhandler(404)
def handle_page_not_found(error):
    return redirect(url_for("homepage"))


@app.route('/')
def homepage():
    global prev_path
    prev_path = request.path
    
    selected_list = request.args.get('list_type', 'popular')
    if selected_list not in LIST_TYPES:
        selected_list = "popular"
        
    movies = tmdb_client.prepare_movies_list(how_many=8, list_type=selected_list)
    movies = check_if_movies_are_in_favorites(movies)
    
    return render_template("homepage.html",
                           movies=movies,
                           current_list=selected_list,
                           list_types=LIST_TYPES
                           )


@app.route('/search')
def search():
    global prev_path
    prev_path = request.full_path
    
    search_query = request.args.get("q", "")
    if search_query:
        movies = tmdb_client.get_movies_by_search_query(search_query)
    else: 
        movies = []
    movies = check_if_movies_are_in_favorites(movies)
    
    return render_template("search.html",
                           movies=movies,
                           search_query=search_query
                           )
    
    
@app.route('/today')
def today():
    global prev_path
    prev_path = request.full_path
    
    today = datetime.date.today()
    timezone = request.args.get("timezone", "")
    timezone = timezone if timezone else 'pl'
    movies = tmdb_client.get_movies_airing_today_by_timezone(timezone)
    movies = check_if_movies_are_in_favorites(movies)
        
    return render_template("today.html",
                           movies=movies,
                           timezone=timezone,
                           today=today
                           )
    

@app.route('/favorites')
def favorites():
    global prev_path
    prev_path = request.full_path
    
    favorites = Favorite.query.all()
    movies = []
    for favorite in favorites:
        movies.append(tmdb_client.get_single_movie_details(favorite.movie_id))
    return render_template("favorites.html",
                            movies=movies,
                            )
    
    
@app.route("/movie/<movie_id>")
def movie_details(movie_id):
    global prev_path
    prev_path = request.full_path
    
    details = tmdb_client.get_single_movie_details(movie_id)
    cast = tmdb_client.get_single_movie_cast(movie_id)
    movie_images = tmdb_client.get_single_movie_images(movie_id)
    random_image = random.choice(movie_images['backdrops'])

    favorites = Favorite.query.all()    
    movie = check_and_mark_if_single_movie_is_in_favorites(details, favorites)
    
    return render_template("movie_details.html",
                           movie=movie,
                           cast=cast,
                           image=random_image
                           )
    

@app.route("/favorites/add", methods=['POST'])
def add_to_favorites():
    global prev_path
        
    data = request.form
    movie_id = data.get('movie_id')
    movie_title = data.get('movie_title')
    if movie_id and movie_title:
        favorites = Favorite.query.all()
        for favorite in favorites:
            if favorite.movie_id == int(movie_id):
                flash(f'"{movie_title}" already in Favorites!')
                return redirect(url_for('homepage'))
        new_favorite = Favorite(movie_id=movie_id, movie_title=movie_title)
        db.session.add(new_favorite)
        db.session.commit()
        flash(f'"{movie_title}" saved in Favorites!')
        
        print(prev_path)
        
    return redirect(prev_path)


@app.route("/favorites/delete", methods=['POST'])
def delete_from_favorites():
    global prev_path
            
    data = request.form
    movie_id = data.get('movie_id')
    movie_title = data.get('movie_title')
    if movie_id and movie_title:
        favorites = Favorite.query.all()
        for favorite in favorites:
            if favorite.movie_id  == int(movie_id):
                db.session.delete(favorite)
                db.session.commit()
        flash(f'"{movie_title}" removed from Favorites!')
        favorites = Favorite.query.all()
        
        print(prev_path)
    return redirect(prev_path if favorites else 'homepage')


@app.context_processor
def utility_processor():
    def tmdb_image_url(path, size):
        return tmdb_client.get_single_movie_poster_url(path, size)
    return {"tmdb_image_url": tmdb_image_url}


@app.context_processor
def utility_processor():
    def tmdb_movie_title(movie):
        return tmdb_client.get_single_movie_title(movie)
    return {"tmdb_movie_title": tmdb_movie_title}


if __name__ == '__main__':
    app.run(debug=True)
from app.models import Favorite

def check_if_movies_are_in_favorites(movies):
    favorites = Favorite.query.all()
    for movie in movies:
        movie = check_and_mark_if_single_movie_is_in_favorites(movie, favorites)
    return movies


def check_and_mark_if_single_movie_is_in_favorites(movie, favorites):
    for favorite in favorites:
        if movie['id'] == favorite.movie_id:
            movie['is_favorite'] = True
    return movie
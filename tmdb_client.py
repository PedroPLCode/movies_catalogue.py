import requests
import random
from PERSONAL_API_KEY import PERSONAL_API_KEY

headers_settings = {
    "accept": "application/json",
    "Authorization": f'Bearer {PERSONAL_API_KEY}'
}
    
def get_popular_movies():
    endpoint = "https://api.themoviedb.org/3/movie/popular"
    response = requests.get(endpoint, headers=headers_settings)
    return response.json()


def get_movies(how_many):
    data = get_popular_movies()
    data_results = data["results"]
    random.shuffle(data_results)
    return data_results[:how_many]


def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"


def get_movie_title(movie):
    return str(movie['title'])


def get_single_movie(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"
    response = requests.get(endpoint, headers=headers_settings)
    return response.json()


def get_single_movie_cast(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    response = requests.get(endpoint, headers=headers_settings)
    return response.json()["cast"]


def get_single_movie_images(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/images"
    response = requests.get(endpoint, headers=headers_settings)
    return response.json()
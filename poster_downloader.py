import tmdbsimple as tmdb
import requests, os
tmdb.API_KEY = "83cbec0139273280b9a3f8ebc9e35ca9"

POSTER_FOLDER = r"movie_posters"
POSTER_ROOT_PATH = "https://image.tmdb.org/t/p/w300"

def main():
    if not os.path.exists(POSTER_FOLDER):
        os.makedirs(POSTER_FOLDER)

    movies = get_movies()

    
    for movie_data in movies:
        get_poster(movie_data)

def get_movies():
    movies = tmdb.Movies()
    popular_movies = movies.popular()["results"]
    return popular_movies

def get_poster(movie_data):
    poster_path = f'{POSTER_ROOT_PATH}{movie_data["poster_path"]}'
    image_name = poster_path.split("/")[-1]
    print(f"Downloading {image_name}")

    file_path = os.path.join(POSTER_FOLDER, image_name)
    
    img_data = requests.get(poster_path).content
    with open(file_path, "wb") as f:
        f.write(img_data)

main()
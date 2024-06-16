import tmdbsimple as tmdb
tmdb.API_KEY = "83cbec0139273280b9a3f8ebc9e35ca9"

poster_folder = r"movie_posters"
POSTER_ROOT_PATH = "https://image.tmdb.org/t/p/w300"

def main():
    movies = get_movies()

    
    for movie_data in movies:
        get_poster(movie_data)

def get_movies():
    movies = tmdb.Movies()
    popular_movies = movies.popular()["results"]
    return popular_movies

def get_poster(movie_data):
    poster_path = movie_data["poster_path"]
    pass

main()
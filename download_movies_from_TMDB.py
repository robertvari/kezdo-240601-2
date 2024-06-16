import tmdbsimple as tmdb
import json
tmdb.API_KEY = "83cbec0139273280b9a3f8ebc9e35ca9"


movies = tmdb.Movies()
popular_movies = movies.popular()["results"]

with open("movie_data.json", "w") as f:
    json.dump(popular_movies, f)
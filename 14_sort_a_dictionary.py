import json, pprint

with open("movie_data.json") as f:
    movie_list = json.load(f)

sorted_movies = sorted(movie_list, key=lambda movie_data: movie_data["popularity"], reverse=True)

for i in sorted_movies:
    print(i["title"], i["popularity"])
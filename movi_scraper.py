import requests
import json


url = "https://api.themoviedb.org/3/trending/movie/week?language=en-US"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI3MDI2M2UxMTIwNjExNzk1MTVhNGQ4MzRmYWIyYzVlMyIsInN1YiI6IjYyYzk4YjI5NDk4YmMyMDY5OGExNDliYiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.CE8PwJFliJqAYd2flBaJ6H8RPkdoWRiCgUDSWUiLth4"
}

response = requests.get(url, headers=headers)

results = response.text
results_formatted = json.loads(results)
print(type(results_formatted))

movies_list = results_formatted["results"]

for movie in movies_list:
    print(movie['title'])
    print(movie['vote_average'])
    print('')
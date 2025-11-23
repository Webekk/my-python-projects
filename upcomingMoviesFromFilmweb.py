import requests
from bs4 import BeautifulSoup
import random
import os

list_of_movies = []
used_movies = []
movies_url = requests.get('https://www.filmweb.pl/premiere/2026/4').text
soup = BeautifulSoup(movies_url, 'lxml')


if os.path.exists("movies.txt"):
    with open("movies.txt", "r") as f:
        for line in f:
            title = line.strip().split(". ", 1)[-1]   # usuwa numer "1. Film"
            used_movies.append(title)



upcoming_premieres = soup.find_all('a', class_ = 'preview__link') # Specify the html tag we are looking for with a specified class name
counter = 1
for upcoming_premiere in upcoming_premieres:
    print(f"{counter}. {upcoming_premiere.text}")
    movie_name = upcoming_premiere.text.strip()
    if movie_name not in list_of_movies:
        list_of_movies.append(upcoming_premiere.text.strip())
    # print(f"{upcoming_premiere.text} został dodany do listy")
    # print(list_of_movies)
    counter += 1

#Deleting the films we already watched!
list_of_movies = [m for m in list_of_movies if m not in used_movies]

def get_random_movie():
    if not list_of_movies:
        print("No movies available")
        return None
    random_movie = random.choice(list_of_movies)
    list_of_movies.remove(random_movie)
    used_movies.append(random_movie)
    return random_movie
random_movie = get_random_movie()
print("The movie you should go for a premiere is: "+ random_movie)

with open("movies.txt", "a") as file:
    file.write(f"{len(used_movies)}. {random_movie}\n")


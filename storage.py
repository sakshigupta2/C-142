import csv

allMovies = []

with open("final.csv",encoding="UTF8") as f:
    reader = csv.reader(f)
    data = list(reader)
    allMovies = data[1:]

liked_movies = []
not_liked_movies = []
did_not_watch = []

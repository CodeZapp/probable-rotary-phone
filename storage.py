import csv
allMovies = []
with open('final.csv') as f:
    reader = csv.reader(f)
    data = list(reader)
    allMovies = data[1:]
likedMovies = []
notLikedMovies = []
didNotWatch = []
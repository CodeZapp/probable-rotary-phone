import csv
with open('movies.csv') as f:
    reader = csv.reader(f)
    data = list(reader)
    allMovies = data[1:]
    headers = data[0]
headers.append('poster_link')
with open('final.csv', 'a+') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
with open('movieLinks.csv') as f:
    reader = csv.reader(f)
    data = list(reader)
    allMoviesLinks = data[1:]
for movieItem in allMovies:
    posterFound = any(movieItem[8] in movieLinkItems for movieLinkItems in allMoviesLinks)
    if posterFound:
        for movieLinkItem in allMoviesLinks:
            if movieItem[8] == movieLinkItem[0]:
                movieItem.append(movieLinkItem[1])
                if len(movieItem) == 28:
                    with open('final.csv', 'a+') as f:
                        csvwriter = csv.writer(f)
                        csvwriter.writerow(movieItem)
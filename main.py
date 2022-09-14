from flask import Flask, jsonify, request
from storage import allMovies, likedMovies, notLikedMovies, didNotWatch
from demographic_filtering import output
from content_filtering import get_recommendations
app = Flask(__name__)
@app.route('/get-movie')
def getMovie():
    movieData = {
        'title': allMovies[0][19],
        'poster_link': allMovies[0][27],
        'release_date': allMovies[0][13] or 'N/A',
        'duration': allMovies[0][15],
        'rating': allMovies[0][20],
        'overview': allMovies[0][9]
    }
    return jsonify({
        'data': movieData,
        'status': 'success'
    })
@app.route('/liked-movie', methods = ['POST'])
def likedMovie():
    movie = allMovies[0]
    likedMovies.append(movie)
    allMovies.pop(0)
    return jsonify({
        'status': 'success'
    }), 201
@app.route('/unliked-movie', methods = ['POST'])
def unliked_movie():
    movie = allMovies[0]
    notLikedMovies.append(movie)
    allMovies.pop(0)
    return jsonify({
        'status': 'success'
    }), 201
@app.route('/did-not-watch', methods = ['POST'])
def didNotWatchView():
    movie = allMovies[0]
    didNotWatch.append(movie)
    allMovies.pop(0)
    return jsonify({
        'status': 'success'
    }), 201

@app.route('/popular-movies')
def popularMovies():
    movieData = []
    for movie in output:
        d = {
            'title': movie[0],
            'poster_link': movie[1],
            'release_date': movie[2] or 'N/A',
            'duration': movie[3],
            'rating': movie[4],
            'overview': movie[5]
        }
        movieData.append(d)
    return jsonify({
        'data': movieData,
        'status': 'success'
    }), 200

@app.route('/recommended-movies')
def recommendedMovies():
    allRecommended = []
    for likedMovie in likedMovies:
        output = getRecommendations(likedMovie[19])
        for data in output:
            allRecommended.append(data)
    import itertools
    allRecommended.sort()
    allRecommended = list(allRecommended for allRecommended,_ in itertools.groupby(allRecommended))
    movieData = []
    for recommended in allRecommended:
        d = {
            'title': recommended[0],
            'poster_link': recommended[1],
            'release_date': recommended[2] or "N/A",
            'duration': recommended[3],
            'rating': recommended[4],
            'overview': recommended[5]
        }
        movieData.append(d)
    return jsonify({
        'data': movieData,
        'status': 'success'
    }), 200

if __name__ == '__main__':
  app.run()
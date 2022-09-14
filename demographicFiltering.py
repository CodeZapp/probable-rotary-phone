import pandas as pd
import numpy as np
df = pd.read_csv('final.csv')
c = df['vote_average'].mean()
m = df['vote_count'].quantile(0.9)
qMovies = df.copy().loc[df['vote_count'] >= m]
def weightedRating(x, m = m, c = c):
    v = x['vote_count']
    r = x['vote_average']
    return (v / (v + m) * r) + (m / (m + v) * c)
qMovies['score'] = qMovies.apply(weightedRating, axis = 1)
qMovies = qMovies.sort_values('score', ascending = False)
output = qMovies[['title', 'poster_link', 'release_date', 'runtime', 'vote_average', 'overview']].head(20).values.tolist()
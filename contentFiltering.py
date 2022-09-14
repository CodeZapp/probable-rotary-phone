from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import numpy as np
df = pd.read_csv('final.csv')
df = df[df['soup'].notna()]
count = CountVectorizer(stop_words = 'english')
countMatrix = count.fit_transform(df['soup'])
cosineSim = cosine_similarity(countMatrix, countMatrix)
df = df.reset_index()
indices = pd.Series(df.index, index = df['title'])
def getRecommendation(title):
    idx = indices[title]
    simScores = list(enumerate(cosineSim[idx]))
    simScores = sorted(simScores, key = lambda x: x[1], reverse = True)
    simScores = simScores[1:11]
    movieIndices = [i[0] for i in simScores]
    return df[['title', 'poster_link', 'release_date', 'runtime', 'vote_average', 'overview']].iloc[movieIndices].values.tolist()
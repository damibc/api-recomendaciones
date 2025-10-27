import pandas as pd

a_col = ['anime_id', 'name','members']
animes = pd.read_csv('data/anime.csv', sep=',', usecols=a_col)

ratings = pd.read_csv('data/ratings.csv', sep=',')
userRatings = ratings.pivot_table(index='user_id',columns='anime_id',values='rating')

corrMatrix = userRatings.corr(method='pearson', min_periods=10)
print(corrMatrix.head())
corrMatrix.to_csv("data/corr_matrix.csv", index=True)
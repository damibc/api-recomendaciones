import pandas as pd

a_col = ['anime_id', 'name', 'members']
animes = pd.read_csv('data/anime.csv', sep=',', usecols=a_col)
ratings = pd.read_csv('data/ratings.csv', sep=',')
corrMatrix = pd.read_csv('data/corr_matrix.csv', index_col=0)

def recomendar_animes(user_id, top_n=10):
    print("hola")
    user_ratings = ratings[ratings['user_id'] == user_id]

    print(user_ratings)
    
    if user_ratings.empty:
        print(f"No se encontraron ratings para el usuario {user_id}")
        return pd.DataFrame()

    myRatings = pd.Series(
        data=user_ratings['rating'].values,
        index=user_ratings['anime_id']
    )

    simCandidates = pd.Series(dtype=float)

    for anime, rating in myRatings.items():
        if anime not in corrMatrix.columns:
            continue
        sims = corrMatrix[anime].dropna()
        sims = sims.map(lambda x: x * rating)
        simCandidates = pd.concat([simCandidates, sims])

    simCandidates = simCandidates.groupby(simCandidates.index).sum()
    simCandidates = simCandidates.drop(myRatings.index, errors='ignore')
    simCandidates = simCandidates.sort_values(ascending=False)

    simdf = simCandidates.reset_index()
    simdf.columns = ['anime_id', 'score']
    recomendaciones = pd.merge(simdf, animes, on='anime_id', how='left')
    recomendaciones.sort_values('score', ascending=False, inplace=True)

    print(recomendaciones)

    return recomendaciones[['anime_id', 'name', 'score']].head(top_n)

recomendar_animes(7)
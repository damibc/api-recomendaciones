import pandas as pd

def entrenar(ratings_path='data/ratings.csv', anime_path='data/anime.csv', output_path='data/corr_matrix.csv'):
    try:
        a_col = ['anime_id', 'name', 'members']
        ratings = pd.read_csv(ratings_path, sep=',')

        userRatings = ratings.pivot_table(index='user_id', columns='anime_id', values='rating')

        corrMatrix = userRatings.corr(method='pearson', min_periods=10)

        corrMatrix.to_csv(output_path, index=True)
        print(f"Matriz de correlación generada correctamente y guardada en '{output_path}' ✅")
        print(corrMatrix.head())

        return corrMatrix

    except Exception as e:
        print(f"❌ Error al generar la matriz de correlación: {e}")
        return None
    
if __name__ == "__main__":
    entrenar()
from anime_recomendator import entrenar
from user_recomendator import recomendar_animes

class AnimeDAO:
    def __init__(self):
        self.version_file = "data/version.txt"

    def get_version(self) -> str:
        try:
            with open(self.version_file, "r") as f:
                version = f.read().strip()
            return version
        except FileNotFoundError:
            return "Versión no encontrada"

    def train(self) -> str:
        entrenar()
        return "Entrenamiento completado"

    def get_recommendations(self, user_id: int) -> list:
        recomendaciones = recomendar_animes(user_id)
        return recomendaciones
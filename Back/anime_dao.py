from .anime_recomendator import entrenar
from .user_recomendator import recomendar_animes
from pathlib import Path

class AnimeDAO:
    def __init__(self):
        self.version_file = Path("data/version.txt")

    def get_version(self):
        try:
            with self.version_file.open("r", encoding="utf-8") as f:
                contenido = f.read().strip()
                return int(contenido) if contenido.isdigit() else 0
        except FileNotFoundError:
            self.version_file.parent.mkdir(parents=True, exist_ok=True)
            self.version_file.write_text("0", encoding="utf-8")
            return 0

    def train(self):
        entrenar()


    def get_recommendations(self, user_id):
        recomendaciones = recomendar_animes(user_id)
        return recomendaciones
import csv
from pathlib import Path
import utils
import menuAnime
import menuRecomendador
from Animes import Anime
from Users import User

def salir():
    print("Que pase una buena tarde.")

    exit()

def iniciar_sesion():
    user_id = utils.validar_numero("Introduzca su ID de usuario:\n")

    # Directorio base
    script_dir = Path(__file__).resolve().parent
    data_dir = script_dir / "data"

    ruta_ratings = data_dir / "ratings.csv"
    ruta_anime = data_dir / "anime.csv"

    # --- Leer ratings.csv ---
    user_ratings = {}  # anime_id -> puntuación del usuario
    try:
        with ruta_ratings.open(newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    if int(row["user_id"]) == user_id:
                        anime_id = int(row["anime_id"])
                        puntuacion = float(row["rating"])
                        user_ratings[anime_id] = puntuacion
                except (KeyError, ValueError):
                    continue
    except FileNotFoundError:
        print(f"❌ No se encontró el archivo: {ruta_ratings}")
        salir()
    except Exception as e:
        print(f"⚠️ Error al leer {ruta_ratings}: {e}")
        salir()

    if not user_ratings:
        print("⚠️ Este usuario no tiene animes registrados.")
        return User(user_id, [])

    # --- Leer anime.csv y crear objetos Anime ---
    user_animes = []
    try:
        with ruta_anime.open(newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for i, row in enumerate(reader, start=1):
                # Validar que la fila tenga la info básica
                if not row or "anime_id" not in row or "name" not in row:
                    continue

                try:
                    anime_id = int(row["anime_id"])
                except ValueError:
                    continue

                if anime_id in user_ratings:
                    generos = row.get("genre", "")
                    generos_list = generos.split(", ") if generos else []

                    anime = Anime(
                        id=anime_id,
                        nombre=row.get("name", "").strip(),
                        puntuacion=user_ratings[anime_id],  # ✅ rating desde ratings.csv
                        generos=generos_list
                    )
                    user_animes.append(anime)
    except FileNotFoundError:
        print(f"❌ No se encontró el archivo: {ruta_anime}")
        salir()
    except Exception as e:
        print(f"⚠️ Error al leer {ruta_anime}: {e}")
        salir()

    usuario = User(id=user_id, animes=user_animes)
    return usuario


def menu(user):
    opciones = {
        1: lambda: menuAnime.menu(user),
        2: lambda: menuRecomendador.menu(),
        0: lambda: salir()
    }

    while True:
        opcion = utils.validar_numero(
            "Seleccione una Opcion:\n"\
            "   1.- Gestionar Animes.\n"\
            "   2.- Gestionar Recomendador.\n"\
            "   0.- Salir.\n",
            0,len(opciones)-1)
        accion = opciones.get(opcion)
        accion()

if __name__ == "__main__":
    user = iniciar_sesion()
    menu(user)
import csv
from pathlib import Path
from Animes import Anime
import utils

DATA_DIR = Path(__file__).resolve().parent / "data"
ANIME_FILE = DATA_DIR / "anime.csv"

def menu(user):
    
    opciones = {
        1: lambda: recomendar_animes(user),
        2: lambda: valorar_anime(user),
        3: lambda: mostrar_animes(user),
        4: lambda: todos_animes()
    }
    while True:
        opcion = utils.validar_numero(
            "Seleccione una Opcion:\n"\
            "   1.- Recomendar Anime.\n"\
            "   2.- Valorar Anime.\n"\
            "   3.- Mostrar Animes Vistos.\n"\
            "   4.- Mostrar Animes Disponibles.\n"\
            "   0.- Volver.\n",
            0,4)
        if opcion == 0: return 
        accion = opciones.get(opcion)
        accion()

def recomendar_animes():
    print("Funcion en Costrucción")


def valorar_anime(user):
    RATINGS_FILE = DATA_DIR / "ratings.csv"

    anime_id = utils.validar_numero("Introduzca el ID del anime que desea valorar:\n")

    anime_info = None
    try:
        with ANIME_FILE.open(newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if int(row["anime_id"]) == anime_id:
                    generos = row["genre"].split(", ") if row["genre"] else []
                    anime_info = Anime(
                        id=anime_id,
                        nombre=row["name"],
                        generos=generos
                    )
                    break
    except FileNotFoundError:
        print(f"No se encontró el archivo {ANIME_FILE}")
        return

    if not anime_info:
        print("El ID del anime no existe.")
        return

    nueva_puntuacion = utils.validar_numero("Introduzca su puntuación (0 a 10):\n", 0, 10)

    animes_usuario = user.get_animes()
    anime_existente = next((a for a in animes_usuario if a.get_id() == anime_id), None)

    if anime_existente:
        # Si ya existe → actualizar
        anime_existente.set_puntuacion(nueva_puntuacion)
        print(f"✅ Puntuación actualizada para {anime_existente.get_nombre()}.")
    else:
        # Si no existe → añadir
        anime_info.set_puntuacion(nueva_puntuacion)
        animes_usuario.append(anime_info)
        print(f"{anime_info.get_nombre()} añadido a tus animes valorados.")

    try:
        # Leer todas las filas
        with RATINGS_FILE.open("r", newline="", encoding="utf-8") as f:
            reader = list(csv.DictReader(f))

        actualizado = False
        for row in reader:
            if int(row["user_id"]) == user.get_id() and int(row["anime_id"]) == anime_id:
                row["rating"] = str(nueva_puntuacion)
                actualizado = True
                break

        # Si no existía, añadirlo
        if not actualizado:
            reader.append({
                "user_id": str(user.get_id()),
                "anime_id": str(anime_id),
                "rating": str(nueva_puntuacion)
            })

        # Sobrescribir el CSV
        with RATINGS_FILE.open("w", newline="", encoding="utf-8") as f:
            fieldnames = ["user_id", "anime_id", "rating"]
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(reader)

    except FileNotFoundError:
        print(f"⚠️ No se encontró {RATINGS_FILE}, creando nuevo archivo...")
        with RATINGS_FILE.open("w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["user_id", "anime_id", "rating"])
            writer.writeheader()
            writer.writerow({
                "user_id": str(user.get_id()),
                "anime_id": str(anime_id),
                "rating": str(nueva_puntuacion)
            })
    except Exception as e:
        print(f" Error al actualizar ratings.csv: {e}")
        return


def mostrar_animes(user):
    animes = user.get_animes()
    for anime in animes:
        print(anime)

def todos_animes():
    # --- Leer todos los animes y agrupar por letra ---
    animes_por_letra = {}
    try:
        with ANIME_FILE.open(newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                nombre = row.get("name", "").strip()
                if not nombre:
                    continue
                letra = nombre[0].upper()
                anime = Anime(
                    id=int(row.get("anime_id", 0)),
                    nombre=nombre,
                    generos=row.get("genre", "").split(", ") if row.get("genre") else []
                )
                if letra not in animes_por_letra:
                    animes_por_letra[letra] = []
                animes_por_letra[letra].append(anime)
    except FileNotFoundError:
        print(f"❌ No se encontró el archivo: {ANIME_FILE}")
        return

    letras_disponibles = sorted(animes_por_letra.keys())
    
    # --- Crear un menú dinámico ---
    while True:
        print("\nOrden alfabético disponible:")
        for idx, letra in enumerate(letras_disponibles, 1):
            print(f"   {idx}.- {letra}")
        print("   0.- Volver")

        opcion = utils.validar_numero("Seleccione una letra:\n", 0, len(letras_disponibles))
        if opcion == 0:
            return

        letra_seleccionada = letras_disponibles[opcion - 1]
        mostrar_animes_por_letra(animes_por_letra, letra_seleccionada)


def mostrar_animes_por_letra(animes_por_letra, letra):
    if letra not in animes_por_letra or not animes_por_letra[letra]:
        print(f"No hay animes que comiencen con '{letra}'.")
        return
    print(f"\nAnimes que comienzan con '{letra}':\n")
    for anime in sorted(animes_por_letra[letra], key=lambda x: x.get_nombre()):
        print(anime)
    print("\n--- Fin de la lista ---\n")

from pathlib import Path
import utils
from Animes import Anime
from Users import User


def menu():
    opciones = {
        1: lambda: entrenar_recomendador(),
        2: lambda: mostrar_version()
    }

    while True:
        opcion = utils.validar_numero(
            "Seleccione una Opcion:\n"
            "   1.- Entrenar Recomendador.\n"
            "   2.- Mostrar Versión Recomendador.\n"
            "   0.- Volver.\n",
            0, len(opciones)
        )

        if opcion == 0:
            return

        accion = opciones.get(opcion)
        accion()


# --- Ruta al archivo version.txt ---
def obtener_ruta_version():
    script_dir = Path(__file__).resolve().parent
    data_dir = script_dir / "data"
    version_file = data_dir / "version.txt"
    return version_file


def leer_version():
    version_file = obtener_ruta_version()
    try:
        with version_file.open("r", encoding="utf-8") as f:
            contenido = f.read().strip()
            return int(contenido) if contenido.isdigit() else 0
    except FileNotFoundError:
        # Si no existe el archivo, crearlo con versión 0
        version_file.write_text("0", encoding="utf-8")
        return 0


def guardar_version(nueva_version):
    version_file = obtener_ruta_version()
    with version_file.open("w", encoding="utf-8") as f:
        f.write(str(nueva_version))


def entrenar_recomendador():
    print("\nEntrenando el recomendador... (simulación)")
    version_actual = leer_version()
    nueva_version = version_actual + 1
    guardar_version(nueva_version)
    print(f"Entrenamiento completado. Nueva versión: {nueva_version}\n")


def mostrar_version():
    version_actual = leer_version()
    print(f"\n Versión actual del recomendador: {version_actual}\n")

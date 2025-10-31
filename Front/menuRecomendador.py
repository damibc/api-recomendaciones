from pathlib import Path
from . import utils
from Back.anime_api import train, version


# === MENÚ PRINCIPAL DEL RECOMENDADOR ===
def menu():
    opciones = {
        1: lambda: entrenar_recomendador(),
        2: lambda: mostrar_version(),
    }

    while True:
        opcion = utils.validar_numero(
            "\nSeleccione una opción:\n"
            "   1.- Entrenar Recomendador.\n"
            "   2.- Mostrar Versión Recomendador.\n"
            "   0.- Volver.\n",
            0,
            len(opciones)
        )

        if opcion == 0:
            return

        accion = opciones.get(opcion)
        accion()


# === GESTIÓN DE VERSIONES ===

#Obtiene la ruta al archivo version.txt.
def obtener_ruta_version():
    script_dir = Path(__file__).resolve().parent.parent
    data_dir = script_dir / "data"
    return data_dir / "version.txt"


#Lee la versión actual del recomendador desde version.txt.
def leer_version():
    version_file = obtener_ruta_version()
    try:
        with version_file.open("r", encoding="utf-8") as f:
            contenido = f.read().strip()
            return int(contenido) if contenido.isdigit() else 0
    except FileNotFoundError:
        version_file.write_text("0", encoding="utf-8")
        return 0


#Guarda una nueva versión en version.txt.
def guardar_version(nueva_version):
    version_file = obtener_ruta_version()
    with version_file.open("w", encoding="utf-8") as f:
        f.write(str(nueva_version))


# === FUNCIONALIDADES ===

#Ejecuta el entrenamiento del recomendador y actualiza la versión.
def entrenar_recomendador():
    print("\nEntrenando el recomendador...\n")
    train()

    version_actual = leer_version()
    nueva_version = version_actual + 1
    guardar_version(nueva_version)

    print(f"Entrenamiento completado. Nueva versión: {nueva_version}\n")


#Muestra la versión actual del recomendador.
def mostrar_version():
    vers = version()
    numero_version = vers.get("version", 0)
    print(f"\nVersión actual del recomendador: {numero_version}\n")

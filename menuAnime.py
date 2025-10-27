import utils
from Animes import Anime
from Users import User

def menu(user):
    
    opciones = {
        1: lambda: recomendar_animes(user),
        2: lambda: valorar_anime(user),
        3: lambda: mostrar_animes(user),
    }
    while True:
        opcion = utils.validar_numero(
            "Seleccione una Opcion:\n"\
            "   1.- Recomendar Anime.\n"\
            "   2.- Valorar Anime.\n"\
            "   3.- Mostrar Animes Vistos.\n"\
            "   0.- Volver.\n",
            0,3)
        if opcion == 0: return 
        accion = opciones.get(opcion)
        accion()

def recomendar_animes():
    print("Funcion en Costrucción")


def valorar_anime():
    print("Funcion en Costrucción")


def mostrar_animes(user):
    animes = user.get_animes()
    for anime in animes:
        print(anime)

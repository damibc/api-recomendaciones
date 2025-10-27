import utils
import menuAnime

def salir():
    print("Que pase una buena tarde.")

    exit()

def menu():
    opciones = {
        1: lambda: menuAnime.menu(),
        0: lambda: salir()
    }

    while True:
        opcion = utils.validar_numero(
            "Seleccione una Opcion:\n"\
            "   1.- Gestionar Animes.\n"\
            "   0.- Salir.\n",
            0,len(opciones)-1)
        accion = opciones.get(opcion)
        accion()

if __name__ == "__main__":
    menu()
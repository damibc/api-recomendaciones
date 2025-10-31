import mysql.connector 

def validar_numero(mensaje, minimo=None, maximo=None):
    while True:
        try:
            valor = int(input(mensaje))

            if minimo is not None and valor < minimo:
                print(f"El valor debe ser mayor o igual que {minimo}.")
                continue

            if maximo is not None and valor > maximo:
                print(f"El valor debe ser menor o igual que {maximo}.")
                continue

            return valor

        except ValueError:
            print("Error: introduzca un número válido.")
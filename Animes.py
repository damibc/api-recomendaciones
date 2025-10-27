class Anime():
    def __init__(self, id = 0, nombre = "",puntuacion = -1, generos = []):
        self.__id = id
        self.__nombre = nombre
        self.__puntuacion = puntuacion
        self.__generos = generos

#Nombre
    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, nombre):
        self.__nombre = nombre

#ID
    def get_id(self):
        return self.__id
    
    def set_id(self, id):
        self.__id = id

#Genero
    def get_generos(self):
        return self.__generos
    
    def set_generos(self, generos):
        self.__generos = generos

#KEYS
    def get_keys(self):
        return self.__id, self.__nombre, self.__generos


#STR
    def __str__(self):
        return f"Nombre: {self.__nombre} || Puntuacion: {self.__puntuacion} || Generos: {self.__generos}\n"
    
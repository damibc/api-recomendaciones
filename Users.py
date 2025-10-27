class User():
    def __init__(self, id, animes):
        self.__id = id
        self.__animes = animes

    def get_animes(self):
        return self.__animes
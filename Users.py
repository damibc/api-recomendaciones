class User():
    def __init__(self, id, animes):
        self.__id = id
        self.__animes = animes

#ID
    def get_id(self):
        return self.__id
    
    def set_id(self, id):
        self.__id = id

    def get_animes(self):
        return self.__animes
class Marca:
    def __init__(self, nombre):
        self.__nombre = nombre

    def getNombre(self):
        return self.__nombre
    
    def setNombre(self, nom):
        self.__nombre = nom
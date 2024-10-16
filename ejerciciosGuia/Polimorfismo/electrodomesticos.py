from abc import ABC, abstractmethod

class Interface(ABC):

    @abstractmethod
    def get_consumo(self):
        pass

    @abstractmethod
    def get_coste_consumo(self):
        pass


class Electrodomestico(Interface):

    def __init__(self, tipo, marca, potencia):
        self.__tipo = tipo
        self.__marca = marca
        self.__potencia = potencia

#getters
    def get_tipo(self):
        return self.__tipo
    
    def get_marca(self):
        return self.__marca
    
    def get_potencia(self):
        return self.__potencia
    

#setters
    def set_tipo(self, tipo):
        self.__tipo = tipo

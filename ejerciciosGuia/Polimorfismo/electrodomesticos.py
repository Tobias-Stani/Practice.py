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

    # Getters
    def get_tipo(self):
        return self.__tipo

    def get_marca(self):
        return self.__marca

    def get_potencia(self):
        return self.__potencia

    # Setters
    def set_tipo(self, tipo):
        self.__tipo = tipo

    def get_consumo(self):
        return self.__potencia * 0.1 

    def get_coste_consumo(self):
        coste_kwh = 0.15 
        return self.get_consumo() * coste_kwh


class Lavadora(Electrodomestico):
    def __init__(self, marca, potencia):
        super().__init__("Lavadora", marca, potencia) 
        self.__precio = 0 
        self.__aguaCaliente = False  


    def __init__(self, marca, precio, potencia, aguaCaliente):
        super().__init__("Lavadora", marca, potencia) 
        self.__precio = precio  
        self.__aguaCaliente = aguaCaliente 

    def get_precio(self):
        return self.__precio

    def get_aguaCaliente(self):
        return self.__aguaCaliente


    def set_precio(self, precio):
        self.__precio = precio

    def set_aguaCaliente(self, aguaCaliente):
        self.__aguaCaliente = aguaCaliente

    # Metodo interfaz
    def get_consumo(self):
        consumo_base = super().get_consumo()  
        if self.__aguaCaliente:
            return consumo_base * 1.2  
        return consumo_base

    # Metodo interfaz
    def get_coste_consumo(self):
        return super().get_coste_consumo()

    # Método para mostrar la información de la lavadora
    def __str__(self):
        modo = "caliente" if self.__aguaCaliente else "fría"
        return f"Lavadora de marca {self.get_marca()} con potencia {self.get_potencia()}W, precio ${self.__precio}, funcionando con agua {modo}."


lavadora1 = Lavadora("Samsung", 400, 500, False) 
lavadora2 = Lavadora("LG", 800, 600, True)  

print(lavadora1)
print(f"Consumo: {lavadora1.get_consumo()} kWh")
print(f"Coste consumo: ${lavadora1.get_coste_consumo():.2f}")

print(lavadora2)
print(f"Consumo: {lavadora2.get_consumo()} kWh")
print(f"Coste consumo: ${lavadora2.get_coste_consumo():.2f}")
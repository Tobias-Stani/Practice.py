class Fabrica: 
    def __init__(self, llantas, color, precio):
        self.__llantas = llantas
        self.__color = color
        self.__precio = precio

    def get_llantas(self):
        return self.__llantas
    
    def get__color(self):
        return self.__color
    
    def get_precio(self):
        return self.__precio
    

class Auto(Fabrica):
    def __init__(self, llantas, color, precio, puertas):
        super().__init__(llantas, color, precio)
        self.__puertas = puertas


class Moto(Fabrica):
    def __init__(self, llantas, color, precio, tipo):
        super().__init__(llantas, color, precio)
        self.__tipo = tipo

    def get_tipo(self):
        return self.__tipo
    

auto = Auto(4, "gris", 5000, 5)

print(f"el auto tiene {auto.get_llantas()} llantas, es de color {auto.get__color()} y cuesta {auto.get_precio()} dolares")

moto = Moto(2, "negra", 3000, "deportiva")

print(f"la moto es de tipo {moto.get_tipo()}, tiene {moto.get_llantas()} llantas, es de color {moto.get__color()} y cuesta {moto.get_precio()} dolares")
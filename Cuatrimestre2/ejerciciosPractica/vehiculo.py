class Vehiculo():
    def __init__(self,chofer,acompanante, cantidad_kilometros):
        self.__chofer = chofer    
        self.__acompanante = acompanante
        self.__cantidad_kilometros = cantidad_kilometros

    def get_chofer(self):
        return self.__chofer
    
    def get_acompanante(self):
        return self.__acompanante
    
    def get_cantidad_kilometros(self):
        return self.__cantidad_kilometros
    

class Moto(Vehiculo):
    def __init__(self, chofer, acompanante, cantidad_kilometros):
        super().__init__(chofer, acompanante, cantidad_kilometros)

    def set_kilometros(self, cantidad_kilometros):
        self.__cantidad_kilometros = cantidad_kilometros

    def set_acompanante(self, acompanante):
        if acompanante <= 1:
            self.__acompanante = acompanante
        else:
            print("la moto solo puede llevar un acompañante")

    def set_chofer(self, chofer):
        if self.get_acompanante() <= 1:
            self.__chofer = chofer
        else:
            print("solo se puede cambiar de chofer cuando no hay acompañantes")



class Colectivo(Vehiculo):
    def __init__(self, chofer, acompanante, cantidad_kilometros):
        super().__init__(chofer, acompanante, cantidad_kilometros)

    def set_kilometros(self, cantidad_kilometros):
        self.__cantidad_kilometros = cantidad_kilometros

    def set_acompanante(self, acompanante):
        if acompanante <= 40:
            self.__acompanante = acompanante
        else:
            print("el colectivo solo puede llevar 40 acompañantes")

    def set_chofer(self, chofer):
        if self.get_acompanante() >= 1:
            self.__chofer = chofer
        else:
            print("solo se puede cambiar de chofer cuando no hay acompañantes")



moto = Moto("carlitossss", 1, 40000)


print(f"el chofer es {moto.get_chofer()}, la cantidad de acompañantes es {moto.get_acompanante()} y la cantidad de kilometros es {moto.get_cantidad_kilometros()}")


cole1 = Colectivo("juan", 30, 1000000)

print(f"el chofer es {cole1.get_chofer()}, la cantidad de acompañantes es {cole1.get_acompanante()} y la cantidad de kilometros es {cole1.get_cantidad_kilometros()}")
cole1.set_acompanante(50)
class Vehiculo:
    def __init__(self, chofer, kilometros=0):
        self._chofer = chofer    
        self._kilometros = kilometros

    def get_chofer(self):
        return self._chofer
    
    def get_kilometros(self):
        return self._kilometros
    
    def set_kilometros(self, km):
        self._kilometros = km
    
    # este método se sobreescribe en las subclases
    def set_chofer(self, chofer):
        self._chofer = chofer


class Moto(Vehiculo):
    def __init__(self, chofer, kilometros=0):
        super().__init__(chofer, kilometros)
        self._acompanante = 0  # 0 o 1

    def get_acompanante(self):
        return self._acompanante

    def set_acompanante(self, cantidad):
        if cantidad in (0, 1):
            self._acompanante = cantidad
        else:
            print("La moto solo puede tener 0 o 1 acompañante")

    def set_chofer(self, chofer):
        if self._acompanante == 0:
            self._chofer = chofer
        else:
            print("No se puede cambiar de chofer si hay acompañante")


class Colectivo(Vehiculo):
    def __init__(self, chofer, kilometros=0):
        super().__init__(chofer, kilometros)
        self._pasajeros = 0  # puede variar entre 0 y 40

    def get_pasajeros(self):
        return self._pasajeros

    def set_pasajeros(self, cantidad):
        if 0 <= cantidad <= 40:
            self._pasajeros = cantidad
        else:
            print("El colectivo solo puede llevar hasta 40 pasajeros")

    def set_chofer(self, chofer):
        if self._pasajeros == 0:
            self._chofer = chofer
        else:
            print("No se puede cambiar de chofer si hay pasajeros")

moto = Moto("Carlos", 40000)
moto.set_acompanante(1)
print(f"Moto - Chofer: {moto.get_chofer()}, Acompañante: {moto.get_acompanante()}, Km: {moto.get_kilometros()}")
moto.set_chofer("Juan")  # ❌ No deja porque tiene acompañante

cole = Colectivo("Pedro", 1000000)
cole.set_pasajeros(30)
print(f"Colectivo - Chofer: {cole.get_chofer()}, Pasajeros: {cole.get_pasajeros()}, Km: {cole.get_kilometros()}")
cole.set_chofer("Luis")  # ❌ No deja porque tiene pasajeros

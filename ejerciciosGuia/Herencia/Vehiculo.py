"""
Ejercicio:
Existen dos tipos de vehículos: las motos, que llevan un chofer y un acompañante, y los colectivos, 
que llevan un chofer y varios pasajeros. Los vehículos deben conocer la cantidad de kilómetros recorridos, 
asignar y cambiar chofer. Cada vehículo particular deberá poder agregar un acompañante o diversos pasajeros, 
respectivamente. En caso del colectivo, no puede cambiar de chofer si hubiera pasajeros. En el caso de la moto,
no puede hacerlo si hubiera un acompañante
"""

class Vehiculo:
    def __init__(self, chofer, kilometrosRecorridos = 0):
        self.chofer = chofer
        self.kilometrosRecorridos = kilometrosRecorridos

    def asignarChofer(self, nuevoChofer):
        self.chofer = nuevoChofer
        print(f"se ha asignado un nuevo chofer: {self.chofer}")

    def cambiarChofer(self, nuevoChofer):
        pass

    def agregarKilometros(self, kilometros):
        self.kilometrosRecorridos += kilometros
        print(f"Kilómetros recorridos: {self.kilometrosRecorridos} km")

        

class Moto(Vehiculo):
    def __init__(self, chofer, kilometrosRecorridos=0, acompanante=None):
        super().__init__(chofer, kilometrosRecorridos)
        self.acompanante = acompanante

    def agregarAcompanante(self, acompanante):
        if self.acompanante:
            print(f"Ya hay un acompañante: {self.acompanante}")
        else:
            self.acompanante = acompanante
            print(f"Se ha agregado el acompañante: {self.acompanante}")

    def quitaAcompanante(self):
        if self.acompanante:
            print(f"Se ha quitado el acompañante: {self.acompanante}")
            self.acompanante = None
        else:
            print("No hay ningún acompañante para quitar.")

    def cambiarChofer(self, nuevoChofer):
        if self.acompanante:
            print("No se puede cambiar el chofer mientras haya un acompañante.")
        else:
            super().asignarChofer(nuevoChofer)


class Colectivo(Vehiculo):
    def __init__(self, chofer, kilometrosRecorridos=0):
        super().__init__(chofer, kilometrosRecorridos)
        self.pasajeros = []

    def agregar_pasajero(self, pasajero):
        self.pasajeros.append(pasajero)
        print(f"Se ha agregado un pasajero: {pasajero}. Total pasajeros: {len(self.pasajeros)}")

    def quitar_pasajero(self, pasajero):
        if pasajero in self.pasajeros:
            self.pasajeros.remove(pasajero)
            print(f"Se ha quitado el pasajero: {pasajero}. Total pasajeros: {len(self.pasajeros)}")
        else:
            print(f"El pasajero {pasajero} no está en el colectivo.")

    def cambiar_chofer(self, nuevoChofer):
        if len(self.pasajeros) > 0:
            print("No se puede cambiar el chofer mientras haya pasajeros.")
        else:
            super().asignarChofer(nuevoChofer)
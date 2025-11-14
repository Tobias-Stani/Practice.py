from abc import ABC, abstractmethod

class Vehiculo(ABC):
    def __init__(self, marca, modelo):
        self._marca = marca
        self._modelo = modelo

    @abstractmethod
    def info(self):
        return print(f"marca: {self._marca}. y su modelos es: {self._modelo}")

    

class Auto(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)
        self._puertas = puertas

    def info(self):
        super().info()
        return print(f"tiene {self._puertas} puertas")
    

class Moto(Vehiculo):
    def __init__(self, marca, modelo, cilindrada):
        super().__init__(marca, modelo)
        self._cilindrada = cilindrada

    def info(self):
        super().info()
        return print(f"tiene {self._cilindrada} cc")    
    

veiculos = []

auto = Auto("clio", "renault", 5)
moto = Moto("gilera", "smash", 110)

veiculos.append(auto)
veiculos.append(moto)

for v in veiculos:
    v.info()


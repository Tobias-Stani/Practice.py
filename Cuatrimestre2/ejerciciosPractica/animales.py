class Animal:
    def __init__(self, nombre, edad):
        self._nombre = nombre 
        self._edad = edad

    def presentarse(self):
        print(f"soy animal {self._nombre} y tengo {self._edad} anios")


class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)
        self._raza = raza

    def presentarse(self):
        print(f"soy perro de raza {self._raza}, me llamo {self._nombre} y tengo {self._edad} anios")


animales = []

perrito = Perro("Pedro", 10, "calle")
perro = Perro("Firulais", 5, "pastor aleman")

animales.append(perrito)
animales.append(perro)

for a in animales:
    a.presentarse()
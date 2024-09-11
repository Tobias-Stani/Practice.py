class Persona:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado


class Estudiante(Persona):
    def __init__(self,nombre, edad, grado, universidad, carrera):
        super().__init__(nombre, edad, grado)
        self.universidad = universidad
        self.carrera = carrera

estudiante1 = Estudiante('tobias', 20, '5to', 'uno', 'lic informatica')

print(estudiante1.carrera)
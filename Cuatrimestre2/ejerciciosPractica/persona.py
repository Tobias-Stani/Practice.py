class Persona:
    def __init__(self, nombre, apellido):
        self.__nombre = nombre 
        self.__apellido = apellido

    def get_nombre(self):   
        return self.__nombre

    def get_apellido(self):
        return self.__apellido
    
    def get_nombre_completo(self):
        return f"{self.__nombre} {self.__apellido}"

class Estudiante(Persona):
    def __init__(self,nombre, apellido, edad, carrera):
        super().__init__(nombre, apellido)
        self.__edad = edad
        self.__carrera = carrera

    def get_carrera(self):
        return self.__carrera
    

estudiante = Estudiante("Tobias", "stani", 21, "lic informatica")

print(f"estudiante: {estudiante.get_nombre_completo()}, cursa la carrera: {estudiante.get_carrera()}")
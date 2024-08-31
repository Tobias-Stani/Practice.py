class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado

    def estudiar(self):
        print(f'el estudiante: {self.nombre} esta estudiando')


nombre = input("ingrese el nombre del alumno: ")
edad = input("ingrese la edad del alumno: ")
grado = input("ingrese el grado del alumno: ")

estudiante1 = Estudiante(nombre, edad, grado)

print(f"""

    Datos del estudiante: \n\n
    nombre:  {estudiante1.nombre}\n
    edad: {estudiante1.edad}\n
    grado: {estudiante1.grado}\n

""")


while True: 
    estudiar = input()
    if(estudiar.lower() == "estudiar"):
        estudiante1.estudiar()
         
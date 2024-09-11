class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

class Artista:
    def __init__(self, habilidad):
        self.habilidad = habilidad
    
    def mostrarHabilidad(self):
        print(f"Mi habilidad es: {self.habilidad}")

# Herencia múltiple
class EmpleadoArtista(Persona, Artista):
    def __init__(self, nombre, edad, nacionalidad, habilidad, salario, empresa):
        # Llamamos directamente a los constructores de las clases base
        Persona.__init__(self, nombre, edad, nacionalidad)  # Heredo atributos de Persona
        Artista.__init__(self, habilidad)  # Heredo atributos de Artista
        self.salario = salario
        self.empresa = empresa

    def presentarse(self):
        # Puedes llamar directamente al método mostrarHabilidad de Artista
        self.mostrarHabilidad()
        print(f"Hola, soy {self.nombre}, trabajo en {self.empresa} y mi salario es {self.salario}.")

# Crear una instancia de EmpleadoArtista
kike = EmpleadoArtista('kike', 43, 'paraguayo', 'hacer asado', 430000, 'changuero')

# Llamar a los métodos
kike.presentarse()

herencia = issubclass(EmpleadoArtista, Artista)
isinstance = isinstance(kike, Persona)

print(herencia)
print(isinstance)
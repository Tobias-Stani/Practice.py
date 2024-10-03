from abc import ABC, abstractmethod
import math

# Clase abstracta que actúa como interfaz
class Figura(ABC):

    @abstractmethod
    def calcular_area(self):
        pass

# Clase Cuadrado que hereda de Figura
class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado ** 2

# Clase Rectangulo que hereda de Figura
class Rectangulo(Figura):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def calcular_area(self):
        return self.ancho * self.alto

# Clase Circulo que hereda de Figura
class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * (self.radio ** 2)



class TestInterface:
    @staticmethod
    def main():
        # Declarar un arreglo de figuras
        figuras = [
            Cuadrado(4),    # Cuadrado con lado 4
            Circulo(3),     # Círculo con radio 3
            Rectangulo(5, 2), # Rectángulo con ancho 5 y alto 2
            Cuadrado(6),    # Cuadrado con lado 6
            Circulo(2)      # Círculo con radio 2
        ]

        # Calcular el área total
        area_total = sum(figura.calcular_area() for figura in figuras)

        # Mostrar el resultado
        print(f"De un total de {len(figuras)} figuras, el área total es de {area_total:.2f} unidades cuadradas.")

# Ejecutar el método main
TestInterface.main()

import math

class Punto:
    
    def __init__(self, x, y):
        self._x = x
        self._y = y
    
    def estaSobreEjeX(self):
        return self._y == 0
    
    def estaSobreEjeY(self):
        return self._x == 0
    
    def esElOrigenDeCoordenadas(self):
        return self._x == 0 and self._y == 0
    
    def distanciaAlOrigen(self):
        return math.sqrt(self._x**2 + self._y**2)
    
    @staticmethod
    def distancia(p1, p2):
        return math.sqrt((p2._x - p1._x)**2 + (p2._y - p1._y)**2)
    
    def distancia(self, p):
        return math.sqrt((p._x - self._x)**2 + (p._y - self._y)**2)



class Circulo:

    def __init_(self, radio):
        self._radio = radio
    
    #getter y setter para el diametro.
    @property
    def radio(self):
        return self._radio
    
    @radio.setter
    def radio(self, valor):
        if valor > 0:
            self._radio = valor
        else:
            raise ValueError("el radio debe ser mayor que 0")
        
    
    #getter para el perimetro
    @property
    def perimetro(self):
        return 2 * math.pi * self._radio
    
    #getter para el area.
    @property
    def area(self):
        return math.pi * (self._radio ** 2)



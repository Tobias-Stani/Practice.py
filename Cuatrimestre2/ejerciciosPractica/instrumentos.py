from abc import ABC, abstractmethod

class Identificable(ABC):

    @abstractmethod
    def queInstrumentoEres(self):
        pass


class Instrumento(ABC):

    numero_de_instrumentos = 0

    def __init__(self, nombre, precio):
        self._nombre = nombre
        self._precio = precio

    @abstractmethod
    def afinar(self):
        pass

class Viento(Instrumento, Identificable):

    numInstrVientoMetal = 0      # Variable estática
    numInstrVientoMadera = 0     # Variable estática

    def __init__(self, nombre, precio, es_metal):
        super().__init__(nombre, precio)
        self._es_metal = es_metal

        if self._es_metal:
            Viento.numInstrVientoMetal += 1
        else:
            Viento.numInstrVientoMadera += 1

    def afinar(self):
        return print(f"Se afino instrumento de viento {self._nombre}")
    
    def es_metal(self):
        return self._es_metal
    
    def queInstrumentoEres(self):
        print(f"{self._nombre}, del tipo Viento")
    

class Percusion(Instrumento, Identificable):
    numInstrPercusion = 0  # Variable estática

    def __init__(self, nombre, precio):
        super().__init__(nombre, precio)
        Percusion.numInstrPercusion += 1  # Cada vez que se crea uno, suma 1

    def afinar(self):
        print(f"Se afinó instrumento de Percusion: {self._nombre}")
    
    def queInstrumentoEres(self):
        print(f"{self._nombre}, del tipo Percusion")

class Cuerda(Instrumento, Identificable):
    numInstrCuerda = 0  # Variable estática

    def __init__(self, nombre, precio):
        super().__init__(nombre, precio)
        Cuerda.numInstrCuerda += 1  # Cada vez que se crea uno, suma 1

    def afinar(self):
        print(f"Se afinó instrumento de cuerda: {self._nombre}")
    
    def queInstrumentoEres(self):
        print(f"{self._nombre}, del tipo Cuerda")


saxo = Viento("Saxofón", 1200, True)
bombo = Percusion("Bombo", 2000)
violin = Cuerda("Violin", 1500)

print(saxo.queInstrumentoEres())    # Saxofón, del tipo Viento
print(bombo.queInstrumentoEres())   # Bombo, del tipo Percusion
print(violin.queInstrumentoEres())  # Violin, del tipo Cuerda
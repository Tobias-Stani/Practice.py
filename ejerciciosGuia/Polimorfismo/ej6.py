from abc import ABC, abstractmethod

# Interfaz Identificable
class Identificable(ABC):
    @abstractmethod
    def queInstrumentoEres(self):
        pass

# Clase abstracta Instrumento
class Instrumento(ABC):
    numeroInstrumentos = 0  # Variable estática que cuenta todos los instrumentos

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
        Instrumento.numeroInstrumentos += 1  # Incrementa el contador de instrumentos

    @abstractmethod
    def afinar(self):
        pass  # Método abstracto que debe ser implementado en las subclases

    @classmethod
    def mostrar_numero_instrumento(cls):
        return f"Total de instrumentos: {cls.numeroInstrumentos}"  # Método de clase para mostrar el número total

# Clase Viento
class Viento(Instrumento, Identificable):
    numInstrVientoMetal = 0  # Variable estática para instrumentos de viento de metal
    numInstrVientoMadera = 0  # Variable estática para instrumentos de viento de madera

    def __init__(self, tipo_material, nombre, precio):
        super().__init__(nombre, precio)  # Llama al constructor de la clase base
        if tipo_material == "metal":
            Viento.numInstrVientoMetal += 1  # Incrementa contador de instrumentos de metal
        elif tipo_material == "madera":
            Viento.numInstrVientoMadera += 1  # Incrementa contador de instrumentos de madera

    def afinar(self):
        return f"El instrumento de viento {self.nombre} suena con el viento."  # Implementación del método abstracto

    def esDeMetal(self):
        return "metal" in self.nombre.lower()  # Lógica simple para determinar si es de metal

    def queInstrumentoEres(self):
        return f"Soy un instrumento de viento llamado {self.nombre}."


# Clase Percusion
class Percusion(Instrumento, Identificable):
    numInstrPercusion = 0  # Variable estática para instrumentos de percusión

    def __init__(self, nombre, precio):
        super().__init__(nombre, precio)  # Llama al constructor de la clase base
        Percusion.numInstrPercusion += 1  # Incrementa contador de instrumentos de percusión

    def afinar(self):
        return f"El instrumento de percusión {self.nombre} golpea con un sonido vibrante."  # Implementación del método abstracto

    def queInstrumentoEres(self):
        return f"Soy un instrumento de percusión llamado {self.nombre}."


# Clase Cuerda
class Cuerda(Instrumento, Identificable):
    numInstrCuerda = 0  # Variable estática para instrumentos de cuerda

    def __init__(self, nombre, precio):
        super().__init__(nombre, precio)  # Llama al constructor de la clase base
        Cuerda.numInstrCuerda += 1  # Incrementa contador de instrumentos de cuerda

    def afinar(self):
        return f"El instrumento de cuerda {self.nombre} produce un sonido melódico al ser tocado."  # Implementación del método abstracto

    def queInstrumentoEres(self):
        return f"Soy un instrumento de cuerda llamado {self.nombre}."


# Ejemplo de uso
instrumento1 = Viento("metal", "Saxo", 1500)
instrumento2 = Percusion("Batería", 3000)
instrumento3 = Cuerda("Guitarra", 1200)

print(Viento.mostrar_numero_instrumento())  # Muestra el número total de instrumentos
print(instrumento1.afinar())  # Afinar el instrumento de viento
print(instrumento2.afinar())  # Afinar el instrumento de percusión
print(instrumento3.afinar())  # Afinar el instrumento de cuerda

print(instrumento1.queInstrumentoEres())  # Identificación del instrumento de viento
print(instrumento2.queInstrumentoEres())  # Identificación del instrumento de percusión
print(instrumento3.queInstrumentoEres())  # Identificación del instrumento de cuerda

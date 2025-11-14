from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def hacer_sonido():
        pass


class Perro(Animal):
    
    def hacer_sonido(self):
        print("Guau!")


class Gato(Animal):
    def hacer_sonido(self):
        print("Miau!")




def escuchar_animal(animal: Animal):
    animal.hacer_sonido()

gato = Gato()

perro = Perro()  # Aquí se crea el objeto
escuchar_animal(gato) 
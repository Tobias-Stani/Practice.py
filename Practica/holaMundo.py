class Celular:
    """constructor"""
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def llamar(self):
        print(f'estas haciendo una llamada: {self.modelo}')

celular1 = Celular('samsung', 's23')

print(celular1.llamar())

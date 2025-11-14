class Marino():
    
    def hablar(self):
        return "Hola, soy un animal marino"
    

class Pulpo(Marino):
    
    def hablar(self):
        return "Hola, soy un pulpo"
    
class Foca(Marino):
    def __init__(self, mensaje):
        self.mensaje = mensaje

    def hablar(self):
        return self.mensaje
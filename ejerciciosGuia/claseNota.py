class Nota:

    def __init__(self, valorInicial):
        if 0 <=valorInicial <=10:
            self._valor = valorInicial
        else:
            raise ValueError("El valor de la nota debe estar entre 0 y 10")
        
    def obtener_valor(self):
        return self._valor
    
    def aprobado(self):
        return self ._valor >= 6
    
    def desaprobado(self):
        return self._valor < 6
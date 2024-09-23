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

    def recuperar(self, nuevoValor):
        if 0 <= nuevoValor <= 10:
            if nuevoValor > self._valor:
                self._valor = nuevoValor
            else: 
                print(f"El nuevo valor {nuevoValor} no es superior al acutal : {self._valor}. La nota no se cambia")
        else:
            print("el valor de la nota debe estar entre 0 y 10.")
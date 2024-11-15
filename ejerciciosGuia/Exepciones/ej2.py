class MiClase:
    def metodo(self):
        print("Método invocado con éxito.")

# Paso 1: Definir una referencia a un objeto e inicializarla a None
referencia = None

# Paso 2: Intentar invocar un método usando esta referencia
try:
    referencia.metodo()  
except AttributeError as e:
    print("Se ha producido una excepción:", e)

# Paso 1: Crear una clase de excepción personalizada
class MiExcepcionPersonalizada(Exception):
    def __init__(self, mensaje):
        """
        Constructor que toma un mensaje y lo almacena como un atributo.
        """
        super().__init__(mensaje)  # Llamar al constructor de la clase base
        self.mensaje = mensaje

    def mostrar_mensaje(self):
        """
        Método para mostrar el mensaje almacenado.
        """
        return f"Excepción personalizada: {self.mensaje}"


# Paso 2: Probar la excepción personalizada dentro de un bloque try-except
try:
    # Lanza la excepción personalizada
    raise MiExcepcionPersonalizada("Este es un error personalizado.")
except MiExcepcionPersonalizada as e:
    # Manejar la excepción y mostrar el mensaje
    print("¡Se capturó una excepción personalizada!")
    print(e.mostrar_mensaje())

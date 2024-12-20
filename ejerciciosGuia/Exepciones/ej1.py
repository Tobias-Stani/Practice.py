class MiClase:
    def main(self):
        try:
            # Generamos una excepción con un mensaje
            raise Exception("Este es un mensaje de error personalizado.")
        except Exception as e:
            print(f"Se capturó una excepción: {e}")
        finally:
            print("Esto se imprime sin importar si hubo una excepción o no.")

# Crear un objeto de la clase y ejecutar el método main
if __name__ == "__main__":
    objeto = MiClase()
    objeto.main()

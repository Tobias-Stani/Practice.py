while True:
    try:
        # Intentar realizar una acción que puede fallar
        numero = int(input("Introduce un número entero: "))
        print(f"¡Número válido ingresado: {numero}!")
        break  # Salir del bucle si no ocurre ninguna excepción
    except ValueError:
        # Manejar la excepción y reintentar
        print("Error: No has introducido un número entero. Inténtalo de nuevo.")

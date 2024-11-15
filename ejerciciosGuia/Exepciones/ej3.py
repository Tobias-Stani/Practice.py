try:
    # Paso 1: Crear una lista
    mi_lista = [1, 2, 3, 4, 5]
    
    # Paso 2: Intentar acceder a un índice fuera del rango
    print(mi_lista[10])  # Esto genera un IndexError porque el índice 10 no existe
    
except IndexError as e:
    # Paso 3: Capturar y manejar la excepción
    print("Se ha producido una excepción: Índice fuera de rango.")
    print("Detalles del error:", e)


# Cola original A con clientes: cada cliente es una tupla (número de ubicación, cantidad de productos)
cola_A = [(1, 8), (2, 3), (3, 6), (4, 2), (5, 5)]

# Crear una nueva lista para la cola B
cola_B = []

# Crear una lista para los clientes que permanecerán en A
cola_A_nueva = []

# Recorrer cada cliente en la cola original
for cliente in cola_A:
    numero_ubicacion = cliente[0]  # Número de ubicación original
    cantidad_productos = cliente[1]  # Cantidad de productos que lleva el cliente

    # Si el cliente lleva menos de 5 productos, se mueve a la cola B
    if cantidad_productos < 5:
        cola_B.append(cliente)
    else:
        # Si el cliente lleva 5 o más productos, permanece en la cola A
        cola_A_nueva.append(cliente)

# Reasignar números de ubicación en la cola A
cola_A_final = []
for i in range(len(cola_A_nueva)):
    nuevo_numero = i + 1  # Los números de ubicación empiezan en 1
    cantidad_productos = cola_A_nueva[i][1]
    cola_A_final.append((nuevo_numero, cantidad_productos))

# Reasignar números de ubicación en la cola B
cola_B_final = []
for i in range(len(cola_B)):
    nuevo_numero = i + 1  # Los números de ubicación empiezan en 1
    cantidad_productos = cola_B[i][1]
    cola_B_final.append((nuevo_numero, cantidad_productos))

# Mostrar los resultados
print("Cola A (Clientes con 5 o más productos):", cola_A_final)
print("Cola B (Clientes con menos de 5 productos):", cola_B_final)

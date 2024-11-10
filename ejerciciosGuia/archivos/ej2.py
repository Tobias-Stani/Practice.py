def escribir_en_archivo(ruta, texto):
    """
    Esta función escribe el texto en el archivo ubicado en la ruta especificada.
    """
    with open(ruta, 'w') as archivo:  # Usa 'w' para sobrescribir el archivo si ya existe
        archivo.write(texto)
    print(f"Texto guardado en {ruta}.")


def mostrar_texto_alternado(texto):
    """
    Esta función convierte el texto alternando entre minúsculas y mayúsculas.
    """
    texto_alternado = ''
    for i, letra in enumerate(texto):
        if letra.isalpha():  # Solo alterna letras, deja otros caracteres igual
            if i % 2 == 0:
                texto_alternado += letra.lower()
            else:
                texto_alternado += letra.upper()
        else:
            texto_alternado += letra  # Deja otros caracteres sin cambios

    print("Texto alternado:", texto_alternado)
    return texto_alternado


# Solicitar la ruta del archivo y el texto al usuario
ruta_archivo = input("Introduce la ruta completa del archivo (ejemplo: '/ruta/archivo.txt'): ")
texto_usuario = input("Introduce el texto que deseas escribir en el archivo: ")

# Llamar a la función para escribir en el archivo
escribir_en_archivo(ruta_archivo, texto_usuario)

# Llamar a la función para mostrar el texto alternado
texto_alternado = mostrar_texto_alternado(texto_usuario)

# Crear un archivo de texto con contenido
contenido = "Esto es una prueba"
nombre_archivo = "archivo.txt"

try:
    with open(nombre_archivo, "w") as archivo:
        archivo.write(contenido)
    print(f"Archivo '{nombre_archivo}' creado exitosamente.")
except Exception as e:
    print(f"Error al crear el archivo: {e}")


# Función para leer y mostrar el contenido del archivo sin espacios
def leer_sin_espacios(nombre_archivo):
    try:
        with open(nombre_archivo, "r") as archivo:
            contenido = archivo.read()
        
        # Eliminar los espacios del contenido
        contenido_sin_espacios = contenido.replace(" ", "")
        
        print("Contenido sin espacios:", contenido_sin_espacios)
    
    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_archivo}' no fue encontrado.")
    except Exception as e:
        print(f"Ha ocurrido un error: {e}")

leer_sin_espacios("archivo.txt")

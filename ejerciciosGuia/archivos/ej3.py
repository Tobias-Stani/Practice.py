import os

def combinar_archivos(ruta_archivo1: str, ruta_archivo2: str, ruta_destino: str):
    """
    Combina el contenido de dos archivos en uno nuevo, que se guarda en la ruta de destino.
    """
    # Validar si los archivos de entrada existen
    if not os.path.exists(ruta_archivo1):
        print(f"El archivo {ruta_archivo1} no existe.")
        return
    if not os.path.exists(ruta_archivo2):
        print(f"El archivo {ruta_archivo2} no existe.")
        return

    # Obtener los nombres base de los archivos
    nombre_archivo1 = os.path.basename(ruta_archivo1)
    nombre_archivo2 = os.path.basename(ruta_archivo2)

    # Crear el nombre del archivo combinado
    nombre_destino = f"{os.path.splitext(nombre_archivo1)[0]}_{os.path.splitext(nombre_archivo2)[0]}.txt"
    ruta_archivo_destino = os.path.join(ruta_destino, nombre_destino)

    # Comprobar si el archivo destino ya existe
    if os.path.exists(ruta_archivo_destino):
        respuesta = input(f"El archivo {ruta_archivo_destino} ya existe. ¿Desea sobrescribirlo? (s/n): ").strip().lower()
        if respuesta != 's':
            print("Operación cancelada. No se ha creado ningún archivo nuevo.")
            return

    # Leer el contenido de los archivos originales
    try:
        with open(ruta_archivo1, "r", encoding="utf-8") as archivo1, \
             open(ruta_archivo2, "r", encoding="utf-8") as archivo2:
            contenido1 = archivo1.read()
            contenido2 = archivo2.read()
    except Exception as e:
        print(f"Ocurrió un error al leer los archivos: {e}")
        return

    # Escribir el contenido combinado en el nuevo archivo
    try:
        with open(ruta_archivo_destino, "w", encoding="utf-8") as archivo_destino:
            archivo_destino.write(contenido1 + contenido2)
        print(f"Archivo combinado creado exitosamente en: {ruta_archivo_destino}")
    except Exception as e:
        print(f"Ocurrió un error al escribir el archivo de destino: {e}")
        return

# Solicitar las rutas al usuario
ruta1 = input("Ingrese la ruta del primer archivo: ").strip()
ruta2 = input("Ingrese la ruta del segundo archivo: ").strip()
ruta_destino = input("Ingrese la ruta de destino (sin archivo al final): ").strip()

# Llamar a la función para combinar archivos
combinar_archivos(ruta1, ruta2, ruta_destino)


# with open('nuevo_archivo.txt', 'r') as archivo:
#     contenido = archivo.read()  
#     print(contenido)

with open('archivo.csv', 'r') as archivo_csv:
    next(archivo_csv) # Saltar la primera línea (encabezado)

    print("lee todo el archivo \n")

    for linea in archivo_csv:
        id, nombre, edad, ciudad = linea.strip().split(',')
        print(f"id: {id} - Nombre: {nombre} - Edad: {edad} -  Ciudad: {ciudad}")


with open('archivo.csv', 'r') as archivo_csv:
    next(archivo_csv)

    print("\nlee solo nombre, edad y ciudad \n")

    for linea in archivo_csv:
        columnas = linea.strip().split(',')
        nombre = columnas[1]
        ciudad = columnas[3]
        print(f"Nombre: {nombre} - Ciudad: {ciudad}")
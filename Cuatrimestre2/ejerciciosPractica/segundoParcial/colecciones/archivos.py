import csv

with open('archivo.csv', 'r+') as archivo_csv:
    lee = csv.reader(archivo_csv)
    filas = list(lee) # Convierte el lector en una lista de filas 

    print("Contenido original")
    for fila in filas[1:]:  # Saltar la primera fila (encabezado)
        print(fila)

    # Agregar una nueva fila
                            # Mover puntero al final
    archivo_csv.seek(0, 2)
    escritor = csv.writer(archivo_csv)
    nueva_fila = ['4', 'Tobias', '21', 'BsAs']
    escritor.writerow(nueva_fila)


with open('archivo.csv', 'r') as archivo_csv:
    lee = csv.reader(archivo_csv)
    next(lee)  # Saltar la primera fila (encabezado)
    print("\nContenido actualizado")
    for fila in lee:
        print(fila)
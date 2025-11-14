import csv 

def pedirNumero():
    while True:
        try:
            numero = int(input("Ingrese un número entero: "))
            return numero
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero.")


def guardarEnCSV(nombre_archivo, numero):
    with open(nombre_archivo, 'w') as archivo_csv:
        escritor = csv.writer(archivo_csv)


        # Escribir encabezado y número
        escritor.writerow(["Número guardado del usuario"])  # Escribir encabezado
        escritor.writerow([numero]) 

        # Espacio y encabezado de la tabla
        escritor.writerow([])
        escritor.writerow(["Tabla de multiplicar del número", numero])
        escritor.writerow(["Multiplicación", "Resultado"])
        
        # Escribir la tabla
        for i in range(1, 11):
            escritor.writerow([f"{numero} x {i}: ", numero * i])


if __name__ == "__main__":
    numero = pedirNumero()
    guardarEnCSV("numeros.csv", numero)
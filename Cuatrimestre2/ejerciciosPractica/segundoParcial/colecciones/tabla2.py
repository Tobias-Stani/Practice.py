import csv

def pedirNumero():
    while True:
        try:
            numero = int(input("Ingrese un número entero: "))
            return numero
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero.")

def leer_numero_guardado(nombre_archivo):
    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
        lineas = archivo.readlines()  # lee todas las líneas como lista
        numero = lineas[1].strip()    # línea 2 → índice 1
        return numero


if __name__ == "__main__":
    numero_guardado = leer_numero_guardado("numeros.csv")
    print(f"El número guardado es: {numero_guardado}")

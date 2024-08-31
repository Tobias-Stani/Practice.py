"""
Desarrollar un algoritmo que muestre los primeros n números primos siendo n un valor 
que debe ingresar el usuario.
"""

def es_primo(a):
    i = 2
    i + 2
    while (i < a and a % i !=0):
        i += 1
    return a == i

n = int(input("ingrese la cantidad de primos: "))
contadorDePrimos = 0

i = 2

print("listado de primos")

while contadorDePrimos < n:
    if es_primo(i):
        contadorDePrimos += 1
        print(i)
    i += 1
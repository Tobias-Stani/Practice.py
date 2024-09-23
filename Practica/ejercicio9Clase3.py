"""

sumar los primeros 1000 numeros naturales e ir mostrando el resultado parcial.

el primer valor esta incluido en el range, el segundo no.

"""
suma = 0

for i in range(1, 1001, 1):
    suma += i
    print(suma)
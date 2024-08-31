"""se ingresa por teclado un cojunto de valores numericos enteros positivos,
se pide informar,
por cada uno si el valor ingresado es par o impar, 
para indicar el final se ingresara un valor cero o negativo. """


valor = int(input("ingrese un valor entero positvo.: "))

while valor > 0:

    if valor%2 ==0:
        print("el valor ingresado es par.")
    else:
        print("es valor es impar.")
        
    valor = int(input("ingrese un valor entero positvo.: "))
# Solicitar al usuario una lista de números separados por comas
entrada = input("Introduce una lista de números separados por comas: ")

# Convertir la entrada en una lista de enteros
numeros = [int(num.strip()) for num in entrada.split(",")]

# Encontrar el número más grande
numero_mas_grande = max(numeros)
numeroMinimo = min(numeros)

# Mostrar el resultado
print("El número más grande es:", numero_mas_grande)
print("El número más chico es:", numeroMinimo)

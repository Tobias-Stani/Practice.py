class Lista:
    def __init__(self):
        self.elementos = []

    def agregar(self, elemento):
        self.elementos.append(elemento)
        print(f"agregado: {elemento}")

    def insertar(self, indice, elemento):
        if 0 <= indice <= len(self.elementos):
            self.elementos.insert(indice, elemento)
            print(f"Insertado {elemento} en la posicion {indice}")
        else:
            print("indice fuera del rango")

    def quitar_por_valor(self, elemento):
        try:
            self.elementos.remove(elemento)
            print(f"Quitado: {elemento}")
        except ValueError:
            print(f"Elemento {elemento}, no se encontro en la lista")

    def quitar_por_indice(self, indice):
        if 0 <= indice < len(self.elementos):
            elemento_quitado = self.elementos.pop(indice)
            print(f"Quitado: {elemento_quitado} de la posicion {indice}")
            return elemento_quitado
        
    def mostrar_lista(self):
        print("lista actual:", self.elementos)

# Uso de la clase
lista = Lista()

# Agregar elementos
lista.agregar("manzana")
lista.agregar("banana")
lista.agregar("naranja")

# Mostrar la lista
lista.mostrar_lista()

# Insertar un elemento
lista.insertar(1, "kiwi")
lista.mostrar_lista()

# Quitar un elemento por valor
lista.quitar_por_valor("banana")
lista.mostrar_lista()

# Quitar un elemento por índice
lista.quitar_por_indice(0)
lista.mostrar_lista()
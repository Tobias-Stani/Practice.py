import csv

class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
    
    def __str__(self):
        return f"El producto {self.nombre} tiene un precio de {self.precio} y una cantidad de {self.cantidad}"



class Inventario:
    def __init__(self):
            self.productos = []

    def agregar_producto(self, producto):
         self.productos.append(producto)

    def mostrar_productos(self):
        for producto in self.productos:
            print(f"  - {producto}")

    def total_inventario(self):
        """Calcula el valor total del inventario sumando precio * cantidad de cada producto"""
        total = 0
        for producto in self.productos:
            valor_producto = producto.precio * producto.cantidad
            total = total + valor_producto
        return total


inventario = Inventario()


def modificar_producto(nombre, nuevo_precio=None, nueva_cantidad=None):

    productos_actualizados = []

    # 1. Leo todo el CSV
    with open("productos.csv", "r") as archivo:
        lector = csv.DictReader(archivo)

        for fila in lector:
            # Si este es el producto a modificar
            if fila["nombre"] == nombre:
                if nuevo_precio is not None:
                    fila["precio"] = str(nuevo_precio)
                if nueva_cantidad is not None:
                    fila["cantidad"] = str(nueva_cantidad)

            productos_actualizados.append(fila)

    # 2. Reescribo el CSV con los datos nuevos
    with open("productos.csv", "w", newline='') as archivo:
        columnas = ["nombre", "precio", "cantidad"]
        escritor = csv.DictWriter(archivo, fieldnames=columnas)

        escritor.writeheader()                  # Escribe cabecera
        escritor.writerows(productos_actualizados)  # Escribe todas las filas

    print("¡Producto actualizado correctamente!")



def cargar_productos_desde_csv():
    with open("productos.csv", "r") as archivo:
         lector = csv.DictReader(archivo)
         for fila in lector:
              producto = Producto(fila["nombre"], float(fila["precio"]), int(fila["cantidad"]))
              inventario.agregar_producto(producto)
          

def modificar_producto_desde_menu():
    print("\n--- Modificar Producto ---")

    nombre = input("Nombre del producto a modificar: ")

    print("Si no querés cambiar un valor, dejalo vacío.\n")

    nuevo_precio = input("Nuevo precio: ")
    nueva_cantidad = input("Nueva cantidad: ")

    # Convertimos a None si dejan vacío
    nuevo_precio = float(nuevo_precio) if nuevo_precio else None
    nueva_cantidad = int(nueva_cantidad) if nueva_cantidad else None

    modificar_producto(nombre, nuevo_precio, nueva_cantidad)



def start():
    cargar_productos_desde_csv()

    print("Para ver los productos del inventario presione 'p'")
    print("Para modificar un producto presione 'm'")
    print("Para salir presione 'q'")
    
    opcion = input("Opción: ").lower()

    if opcion == "p":
        inventario.mostrar_productos()
        inventario_total = inventario.total_inventario()
        print()
        print(f"El valor total del inventario es: {inventario_total}")

    elif opcion == "m":
        modificar_producto_desde_menu()

    elif opcion == "q":
        print("Saliendo del programa.")
        return

    else:
        print("Opción inválida.")


if __name__ == "__main__":
    start()
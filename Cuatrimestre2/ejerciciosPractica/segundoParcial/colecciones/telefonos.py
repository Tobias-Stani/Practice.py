import csv

class Cliente:
    def __init__(self, nombre, telefono, empresa):
        self.nombre = nombre
        self.telefono = telefono
        self.empresa = empresa

    def __str__(self):
        return f"{self.nombre} ({self.telefono}) - {self.empresa}"
    
    
    
class Empresa:
    def __init__(self, nombre):
        self.nombre = nombre
        self.clientes = []

    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)
        
    def mostrar_clientes(self):
        for cliente in self.clientes:
            print(f"  - {cliente}")

    def __str__(self):
        return f"Empresa: {self.nombre}, Clientes: {len(self.clientes)}"
    

import csv

# Diccionario para guardar las empresas
# Clave: nombre de la empresa, Valor: objeto Empresa
empresas = {}

# Abrir el archivo CSV
with open("clientes.csv", "r") as archivo:
    lector = csv.DictReader(archivo)
    
    for fila in lector:
        # Validar que la fila tenga todos los datos necesarios
        nombre = fila.get("nombre")
        telefono = fila.get("telefono")
        empresa_nombre = fila.get("empresa")
        
        if not nombre or not telefono or not empresa_nombre:
            continue  # saltar filas incompletas
        
        # Crear el objeto Cliente
        cliente = Cliente(nombre, telefono, empresa_nombre)
        
        # Si la empresa no existe aÃºn, crear el objeto Empresa
        if empresa_nombre not in empresas:
            empresas[empresa_nombre] = Empresa(empresa_nombre)
        
        # Agregar el cliente a la empresa
        empresas[empresa_nombre].agregar_cliente(cliente)

# Mostrar empresas y sus clientes
for empresa in empresas.values():
    print(empresa)
    empresa.mostrar_clientes()
    print()  # línea en blanco entre empresas

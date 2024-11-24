import csv

# Definir la clase Empleado
class Empleado:
    def __init__(self, nombre, sector, salario):
        self.nombre = nombre
        self.sector = sector
        self.salario = float(salario)

    def __repr__(self):
        return f"Empleado(nombre={self.nombre}, sector={self.sector}, salario={self.salario})"

# Definir la clase GestionEmpleados
class GestionEmpleados:
    def __init__(self):
        self.empleados = []  # Lista para almacenar los empleados

    def leer_empleados(self, archivo):
        """Leer empleados desde un archivo CSV y guardarlos en la lista."""
        with open(archivo, "r") as f:
            lector_csv = csv.reader(f)
            for fila in lector_csv:
                nombre, sector, salario = fila
                # Crear un objeto Empleado y agregarlo a la lista
                empleado = Empleado(nombre, sector, salario)
                self.empleados.append(empleado)

    def agrupar_por_sector(self):
        """Agrupar empleados por sector."""
        diccionario_sectores = {}
        for empleado in self.empleados:
            # Si el sector no está en el diccionario, agregarlo
            if empleado.sector not in diccionario_sectores:
                diccionario_sectores[empleado.sector] = []
            # Agregar el empleado a la lista del sector correspondiente
            diccionario_sectores[empleado.sector].append(empleado)
        return diccionario_sectores

# Uso del programa
if __name__ == "__main__":
    # Crear una instancia de GestionEmpleados
    gestion = GestionEmpleados()

    # Leer el archivo empleados.csv
    gestion.leer_empleados("empleados.csv")

    # Agrupar empleados por sector
    empleados_por_sector = gestion.agrupar_por_sector()

    # Mostrar el resultado
    for sector, empleados in empleados_por_sector.items():
        print(f"Sector: {sector}")
        for empleado in empleados:
            print(f"  {empleado}")

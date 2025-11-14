from abc import ABC, abstractmethod

class Empleado(ABC):
    def __init__(self, nombre, dni, sueldo_base):
        self._nombre = nombre
        self._dni = dni
        self._sueldo_base = sueldo_base

    @abstractmethod
    def calcular_sueldo(self):
        pass

    @abstractmethod
    def mostrar_info(self):
       print(f"el empleado: {self._nombre}, va a cobrar {self.calcular_sueldo()}")
    

class EmpleadoPlanta(Empleado):
    def __init__(self, nombre, dni, sueldo_base, antiguedad):
        super().__init__(nombre, dni, sueldo_base)
        self._antiguedad = antiguedad

    def calcular_sueldo(self):
        return self._sueldo_base + (self._antiguedad * 1000)
    
    def mostrar_info(self):
        super().mostrar_info()


class EmpleadoTemporal(Empleado):
    def __init__(self, nombre, dni, sueldo_base, horas_trabajadas, valor_hora):
        super().__init__(nombre, dni, sueldo_base)
        self._horas_trabajadas = horas_trabajadas
        self._valor_hora = valor_hora

    def calcular_sueldo(self):
        return self._horas_trabajadas * self._valor_hora
    

    def mostrar_info(self):
        super().mostrar_info()
        

class Empresa():
    def __init__(self):
        self._empleados = []

    def agregar_emmpleado(self, empleado):
        self._empleados.append(empleado)

    def listar_empleados(self):
        for e in self._empleados:
            print(f"{e._nombre}, {e._dni}, {e._sueldo_base}")





planta = EmpleadoPlanta("tob", "458687", 10, 2)

# planta.mostrar_info()


temporal = EmpleadoTemporal("fer", "3333", 2, 4, 2)

# temporal.mostrar_info()

Mitesia = Empresa()
Mitesia.agregar_emmpleado(planta)

Mitesia.agregar_emmpleado(temporal)
Mitesia.listar_empleados()
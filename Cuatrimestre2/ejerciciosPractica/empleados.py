from abc import ABC, abstractmethod
    
class Empleado(ABC):
    def __init__(self, horas, antiguedad, hijos, casado):
        self._horas = horas
        self._antiguedad = antiguedad
        self._hijos = hijos
        self._casado = casado

    @abstractmethod
    def calcular_sueldo(self):
        pass

class Planta_permanente(Empleado):
    def __init__(self, horas, antiguedad, hijos, casado):
        super().__init__(horas, antiguedad, hijos, casado)
    
    def calcular_sueldo(self):
        sueldo_horas = self._horas * 300
        sueldo_antiguedad = self._antiguedad * 100
        sueldo_familiar = self._hijos * 200
        if self._casado:   # si casado es True
            sueldo_familiar += 100
        return sueldo_horas + sueldo_antiguedad + sueldo_familiar

class Gerente(Planta_permanente):
    def __init__(self, horas, antiguedad, hijos, casado):
        super().__init__(horas, antiguedad, hijos, casado)

    def calcular_sueldo(self):
        sueldo_horas = self._horas * 400
        sueldo_antiguedad = self._antiguedad * 150
        sueldo_familiar = self._hijos * 200
        casado = 0 
        return sueldo_horas + sueldo_antiguedad + sueldo_familiar

class Planta_temporal(Empleado):
    def __init__(self, horas, antiguedad, hijos, casado):
        super().__init__(horas, antiguedad, hijos, casado)

    def calcular_sueldo(self):
        sueldo_horas = self._horas * 200
        sueldo_familiar = self._hijos * 200
        if self._casado:   # si casado es True
            sueldo_familiar += 100
        return sueldo_horas + sueldo_familiar
    

class Empresa:
    def __init__(self):
        self._empleados = []   # lista para almacenar empleados

    def agregar_empleado(self, empleado):
        self._empleados.append(empleado)

    def monto_total(self):
        total = 0
        for empleado in self._empleados:
            total += empleado.calcular_sueldo()
        return total
    

empresa = Empresa()

e1 = Planta_permanente(160, 5, 2, True)   # 160 horas, 5 años, 2 hijos, casado
e2 = Planta_temporal(100, 0, 1, False)    # 100 horas, 0 antigüedad, 1 hijo
e3 = Gerente(200, 10, 3, True)           # 200 horas, 10 años, 3 hijos, casado
empresa.agregar_empleado(e1)
empresa.agregar_empleado(e2)
empresa.agregar_empleado(e3)
print("Monto total de sueldos a pagar:", empresa.monto_total())
from abc import ABC, abstractmethod

class Vehiculos(ABC):
    
    @abstractmethod
    def get_id(self):
        pass

    @abstractmethod
    def get_tiempo(self):
        pass

    @abstractmethod
    def set_id(self, id):
        pass

    @abstractmethod
    def set_tiempo(self, tiempo):
        pass

    def __str__(self):
        pass


class VehiculoCliente(Vehiculos):
    def __init__(self, id, tiempo=0):
        self._id = id
        self._tiempo = tiempo

    # Implementando los métodos abstractos
    def get_id(self):
        return self._id

    def get_tiempo(self):
        return self._tiempo
    
    def set_id(self, id):
        self._id = id
    
    def set_tiempo(self, tiempo):
        if tiempo < 0:
            raise ValueError("El tiempo no puede ser menor que 0.")
        self._tiempo = tiempo

    def __str__(self):
        return f"Vehiculo (ID: {self._id}, Tiempo: {self._tiempo} horas)"
    
    def factura(self):
        dias_completos = self._tiempo // 24
        horas_restantes = self._tiempo % 24

        costo_dias = dias_completos * 12  # $12 por día completo
        costo_horas = horas_restantes * 0.6  # $0.6 por hora

        costo_total = costo_dias + costo_horas

        return f"El costo total de su estadía es de ${costo_total:.2f}."


class VehiculoAbandonado(Vehiculos):
    def __init__(self, id, tiempo):
        self._id = id
        self._tiempo = tiempo

    # Implementando los métodos abstractos
    def get_id(self):
        return self._id

    def get_tiempo(self):
        return self._tiempo
    
    def set_id(self, id):
        self._id = id
    
    def set_tiempo(self, tiempo):
        if tiempo < 0:
            raise ValueError("El tiempo no puede ser menor que 0.")
        elif tiempo > 12:
            raise ValueError("El tiempo no puede ser mayor que 12.")
        self._tiempo = tiempo

    def factura(self):
        costo_por_mes = 200  # Costo por mes
        total = self._tiempo * costo_por_mes
        return f"El costo de la estancia por {self._tiempo} meses es de ${total:.2f}."


class VehiculoAbandonado(Vehiculos):
    def __init__(self, id, tiempo):
        self._id = id
        self._tiempo = tiempo

    # Implementando los métodos abstractos
    def get_id(self):
        return self._id

    def get_tiempo(self):
        return self._tiempo
    
    def set_id(self, id):
        self._id = id

    def set_tiempo(self, tiempo):
        if tiempo < 0:
            raise ValueError("El tiempo no puede ser menor que 0.")
        self._tiempo = tiempo

    def factura(self):
        costo_por_dia = 10  
        total = self._tiempo * costo_por_dia
        return f"El costo de la estancia por {self._tiempo} dias es de ${total:.2f}."


# Ejemplo de uso
vehiculo = VehiculoAbandonado("ABC123", tiempo=3)
print(vehiculo.factura())  # Imprime el costo para un vehículo abandonado

vehiculo_cliente = VehiculoCliente("DEF456", tiempo=50)  # 50 horas
print(vehiculo_cliente.factura())  # Imprime el costo de la estancia del cliente

vehiculo_Abandonado = VehiculoAbandonado("CRR777", tiempo=10)
print(vehiculo_Abandonado.factura())
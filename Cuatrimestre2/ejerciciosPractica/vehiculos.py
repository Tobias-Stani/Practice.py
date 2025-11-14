from abc import ABC, abstractmethod

class Vehiculo(ABC):
    def __init__(self, id, tiempo):
        self._id = id
        self._tiempo = tiempo

    @abstractmethod
    def info(self):
        pass

    @abstractmethod
    def factura(self):
        pass

class VehiculoCliente(Vehiculo):
    def __init__(self, id, tiempo = 0):
        super().__init__(id, tiempo)
    

    def get_tiempo(self):
        return self._tiempo

    def set_tiempo(self, tiempo):
        self._tiempo = tiempo

    def get_id(self):
        return self._id

    def factura(self):
        if self._tiempo > 24:
            costo = 12
        else:
            costo = 0.6
        
        total_pago = costo * self._tiempo
        return total_pago
    
    def info(self):
        print(f"El id es {self._id} y el tiempo es {self._tiempo} y el monto a pagar es {self.factura()}")
    
    def hay_plaza(self, libre):
        return libre > 0
    
class VehiculoAbonado(Vehiculo):
    def __init__(self,id, tiempo):
        super().__init__(id, tiempo)


    def info(self):
        pass

    def factura(self):
        total_pago = self._tiempo * 200
        return total_pago
    
    def hay_plaza(self, libre):
        return libre > 0
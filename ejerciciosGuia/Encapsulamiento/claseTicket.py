class Ticket:

    def __init__(self):
        self._importe = 0
        self._abierto = True
        self._descuentoAplicado = False
        self._productosContador = 0

    def ticket(self):
        return self._importe
    
    def agregarItem(self, cantidad, precioUnitario):
        if cantidad > 0 and precioUnitario > 0:
            if self._abierto:
                self._importe += cantidad * precioUnitario
                self._productosContador += cantidad
            else:
                print("El ticket esta cerrado.")
    

    def aplicarDescuento(self, porcentaje):
        if self._abierto and not self._descuentoAplicado:
            descuento = (porcentaje / 100) * self._importe
            self._importe -= descuento
            print(f"Descuento del {porcentaje}% aplicado.")
        else:
            print("descuento no aplicable o ticket cerrado")

        self._descuentoAplicado = True


    def calcularSubtotal(self):
        return self._importe
    
    def calcularTotal(self):
        self._abierto = False
        return self._importe
    
    def contarProductos(self):
        return self._productosContador
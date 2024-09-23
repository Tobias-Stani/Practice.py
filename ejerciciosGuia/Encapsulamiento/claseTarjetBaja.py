class TarjetaBaja:

    def __init__(self, saldoInicial):
        self._saldo = saldoInicial
        self._contadorViajes = 0
        self._contadorViajesColectivo = 0
        self._contadorViajesSubte = 0

    def tarjetaBaja(self):
        return self._saldo
    
    def cargar(self, monto):
        if monto > 0:
            self._saldo += monto
        return self._saldo
    
    def pagarViajeEnColectivo(self):
        costoViaje = 21.50
        if self._saldo >= costoViaje:
            self._saldo -= costoViaje
            self._contadorViajes += 1
            self._contadorViajesColectivo += 1
            print(f"pago exitoso para viaje en colectivo, se descontaron {costoViaje} del saldo")

    def pagarViajeEnSubte(self):
        costoViaje = 19.50
        if self._saldo >= costoViaje:
            self._saldo -= costoViaje
            self._contadorViajes += 1
            self._contadorViajesSubte += 1
            print(f"pago exitoso para viaje en subte, se descontaron {costoViaje} del saldo")
        
    def contarViajes(self):
        return self._contadorViajes
    
    def contarViajesColectivo(self):
        return self._contadorViajesColectivo
    
    def contarViajesSubte(self):
        return self._contadorViajesSubte
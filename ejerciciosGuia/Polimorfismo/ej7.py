from abc import ABC, abstractmethod

class Salida(ABC):
    @abstractmethod
    def imprimirCuenta(self):
        pass

class Cuenta(Salida):
    def __init__(self, nCuenta, propietario, saldo, interes):
        self.nCuenta = nCuenta  
        self.propietario = propietario 
        self.saldo = saldo  
        self.interes = interes  

    def imprimirCuenta(self):
        return f"El saldo actual es de: ${self.saldo:.2f}, el propietario de la cuenta es: {self.propietario}"

    def get_saldo(self):
        return self.saldo
    
    def get_interes(self):
        return self.interes
    
    def set_saldo(self, saldo):
        self.saldo = saldo

    def set_interes(self, interes):
        self.interes = interes

    def actualizarSaldo(self):
        intereses = self.saldo * self.interes
        self.saldo += intereses
        return f"El saldo actualizado es: ${self.saldo:.2f}"


class Banco:
    def __init__(self):
        self.lista_cuentas = []

    def crearCuenta(self, nCuenta, propietario, saldo, interes):
        # Verificar si la cuenta ya existe por número de cuenta
        for c in self.lista_cuentas:
            if c.nCuenta == nCuenta:
                print("Ya existe esta cuenta.")
                return
        
        # Crear y agregar la nueva cuenta
        nueva_cuenta = Cuenta(nCuenta=nCuenta, propietario=propietario, saldo=saldo, interes=interes)
        self.lista_cuentas.append(nueva_cuenta)
        print(f"Cuenta {nueva_cuenta.nCuenta} creada exitosamente.")


    def actualizarCuentas(self):
        # Actualizar el saldo de todas las cuentas
        for cuenta in self.lista_cuentas:
            print(cuenta.actualizarSaldo())

    def mostrarCuentas(self):
        # Mostrar los detalles de todas las cuentas
        for cuenta in self.lista_cuentas:
            print(cuenta.imprimirCuenta())

    def borrarCuenta(self, nCuenta):
        # Borrar una cuenta por número de cuenta
        for cuenta in self.lista_cuentas:
            if cuenta.nCuenta == nCuenta:
                self.lista_cuentas.remove(cuenta)
                print(f"Cuenta {nCuenta} eliminada.")
                return
        print(f"No se encontró la cuenta {nCuenta}.")



def mostrar_menu():
    print("\nMenú de opciones:")
    print("1. Crear cuenta")
    print("2. Borrar cuenta")
    print("3. Actualizar cuentas (aplicar intereses)")
    print("4. Mostrar cuentas")
    print("5. Salir")

def main():
    banco = Banco()

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            # Crear cuenta
            nCuenta = int(input("Ingrese el número de cuenta: "))
            propietario = input("Ingrese el nombre del propietario: ")
            saldo = float(input("Ingrese el saldo inicial: "))
            interes = float(input("Ingrese el interés (ej. 0.05 para 5%): "))
            banco.crearCuenta(nCuenta, propietario, saldo, interes)

        elif opcion == "2":
            # Borrar cuenta
            nCuenta = int(input("Ingrese el número de la cuenta a eliminar: "))
            banco.borrarCuenta(nCuenta)

        elif opcion == "3":
            # Actualizar cuentas
            banco.actualizarCuentas()

        elif opcion == "4":
            # Mostrar cuentas
            banco.mostrarCuentas()

        elif opcion == "5":
            # Salir
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()
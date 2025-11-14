from abc import ABC, abstractmethod


class Sociedades(ABC):
    def __init__(self, denominacion_social, domicilio, capital, cuit):
        self._denominacion_social = denominacion_social
        self._domicilio = domicilio
        self._capital = capital
        self._cuit = cuit


class SA(Sociedades):
    def __init__(self, denominacion_social, domicilio, capital, cuit, cant_acciones, precio, cotiza, directores):
        super().__init__(denominacion_social, domicilio, capital, cuit)
        self._cant_acciones = cant_acciones
        self._precio = precio
        self._cotiza = cotiza
        self._directores = directores

    def info(self):
        return print(f"razon soc: {self._denominacion_social}, domicilio: {self._domicilio}, capital: {self._capital}, cantidad de acciones: {self._cant_acciones}, precio: {self._precio}, cotiza: {self._cotiza}")
    

class Srl(Sociedades):
    def __init__(self, denominacion_social, domicilio, capital, cuit):
        super().__init__(denominacion_social, domicilio, capital, cuit)
        self._socios_gerentes = []
        self._socios_no_gerentes = []
    
    def agregar_socio_gerente(self, nombre, patrimonio):
         if len(self._socios_gerentes) < 3:
            self._socios_gerentes.append({"nombre": nombre, "patrimonio": patrimonio})
            print(f"socio gerente {nombre} agregado correctamente.")
         else:
             print("No se puede agregar mas de 3 socios gerentes.")
            

    def agregar_socio_no_gerente(self, nombre, patrimonio):
         self._socios_no_gerentes.append({"nombre": nombre, "patrimonio": patrimonio})
         
    def listar_socios_gerente(self):
        for socio in self._socios_gerentes:
            print(f"nombre: {socio['nombre']}, con un patrimonio de {socio['patrimonio']}")

    def listar_socio_no_gerente(self):
        for socio in self._socios_no_gerentes:
            print(f"nombre: {socio['nombre']}, con un patrimonio de {socio['patrimonio']}")

         

class Sh(Sociedades):
    def __init__(self, denominacion_social, domicilio, capital, cuit):
            super().__init__(denominacion_social, domicilio, capital, cuit)
            self._lista_de_socios = []

    def agregar__socio(self, nombre, porcentaje):
        self._lista_de_socios.append({"nombre": nombre, "porcentaje": porcentaje})

    def ver_socios(self):
         for socio in self._lista_de_socios:
            print(socio["nombre"], socio["porcentaje"])


def main():
    socio = Sh("mitesia", "figuero alcorta", 90, "235444556")

    srl = Srl("el fauno", "noguera", 10, "233344432")

    socio.agregar__socio("tobias", 40)

    socio.agregar__socio("fernando", 5)

    socio.agregar__socio("karina", 10)

    srl.agregar_socio_gerente("yo", 0.001)

    socio.ver_socios()

    print("----Socio de SRL que es gerente----")
    srl.listar_socios_gerente()


if __name__ == "__main__":
    main()
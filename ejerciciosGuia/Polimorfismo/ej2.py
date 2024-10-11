from abc import ABC, abstractmethod

# Clase base abstracta
class Sociedad(ABC):
    def __init__(self, denominacion, domicilio, capital, cuit):
        self.denominacion = denominacion
        self.domicilio = domicilio
        self.capital = capital
        self.cuit = cuit

    @abstractmethod
    def mostrar_informacion(self):
        pass

    def comparar_capital(self, otra_sociedad):
        if self.capital > otra_sociedad.capital:
            return f"{self.denominacion} tiene más capital que {otra_sociedad.denominacion}."
        elif self.capital < otra_sociedad.capital:
            return f"{otra_sociedad.denominacion} tiene más capital que {self.denominacion}."
        else:
            return "Ambas sociedades tienen el mismo capital."


# Subclase Sociedad Anónima
class SociedadAnonima(Sociedad):
    def __init__(self, denominacion, domicilio, capital, cuit, acciones, precio_accion, cotiza, directores):
        super().__init__(denominacion, domicilio, capital, cuit)
        self.acciones = acciones
        self.precio_accion = precio_accion
        self.cotiza = cotiza  # True o False
        self.directores = directores

    def mostrar_informacion(self):
        cotiza_bolsa = "Sí" if self.cotiza else "No"
        return (f"Sociedad Anónima: {self.denominacion}\n"
                f"Domicilio: {self.domicilio}\nCapital: {self.capital}\nCUIT: {self.cuit}\n"
                f"Acciones: {self.acciones}\nPrecio por acción: {self.precio_accion}\n"
                f"Cotiza en bolsa: {cotiza_bolsa}\nDirectores: {self.directores}")


# Subclase SRL
class SRL(Sociedad):
    def __init__(self, denominacion, domicilio, capital, cuit, socios_gerentes, patrimonios, no_gerentes):
        super().__init__(denominacion, domicilio, capital, cuit)
        self.socios_gerentes = socios_gerentes
        self.patrimonios = patrimonios
        self.no_gerentes = no_gerentes

    def mostrar_informacion(self):
        socios_info = "\n".join([f"Socio gerente: {nombre}, Patrimonio: {patrimonio}"
                                for nombre, patrimonio in zip(self.socios_gerentes, self.patrimonios)])
        return (f"SRL: {self.denominacion}\n"
                f"Domicilio: {self.domicilio}\nCapital: {self.capital}\nCUIT: {self.cuit}\n"
                f"{socios_info}\nCantidad de socios no gerentes: {self.no_gerentes}")


# Subclase SH
class SH(Sociedad):
    def __init__(self, denominacion, domicilio, capital, cuit, socios, participaciones):
        super().__init__(denominacion, domicilio, capital, cuit)
        self.socios = socios
        self.participaciones = participaciones

    def mostrar_informacion(self):
        socios_info = "\n".join([f"Socio: {nombre}, Participación: {participacion}%"
                                for nombre, participacion in zip(self.socios, self.participaciones)])
        return (f"Sociedad de Hecho (SH): {self.denominacion}\n"
                f"Domicilio: {self.domicilio}\nCapital: {self.capital}\nCUIT: {self.cuit}\n"
                f"{socios_info}")

# Programa principal usando polimorfismo
def mostrar_informacion_sociedad(sociedad):
    print(sociedad.mostrar_informacion())
    print()

# Ejemplo de uso
sa = SociedadAnonima("Tech SA", "Calle Falsa 123", 1000000, "30-12345678-9", 10000, 100, True, 5)
srl = SRL("Innova SRL", "Av. Siempre Viva 456", 500000, "30-87654321-9", ["Juan", "Pedro"], [100000, 150000], 2)
sh = SH("Consultores SH", "Boulevard Central 789", 300000, "20-12345678-0", ["Ana", "Luis"], [50, 50])

# Mostrar información de cada sociedad
mostrar_informacion_sociedad(sa)
mostrar_informacion_sociedad(srl)
mostrar_informacion_sociedad(sh)

# Comparar capital de dos sociedades
print(sa.comparar_capital(srl))

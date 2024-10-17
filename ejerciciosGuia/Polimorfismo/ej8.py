class Unidad:
    def __init__(self, salud, daño):
        self.salud = salud
        self.daño = daño

    def atacar(self, unidad_objetivo):
        """Ataca a otra unidad si es posible"""
        if self.salud <= 0:
            print(f"{self.__class__.__name__} está muerto y no puede atacar.")
            return False
        self.realizar_ataque(unidad_objetivo)

    def recibir_daño(self, daño):
        self.salud -= daño
        if self.salud <= 0:
            print(f"{self.__class__.__name__} ha muerto.")
    
    def realizar_ataque(self, unidad_objetivo):
        """Método abstracto que se implementa en las subclases"""
        pass


class Soldado(Unidad):
    def __init__(self):
        super().__init__(200, 10)
        self.energia = 100

    def realizar_ataque(self, unidad_objetivo):
        if self.energia >= 10:
            print(f"Soldado ataca a {unidad_objetivo.__class__.__name__} e inflige {self.daño} de daño.")
            unidad_objetivo.recibir_daño(self.daño)
            self.energia -= 10
        else:
            print("Soldado no tiene suficiente energía para atacar.")

    def restaurar_energia(self):
        """Restaurar energía con ración de agua"""
        self.energia += 20
        print("Soldado ha restaurado su energía.")


class Arquero(Unidad):
    def __init__(self):
        super().__init__(50, 5)
        self.flechas = 20

    def realizar_ataque(self, unidad_objetivo, distancia):
        if 2 <= distancia <= 5:
            if self.flechas > 0:
                print(f"Arquero ataca a {unidad_objetivo.__class__.__name__} desde {distancia} de distancia e inflige {self.daño} de daño.")
                unidad_objetivo.recibir_daño(self.daño)
                self.flechas -= 1
            else:
                print("Arquero no tiene suficientes flechas.")
        else:
            print("El objetivo está fuera del alcance del Arquero.")

    def recargar_flechas(self):
        """Recargar el carcaj de flechas"""
        self.flechas += 6
        print("Arquero ha recargado su carcaj.")


class Lancero(Unidad):
    def __init__(self):
        super().__init__(150, 25)

    def realizar_ataque(self, unidad_objetivo, distancia):
        if 1 <= distancia <= 3:
            print(f"Lancero ataca a {unidad_objetivo.__class__.__name__} desde {distancia} de distancia e inflige {self.daño} de daño.")
            unidad_objetivo.recibir_daño(self.daño)
        else:
            print("El objetivo está fuera del alcance del Lancero.")


class Caballero(Unidad):
    def __init__(self):
        super().__init__(200, 50)
        self.ataques_realizados = 0
        self.rebelde = False

    def realizar_ataque(self, unidad_objetivo, distancia):
        if self.rebelde:
            print("El caballo del Caballero está rebelde, no puede atacar.")
        elif 1 <= distancia <= 2:
            print(f"Caballero ataca a {unidad_objetivo.__class__.__name__} desde {distancia} de distancia e inflige {self.daño} de daño.")
            unidad_objetivo.recibir_daño(self.daño)
            self.ataques_realizados += 1
            if self.ataques_realizados == 3:
                self.rebelde = True
                print("El caballo del Caballero se ha puesto rebelde.")
        else:
            print("El objetivo está fuera del alcance del Caballero.")

    def calmar_caballo(self):
        """Calmar el caballo rebelde con agua"""
        self.rebelde = False
        self.ataques_realizados = 0
        print("Caballo del Caballero ha sido calmado.")

# Ejemplo de juego
if __name__ == "__main__":
    soldado = Soldado()
    arquero = Arquero()
    lancero = Lancero()
    caballero = Caballero()

    # Soldado ataca a Lancero
    soldado.atacar(lancero)
    print(f"Salud del Lancero: {lancero.salud}")

    # Arquero ataca a Soldado a distancia 3
    arquero.realizar_ataque(soldado, 3)
    print(f"Salud del Soldado: {soldado.salud}")

    # Lancero ataca a Caballero a distancia 2
    lancero.realizar_ataque(caballero, 2)
    print(f"Salud del Caballero: {caballero.salud}")

    # Caballero ataca a Arquero a distancia 1
    caballero.realizar_ataque(arquero, 1)
    print(f"Salud del Arquero: {arquero.salud}")

    # Caballero realiza varios ataques hasta que su caballo se rebela
    caballero.realizar_ataque(arquero, 1)
    caballero.realizar_ataque(arquero, 1)

    # Caballero calma su caballo
    caballero.calmar_caballo()
    caballero.realizar_ataque(arquero, 1)

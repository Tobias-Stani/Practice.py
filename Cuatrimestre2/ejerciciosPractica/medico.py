from abc import ABC, abstractmethod

# ---------- Interfaz ----------
class Curacion(ABC):
    @abstractmethod
    def curar(self) -> str:
        """Realiza la acción de curar y devuelve la enfermedad tratada."""
        pass

# ---------- Clase base ----------
class EmpleadoHospital(ABC):
    ESPECIALIDADES = ("Pediatra", "Cirujano Abdomen", "Cirujano Corazón")

    def __init__(self, nombre, apellido, edad, especialidad):
        if especialidad not in self.ESPECIALIDADES:
            raise ValueError(f"Especialidad inválida: {especialidad}")
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad
        self._especialidad = especialidad

    # getters útiles
    def get_nombre(self):
        return self._nombre

    def get_apellido(self):
        return self._apellido

    def get_especialidad(self):
        return self._especialidad

    @abstractmethod
    def mostrar_info(self):
        pass

# ---------- Subclases (implementan Curacion) ----------
class MedicoPediatra(EmpleadoHospital, Curacion):
    def __init__(self, nombre, apellido, edad, cantidad_pacientes):
        super().__init__(nombre, apellido, edad, "Pediatra")
        self._cantidad_pacientes = cantidad_pacientes

    def get_cantidad_pacientes(self):
        return self._cantidad_pacientes

    def curar(self) -> str:
        # devuelve la enfermedad tratada (puede usarse por el método puente)
        return "Enfermedad Infantil"

    def mostrar_info(self):
        print(f"Pediatra: {self._nombre} {self._apellido}, {self._edad} años. Pacientes: {self._cantidad_pacientes}")

class MedicoCirujanoAbdomen(EmpleadoHospital, Curacion):
    def __init__(self, nombre, apellido, edad, cantidad_cirugias):
        super().__init__(nombre, apellido, edad, "Cirujano Abdomen")
        self._cantidad_cirugias = cantidad_cirugias

    def get_cantidad_cirugias(self):
        return self._cantidad_cirugias

    def curar(self) -> str:
        return "Enfermedad de Abdomen"

    def mostrar_info(self):
        print(f"Cirujano de Abdomen: {self._nombre} {self._apellido}, {self._edad} años. Cirugías: {self._cantidad_cirugias}")

class MedicoCirujanoCorazon(EmpleadoHospital, Curacion):
    def __init__(self, nombre, apellido, edad, cantidad_bypass):
        super().__init__(nombre, apellido, edad, "Cirujano Corazón")
        self._cantidad_bypass = cantidad_bypass

    def get_cantidad_bypass(self):
        return self._cantidad_bypass

    def curar(self) -> str:
        return "Enfermedad de Corazón"

    def mostrar_info(self):
        print(f"Cirujano de Corazón: {self._nombre} {self._apellido}, {self._edad} años. Bypass realizados: {self._cantidad_bypass}")

# ---------- Método puente (polimorfismo) ----------
def aplicar_curacion(personal: Curacion):
    """
    Método puente: recibe cualquier objeto que implemente Curacion
    y ejecuta su curar() sin preguntar su tipo concreto.
    """
    enfermedad = personal.curar()
    print(f"{personal.get_nombre()} {personal.get_apellido()} -> cura: {enfermedad}")

# ---------- Clase Hospital ----------
class Hospital:
    def __init__(self, nombre):
        self._nombre = nombre
        self._empleados = []

    def agregar_empleado(self, empleado: EmpleadoHospital):
        self._empleados.append(empleado)

    def procesar_lista(self):
        """
        Muestra datos de cada empleado, dice qué cura (usando polimorfismo)
        y al final informa:
          - cantidad total de pacientes de Pediatría
          - cantidad de cirujanos de abdomen
        """
        total_pacientes_pediatria = 0
        total_cirujanos_abdomen = 0

        print(f"--- Hospital: {self._nombre} ---")
        for e in self._empleados:
            e.mostrar_info()
            # si implementa Curacion, pedimos qué cura
            if isinstance(e, Curacion):
                enfermedad = e.curar()
                print(f"-> Cura: {enfermedad}")
            else:
                print("-> No realiza curaciones")

            # conteos específicos
            if isinstance(e, MedicoPediatra):
                total_pacientes_pediatria += e.get_cantidad_pacientes()
            if isinstance(e, MedicoCirujanoAbdomen):
                total_cirujanos_abdomen += 1
            print("")

        print(f"Total pacientes en Pediatría: {total_pacientes_pediatria}")
        print(f"Total cirujanos de abdomen: {total_cirujanos_abdomen}")

# ---------- Ejemplo / main ----------
def main():
    # crear médicos
    pediatra = MedicoPediatra("Lucía", "Gómez", 40, cantidad_pacientes=20)
    cir_abd = MedicoCirujanoAbdomen("Carlos", "Pérez", 50, cantidad_cirugias=15)
    cir_cor = MedicoCirujanoCorazon("María", "Fernández", 45, cantidad_bypass=8)

    # usar método puente (polimorfismo)
    aplicar_curacion(pediatra)
    aplicar_curacion(cir_abd)
    aplicar_curacion(cir_cor)
    print()

    # Hospital y conteos
    h = Hospital("San Buenaventura")
    h.agregar_empleado(pediatra)
    h.agregar_empleado(cir_abd)
    h.agregar_empleado(cir_cor)

    h.procesar_lista()

if __name__ == "__main__":
    main()

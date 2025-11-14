from abc import ABC, abstractmethod

class Cancion(ABC):
    def __init__(self, numero_ref, titulo, album, grupo):
        self._numero_ref = numero_ref
        self._titulo = titulo
        self._album = album
        self._grupo = grupo

    @abstractmethod
    def imprimirCancion(self):
        pass

    @abstractmethod
    def crear(self, lista_canciones):
        pass

    @abstractmethod
    def eliminar(self, lista_canciones):
        pass

    @abstractmethod
    def listado(self, lista_canciones):
        pass


class Clasica(Cancion):
    def __init__(self, numero_ref, titulo, album, grupo, instrumentos):
        super().__init__(numero_ref, titulo, album, grupo)
        self._instrumentos = instrumentos

    def imprimirCancion(self):
        print(f"Ref: {self._numero_ref}, Título: {self._titulo}, Álbum: {self._album}, Grupo: {self._grupo}, Instrumentos: {', '.join(self._instrumentos)}")

    @staticmethod
    def crear(lista_canciones, numero_ref, titulo, album, grupo, instrumentos):
        nueva = Clasica(numero_ref, titulo, album, grupo, instrumentos)
        lista_canciones.append(nueva)
        print(f"Canción '{titulo}' agregada.")
        return nueva

    @staticmethod
    def eliminar(lista_canciones, numero_ref):
        for c in lista_canciones:
            if c._numero_ref == numero_ref:
                lista_canciones.remove(c)
                print(f"Canción con ref {numero_ref} eliminada.")
                return True
        print(f"No se encontró la canción con ref {numero_ref}.")
        return False

    @staticmethod
    def listado(lista_canciones):
        print("Listado de canciones:")
        for c in lista_canciones:
            c.imprimirCancion()
        if not lista_canciones:
            print("No hay canciones en la base de datos.")


# --- Ejemplo de uso ---
def main():
    canciones = []

    # Crear canciones
    Clasica.crear(canciones, 1, "Canon en D", "Barroco", "Pachelbel", ["violín", "cello"])
    Clasica.crear(canciones, 2, "Concierto de Aranjuez", "Conciertos", "Rodrigo", ["guitarra", "orquesta"])
    Clasica.crear(canciones, 3, "Fur Elise", "Piano Solo", "Beethoven", ["piano"])

    # Listar canciones
    Clasica.listado(canciones)

    # Eliminar una canción
    Clasica.eliminar(canciones, 2)

    # Listar después de eliminar
    Clasica.listado(canciones)


if __name__ == "__main__":
    main()

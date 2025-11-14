class Libro():
    def __init__(self, titulo, autor, anio):
        self._titulo = titulo
        self._autor = autor
        self._anio = anio

    def info(self):
        return print(f"titulo del libro: {self._titulo}, el autor es: {self._autor}, el anio es {self._anio}")
    

    def get_titulo(self):
        return self._titulo

class LibroFisica(Libro):
    def __init__(self, titulo, autor, anio, tema):
        super().__init__(titulo, autor, anio )
        self._tema = tema

    
    def info(self):
        super().info()
        print(f"el tema es: {self._tema}")
    

class LibroLiteratura(Libro):
    def __init__(self, titulo, autor, anio, genero):
        super().__init__(titulo, autor, anio)
        self._genero = genero

    def get_titulo(self):
        return self._titulo

    def info(self):
        super().info()
        print(f"el genero es: {self._genero}")


class Biblioteca:
    def __init__(self):
        self._libros = []

    def agregarLibro(self, libro):
        self._libros.append(libro)

    def listarLibros(self):
        for l in self._libros:
            l.info()
            print("---")
        
    def eliminarLibro(self, titulo):
        for libro in self._libros:
            if libro.get_titulo() == titulo:
                self._libros.remove(libro)
                print(f"libro {titulo}, eliminado")
                return True
        
        print(f"No se encontro el libro {titulo}")
        return False
    
    # def modificarLista(self, titulo, nuevoValor):
    #     for libro in self._libros:
    #         if libro.get_titulo() == titulo:
    #             self._libros[0] = nuevoValor
    #             print(f"libro {titulo}, modificado")
    #             return True
        
    #     print(f"no se pudo modificar")
    #     return False
    
    def modificarLista(self, titulo, nuevo_titulo):
        for libro in self._libros:
            if libro.get_titulo() == titulo:
                libro._titulo = nuevo_titulo
                print(f"Libro '{titulo}' modificado a '{nuevo_titulo}'")
                return True

        print(f"No se pudo modificar: no se encontró el libro '{titulo}'")
        return False


def main():

    b = Biblioteca()

    libro1 = LibroLiteratura("el principito", "greta", 1930, "fantasia")
    libro2 = LibroFisica("el chabo", "mi papa", 2005, "qcy")

    b.agregarLibro(libro1)
    b.agregarLibro(libro2)

    b.modificarLista("el chabo", "harry potter")

    b.listarLibros()

if __name__ == "__main__":
    main()
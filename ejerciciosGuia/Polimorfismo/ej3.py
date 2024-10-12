from abc import ABC, abstractmethod

class Entregable(ABC):

    @abstractmethod
    def entregar(self):
        pass

    @abstractmethod
    def devolver(self):
        pass

    @abstractmethod
    def isEntregado(self):
        pass

    @abstractmethod
    def compareTo(self, other):
        pass



class Pelicula(Entregable):
    # Constructor por defecto
    def __init__(self, titulo="", año=0, genero="no definido", director=""):
        self.titulo = titulo
        self.año = año
        self.entregado = False  
        self.genero = genero
        self.director = director

    # Constructor con solo título y director (el resto por defecto)
    @classmethod
    def con_titulo_y_director(cls, titulo, director):
        return cls(titulo=titulo, director=director)

    # Constructor con todos los atributos excepto entregado
    @classmethod
    def con_todos(cls, titulo, año, genero, director):
        return cls(titulo=titulo, año=año, genero=genero, director=director)

    # Métodos getters
    def get_titulo(self):
        return self.titulo

    def get_año(self):
        return self.año

    def get_genero(self):
        return self.genero

    def get_director(self):
        return self.director

    # Métodos setters
    def set_titulo(self, titulo):
        self.titulo = titulo

    def set_año(self, año):
        self.año = año

    def set_genero(self, genero):
        self.genero = genero

    def set_director(self, director):
        self.director = director

    # Sobrescribir el método __str__ (equivalente al toString en Java)
    def __str__(self):
        return f"Película(Título: {self.titulo}, Año: {self.año}, Género: {self.genero}, Director: {self.director}, Entregado: {self.entregado})"


    #punto 4
    def entregar(self):
        self.entregado = True

    def devolver(self):
        self.entregado = False

    def isEntregado(self):
        return self.entregado
    
    def compareTo(self, other):
        if not isinstance(other, Pelicula):
            return NotImplemented
        if self.año > other.año:
            return 1
        elif self.año < other.año:
            return -1
        else:
            return 0


class Serie(Entregable):
    def __init__(self, titulo="", nTemporadas=3, entregado=False, genero="", creador=""):
        self.titulo = titulo
        self.nTemporadas = nTemporadas
        self.entregado = entregado
        self.genero = genero
        self.creador = creador

    @classmethod
    def titulo_y_creador(cls, titulo, creador):
        return cls(titulo=titulo, creador=creador)
    
    @classmethod
    def con_todos(cls, titulo, nTemporadas, genero, creador):
        return cls(titulo=titulo, nTemporadas=nTemporadas, genero=genero, creador=creador)
    
    # getters
    def get_titulo(self):
        return self.titulo
    
    def get_nTemporadas(self):
        return self.nTemporadas
    
    def get_genero(self):
        return self.genero
    
    def get_creador(self):
        return self.creador
    
    #setters
    def set_titulo(self, titulo):
        self.titulo = titulo

    def set_nTemporadas(self, nTemporadas):
        self.nTemporadas = nTemporadas
    
    def set_genero(self, genero):
        self.genero = genero

    def set_creador(self, creador):
        self.creador = creador

    def __str__(self):
        return f"Serie (titulo: {self.titulo}, numero temporadas: {self.nTemporadas}, genero: {self.genero}, creador: {self.creador})"


    #punto 4
    def entregar(self):
        self.entregado = True

    def devolver(self):
        self.entregado = False

    def isEntregado(self):
        return self.entregado

    def compareTo(self, other):
        if not isinstance(other, Serie):
            return NotImplemented
        if self.nTemporadas > other.nTemporadas:
            return 1
        elif self.nTemporadas < other.nTemporadas:
            return -1
        else:
            return 0

class Videojuego(Entregable):
    def __init__(self, titulo="", horas_estimadas=10, entregado=False, genero="", compania=""):
        self.titulo = titulo
        self.horas_estimadas = horas_estimadas
        self.entregado = entregado
        self.genero = genero
        self.compania = compania

    @classmethod
    def titulo_horas_estimadas(cls, titulo, horas_estimadas):
        return cls(titulo=titulo, horas_estimadas=horas_estimadas)
    
    @classmethod
    def con_todos(cls, titulo, horas_estimadas, genero, compania):
        return cls(titulo=titulo, horas_estimadas=horas_estimadas, genero=genero, compania=compania)
    

    def get_titulo(self):
        return self.titulo
    
    def get_horas_estimadas(self):
        return self.horas_estimadas
    
    def get_genero(self):
        return self.genero
    
    def get_compania(self):
        return self.compania
    
    #setters
    def set_titulo(self, titulo):
        self.titulo = titulo

    def set_horas_estimadas(self, horas_estimadas):
        self.horas_estimadas = horas_estimadas
    
    def set_genero(self, genero):
        self.genero = genero
    
    def set_compania(self, compania):
        self.compania = compania
    
    def __str__(self):
        return f"Video juego (titulo: {self.titulo}, horas estimadas: {self.horas_estimadas}, genero: {self.genero}, compania: {self.compania})"
    

    #punto4
    def entregar(self):
        self.entregado = True

    def devolver(self):
        self.entregado = False

    def isEntregado(self):
        return self.entregado

    # Método compareTo corregido para Videojuegos
    def compareTo(self, other):
        if not isinstance(other, Videojuego):
            return NotImplemented
        if self.horas_estimadas > other.horas_estimadas:
            return 1
        elif self.horas_estimadas < other.horas_estimadas:
            return -1
        else:
            return 0


## punto 5

def main():
    # 1. Crear los arrays (listas en Python)
    peliculas = [
        Pelicula("Inception", 2010, "Sci-Fi", "Christopher Nolan"),
        Pelicula("The Matrix", 1999, "Action", "Wachowski Brothers"),
        Pelicula("The Godfather", 1972, "Crime", "Francis Ford Coppola")
    ]
    
    series = [
        Serie("Breaking Bad", 5, "Drama", "Vince Gilligan"),
        Serie("Stranger Things", 4, "Sci-Fi", "The Duffer Brothers"),
        Serie("Friends", 10, "Comedy", "David Crane")
    ]
    
    videojuegos = [
        Videojuego("The Witcher 3", 100, "RPG", "CD Projekt"),
        Videojuego("Cyberpunk 2077", 200, "RPG", "CD Projekt"),
        Videojuego("The Last of Us", 30, "Action", "Naughty Dog")
    ]
    
    # 2. Entregar algunos videojuegos, películas y series
    peliculas[0].entregar()  # Entregar la película 'Inception'
    peliculas[2].entregar()  # Entregar 'The Godfather'
    
    series[1].entregar()  # Entregar 'Stranger Things'
    
    videojuegos[1].entregar()  # Entregar 'Cyberpunk 2077'
    
    # 3. Contar cuántos objetos están entregados
    entregados_peliculas = sum(1 for pelicula in peliculas if pelicula.isEntregado())
    entregados_series = sum(1 for serie in series if serie.isEntregado())
    entregados_videojuegos = sum(1 for videojuego in videojuegos if videojuego.isEntregado())

    print(f"Películas entregadas: {entregados_peliculas}")
    print(f"Series entregadas: {entregados_series}")
    print(f"Videojuegos entregados: {entregados_videojuegos}")
    
    # 4. Encontrar el videojuego con más horas estimadas
    videojuego_mas_horas = max(videojuegos, key=lambda v: v.get_horas_estimadas())
    
    # 5. Encontrar la serie con más temporadas
    serie_mas_temporadas = max(series, key=lambda s: s.get_nTemporadas())
    
    # 6. Encontrar la película más antigua
    pelicula_mas_antigua = min(peliculas, key=lambda p: p.get_año())
    
    # 7. Mostrar la información de los objetos encontrados
    print("\nVideojuego con más horas estimadas:")
    print(videojuego_mas_horas)
    
    print("\nSerie con más temporadas:")
    print(serie_mas_temporadas)
    
    print("\nPelícula más antigua:")
    print(pelicula_mas_antigua)


if __name__ == "__main__":
    main()
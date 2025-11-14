from pokemon import Pokemon

class Pikachu(Pokemon):

    __tipo = "Eléctrico"

    def __init__(self, nombre, nivel, salud, voltaje_max, amperaje_max, color):
        super().__init__(nombre = nombre, nivel = nivel, salud = salud, color = color)
        self.__voltaje_max = voltaje_max
        self.__amperaje_max = amperaje_max

    # Getters tradicionales
    
    def get_salud(self):
        return self.__salud
        
    def get_nivel(self):
        return self.__nivel
        
    def get_voltaje_max(self):
        return self.__voltaje_max
        
    def get_amperaje_max(self):
        return self.__amperaje_max
        
    def get_tipo(self):
        return self.__tipo

    # Setters tradicionales
    def set_salud(self, salud):
        if salud > 0 and salud <= 500:
            self.__salud = salud
        else:
            print("La salud no puede ser negativa o mayor a 500")
            
    def set_nivel(self, nivel):
        if nivel > 0:
            self.__nivel = nivel
        else:
            print("El nivel no puede ser negativo")
            
    def set_voltaje_max(self, voltaje):
        if voltaje > 0:
            self.__voltaje_max = voltaje
        else:
            print("El voltaje máximo no puede ser negativo")
            
    def set_amperaje_max(self, amperaje):
        if amperaje > 0:
            self.__amperaje_max = amperaje
        else:
            print("El amperaje máximo no puede ser negativo")

    def atacar(self):           
        print(f"Pikachu ataca y genera {self.__nivel/4} de daño")


pikachu_1 = Pikachu("morty", 5, 100, 220, 12, "Amarillo")

pikachu_1.set_salud(200)  # Usando el setter tradicional

print(f"La salud actual de {pikachu_1.nombre} es: {pikachu_1.get_salud()}")
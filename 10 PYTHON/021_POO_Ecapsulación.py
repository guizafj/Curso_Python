


# POO

# CREACIÓN DE UNA CLASE
""" 
    Los atributos siempre se declaran privados, por seguridad y funcionalidad, por norma general cada atributo debe tener un getter y un setter 
    los metodos y funciones publicas
    con getter 
"""



class Coche():
# Método constructor
    def __init__(self,):
        self.__largo = 250
        self.__ancho = 120
        self.__ruedas = 4
        self.__peso = 900
        self.__color = "rojo"
        self.__is_enMarcha = False

# Declaración de métodos
    def arrancar(self):             # self hace referencia a la instancia de clase.
        self.__is_enMarcha = True     # Es como si pusiésemos miCoche.is_enMarcha = True

    def estado(self):
        if self.__is_enMarcha:
            return "El coche está arrancado"
        else:
            return "El coche está parado"    
 
    
    def color(self):
        return self.__color

    @property
    def cambiar_color(self, color_nuevo):        
        self.__color = color_nuevo
        print("se ha cambiado el color!")
        
                
    def ver_peso(self):
        print(f"El peso del coche es: {self.__peso}")

    def ver_largo(self):
        print(f"El largo del coche es: {self.__largo}")

    def ver_ancho(self):
        print(f"El ancho del coche es: {self.__ancho}")


# Declaración de una instancia de clase, objeto de clase o ejemplar de clase.
miCoche = Coche()

miCoche.ver_ancho()
miCoche.cambiar_color
miCoche.ver_largo()
miCoche.ver_peso()
miCoche.cambiar_color = input("Indica el color deseado: ")
miCoche.cambiar_color

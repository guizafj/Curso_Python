


# POO

# CREACIÓN DE UNA CLASE


class Coche:
# Declaración de atributos
    def __init__(self): # Por buenas practicas es recomendado hacer uso del constructor
        self.largo = 250
        self.ancho = 120
        self.ruedas = 4
        self.peso = 900
        self.color = "rojo"
        self.is_enMarcha = False

# Declaración de métodos
    def arrancar(self):             # self hace referencia a la instancia de clase. / en otros lenguajes de programacion se conoce como this
        self.is_enMarcha = True     # Es como si pusiésemos miCoche.is_enMarcha = True

    def estado(self):
        if self.is_enMarcha:
            return "El coche está arrancado"
        else:
            return "El coche está parado"    

    def cambiar_color(self):
        if self.color:
            nuevo_color = input("Ingresa el color deseado: ")
            self.color = nuevo_color
            print("se ha cambiado el color")
            return
            

# Declaración de una instancia de clase, objeto de clase o ejemplar de clase.
miCoche = Coche()
miCoche2 = Coche()

# Acceso a un atributo de la clase Coche. Nomenclatura del punto.
print("El largo del coche es de" , miCoche.largo, "cm.")
miCoche.arrancar()
print(miCoche.estado())
print(miCoche.color) # Cuanndo se accede a un atributo se diferencia porque no lleva () en el llamado
miCoche2.cambiar_color()
print(f"El color del coche 2 es: {miCoche2.color}") 

# Acceso a un método de la clase Coche. Nomenclatura del punto.
print("El coche está arrancado:" , miCoche.arrancar()) 
print(f"El coche 1: {miCoche.estado()}")
print(f"El coche 2: {miCoche2.estado()}")

#Modificamos el valor de una propiedad
miCoche2.ruedas = 10
print("El coche2 tiene:" , miCoche2.ruedas, "ruedas.")
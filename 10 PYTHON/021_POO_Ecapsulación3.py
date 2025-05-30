# POO

# CREACIÓN DE UNA CLASE
""" 
    Los atributos siempre se declaran privados, por seguridad y funcionalidad, por norma general cada atributo debe tener un getter y un setter 
    los metodos y funciones publicas
"""

""" 
    Un decorador es una función que se le añade a otra función, se crea una función inicial dentro de la clase
    y luego se le realiza la llamada  
"""

class Persona:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self.apellido = apellido
        self.edad = edad

    @property # Metodo getter
    def nombre(self):
        print('Llamando método get nombre')
        return self._nombre

    @nombre.setter # Metodo setter
    def nombre(self, nombre):
        print('Llamando método set nombre')
        self._nombre = nombre

    def mostrar_detalle(self):
        print(f'Persona: {self._nombre} {self.apellido} {self.edad}')

    #Sin decoradores

    #def mostrar_detalle(self):
    #    print(f'Persona: {self.nombre()} {self.apellido} {self.edad}')


persona1 = Persona('Juan', 'Perez', 28)
persona1.nombre = 'Juan Carlos'
print(persona1.nombre)
# persona1._nombre = 'Cambio'
# print(persona1._nombre)

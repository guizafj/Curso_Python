class Persona:
    def __init__(self, nombre, apellido, edad):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__edad = edad

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def apellido(self):
        return self.__apellido

    @apellido.setter
    def apellido(self, apellido):
        self.__apellido = apellido

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, edad):
        self.__edad = edad

    def mostrar_detalle(self):
        print(f'Persona: {self.__nombre} {self.__apellido} {self.__edad}')


persona1 = Persona('Juan', 'Perez', 28)
persona1.nombre = 'Juan Carlos'
persona1.apellido = 'Lara'
persona1.edad = 30
persona1.mostrar_detalle()

# persona1._nombre = 'Cambio'
# print(persona1._nombre)

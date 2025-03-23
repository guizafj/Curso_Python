# POO

# CREACIÓN DE UNA CLASE
class Usuario:
    # Declaración de atributos
    nombre = "Angel"
    __edad = 47 # Se realiza encapsulación de la variable y se deja de forma privada, no es posible modificarla sin hacer uso del metodo setter
    login = "admin"
    password = "1234"
    email = "angel@loquesea.com"
    telefono = 666666666

    # Declaración de métodos
    def resumen(self):  # self hace referencia a la instancia de clase.
        print(f'Los datos del usuario son:\n'
              f'Nombre: {self.nombre}\n'
              f'Edad: {self.__edad}\n'
              f'Login: {self.login}\n'
              f'Password: {self.password}\n'
              f'Email: {self.email}\n'
              f'Teléfono: {self.telefono}')

    
    def cambiar_Edad(self):
        edadIntroducida = int(input("Introduce edad entre 18-100:"))

        if 18 < edadIntroducida < 100:
        #if edadIntroducida < 18 and edadIntroducida > 100:
            self.__edad = edadIntroducida
            print("Edad introducida correcta")
            return 
        else:
            print("La edad introducida no es correcta.")
            self.cambiar_Edad() # Uso de recursividad
            return ""

    def muestraEdad(self):
        print('La edad del usuario es:', self.__edad, 'años.')
        


administrador = Usuario()

administrador.resumen()

print(administrador.cambiar_Edad())
print(administrador.muestraEdad())
print(administrador.__edad) #error

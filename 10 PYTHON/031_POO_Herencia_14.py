class Usuario():
    def __init__(self):
        self.nombre = input("ingresa tu nombre: ")
        self.edad = int(input("ingresa tu edad: "))
        self.login = input("Ingresa tu usuario: ")
        self.passsword = input("Elige tu contraseña: ")
        self.email = input("Facilita tu email: ")
        self.telefono = int(input("Ingresa tu telefono: "))

    def __del__(self):
        print("Acabas de eliminar un usuario")

    def resumen(self):
        print(f"\nlos datos del usuario son:\n Nombre: {self.nombre}\n Edad: {self.edad}\n Login: {self.login}\n Password: {self.passsword}\n Email: {self.email}\n Telefono: {self.telefono}")    

    def cambiar_edad(self):
        edad_introducida = int(input("introduce tu edad: "))
        if 18 < edad_introducida < 100: 
            self.edad = edad_introducida
            print("Edad introducidad correcta")
            return ""
        else:
            print("La edad introducida no es correcta")
            self.cambiar_edad
            return ""

    def muestra_edad(self):
        print(f"La edad del usuario es: {self.edad} años")
        return     ""
    

administrador = Usuario()
administrador.resumen()

administrador.cambiar_edad()
administrador.muestra_edad()

del administrador
      



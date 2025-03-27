#Creacion de uan estructura para los clientes:

class Cliente:
    
    def __init__(self, dni, nombre, apellidos):
        self.dni = dni
        self.nombre = nombre
        self.apellidos = apellidos

    def __str__(self):
        return(f"{self.nombre} {self.apellidos}")

# creacion de la estructura para las empresas

class Empresa:
    def __init__(self, clientes=[]):
        self.clientes = clientes

    def mostrar_clientes(self, dni = None):
        for c in self.clientes:
            if c.dni == dni:
                print(c)
                return
        print("Cliente no encontrado")        

    def borrar_cliente(self, dni = None):
        for i,c in enumerate(self.clientes):
            if c.dni == dni:
                del(self.clientes[i])
                print(str(c), "> Borrado")
        print("Cliente no encontrado") 

# Utilización de las estructuras
# creacion de clientes

hector = Cliente(dni = "11111111A", nombre = "hector", apellidos ="Costa Guzman")
juan = Cliente(dni = "22222222B", nombre = "juan", apellidos = "Gonzalez Marquez")

# creacion de objetos con la clase empresa
empresa = Empresa(clientes=[hector, juan])

# Mostrar los clientes en un listado
print("==LISTADO DE CLIENTES==")
print(str(empresa.clientes))

print("\n==MOSTRAR CLIENTES POR DNI==")
# Consulto clientes por DNI
empresa.mostrar_clientes("11111111A")
empresa.mostrar_clientes("11111111Z")

print("\n==BORRAR CLIENTES POR DNI==")
# Borro un cliente por DNI
empresa.borrar_cliente("22222222V")
empresa.borrar_cliente("22222222B")


# Muestro de nuevo todos los clientes
print("\n==LISTADO DE CLIENTES==")
print(empresa.clientes)



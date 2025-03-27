# Se definen unos cuantos clientes
clientes = [
    {'Nombre': 'Hector',
     'Apellidos': 'Costa Guzman',
     'dni' : '11111111A'
    },
    {'Nombre' : 'Juan',
     'Apellidos' : 'González Márquez',
     'dni' : '22222222B'
    }
]

# Se crea una función que muestra un cliente en una lista apartir del DNI

def mostrar_cliente(clientes, dni):
    for c in clientes:
        if (dni == c ['dni']):
            print(f"{c}\n")
            return
    
    print('Cliente no encontrado')
          

# Se crea una función que borra un cliente en una lista apartir del DNI

def borrar_cliente(clientes, dni):
    for i,c in enumerate(clientes):  
        if (dni == c ['dni']):
            del(clientes[i])
            print(str(c), "> Borrado")
            return 
        
    print("Cliente no encontrado")

# Utilización del codigo estructurado

print("----Listado de clientes----")
print(clientes)

print("\n---Ver clientes por DNI---")
mostrar_cliente(clientes, '11111111A')
mostrar_cliente(clientes, '22222222B')

print("\n-----Borrar clientes por DNI----")
borrar_cliente(clientes, '22222222V')
borrar_cliente(clientes, '22222222B')

print("\n-----Listado de clientes----")
print(clientes)
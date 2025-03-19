""" programa que pide al usuario su documento para verificar su edad
    en caso de que no se encuentre  en el diccionario pide la edad para agregrar su 
    información
"""
# importacion de librerias
import pickle
from  pathlib import Path

docu = {} # creacion de un diccionario vacio
# la información contenida en las "" es la posicion dentro del diccionario y lo que viene despues es su valor

def abrir_archivo():
    global docu # declarar docu como variable global
    file_name = input("introduce el nombre del archivo: ")# se solicita nombre de archivo 

    path = Path(file_name) #comprobacion de archivo existente

    if path.is_file(): #Abre el archivo en modo lectura 
        input_file = open(file_name, 'rb') # se crea una variable asignandole el archivo
        docu = pickle.load(input_file)
        input_file.close() # se cierra el archivo
    else:
        print("archivo no encontrado, crearemos un diccionario vacio")    

abrir_archivo()
print(docu)

document_number = input("introduce tu documento de identidad: ")

if document_number in docu: #comprueba que el dato introducido este en el diccionario
    print(f"\n la edad de {document_number} es: {docu[document_number]}")

else: 
    edad = input("Documento no encontrado, introduce tu edad: ")    
    if edad.isnumeric(): # se verifica que sea un numero valido (solo aplica para positivos)
        num = int(edad)
        docu[document_number] = num # se añade al diccionario los valores introducidos por el usuario
        print("añadido al diccionario")
    else:
        print("edad no valida")

print("\n", docu)   

guardar = input("deseas guardar el diccionario:") 

if guardar == "si": #Metodo usado para guardar un archivo tipo diccionario
    output = open('midic.pkl', 'wb') # Abre un archivo en modo escritura binaria ('wb')
    pickle.dump(docu, output) # Guarda el objeto 'docu' en el archivo usando pickle
    output.close() # Cierra el archivo
    print("diccionario guardado con exito")
else: 
    document_number = input("introduce tu documento de identidad: ")

# Ingreso de datos por consola para asginarlos a un diccionario

nombre_usu = input("Introduce tu nombre: ")
apellido_usu = input("introduce tu apellido: ")
pais_usu = input("Cual es tu pais: ")
ciudad_usu = input("Ingresa tu ciudad: ")

# Creación de un diccionario
dic_01 = {
    "Nombre": nombre_usu,
    "Apellido": apellido_usu,
    "Pais":pais_usu,
    "Ciudad": ciudad_usu
}
print(dic_01)

# Otra forma de definir diccionarios con la funcion dict()
dic_02 = dict(
    Nombre="Santiago",
    Apellido="Hernandez",
    Pais="España",
    Ciudad="Madrid"
)
print(dic_02)

dic_03 = dic_02.copy()
print(dic_03)

dic_03.clear()
print(f"Este diccionario esta vacio: {dic_03}")

# Los metodos que se usan en el diccionario estan especificados en el archivo de estuctura de datos

# Devuelve un diccionario con las claves y valores especificados
print(f"muestra los apellidos: {dic_01.fromkeys("Apellido")}")

# Devuelve el valor de una clave
print(f"muestra el nombre contenido en el diccionario: {dic_01.get("Nombre")}")

# Devuelve una lista que contiene una tupla por cada par clave-valor
print(f"mostrar el diccionario como tupla: {dic_01.items()}")

# Devuelve una lista que contiene las claves del diccionario
print(f"Muestra una lista que contiene el diccionario: {dic_01.keys()}")

# Borra el elemento con la clave especificada
dic_01.pop("Apellido")
print(dic_01)

# Borra el último par clave-valor insertado
dic_02.popitem()
print(dic_02)

# Devuelve el valor de la clave especificada. Si no existe, inserta la clave con el valor especificado.
print(f"muestra el valor de nombre: {dic_02.setdefault("Apellido")}")

# Actualiza el diccionario con el par clave-valor que se especifique
dic_01.update(Apellido = "Diaz")

# Devuelve una lista con los valores del diccionario
print(f"Muestra el diccionario: {dic_01.values()}")
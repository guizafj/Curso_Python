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
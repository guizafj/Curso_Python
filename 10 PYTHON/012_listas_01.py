from pathlib import Path
import pickle

lista_1 = list() # creacion de lista vacia

def abrir_archivo():# abrir archivo
    global lista_1 # declarar lista_1 como variable global
    file_name = input("introduce el nombre del archivo: ")# se solicita nombre de archivo 

#comprobacion de archivo existente
    path = Path(file_name)

    if path.is_file(): #Abre el archivo en modo lectura 
        input_file = open(file_name, 'rb') # se crea una variable asignandole el archivo
        lista_1 = pickle.load(input_file)
        input_file.close() # se cierra el archivo
    else:
        print("archivo no encontrado, crearemos una lista vacia")    

abrir_archivo()
print(lista_1)

def crear_lista():
    while True:
        n_usuario = input("Ingresa un valor (o escribe 'salir' para terminar): ")  

        if n_usuario.lower() == "salir":  # Convertimos a minúsculas para evitar errores
            break  # Sale del bucle si el usuario escribe 'salir'
    
        if n_usuario.isnumeric(): # comprobacion del numero
            num = int(n_usuario)
            lista_1.append(num) # se agrega a la lista despues de comprobarlo
            print(f"numero {num} agregado exitosamente")
           
        else:
            print("has ingresado un valor no mumerico") # en caso de que no sea un número
            

crear_lista() # Llamamos a la función antes de guardar
print(lista_1)

def guardar():
    guardar = input("deseas guardar la lista: (si) o (no)").lower() 

    if guardar == "si": #Metodo usado para guardar un archivo tipo lista
        output = open('mi_lista.pkl', 'wb') # Abre un archivo en modo escritura binaria ('wb')
        pickle.dump(lista_1, output) # Guarda el objeto 'lista_1' en el archivo usando pickle
        output.close() # Cierra el archivo
        print("lista guardado con exito")
guardar()
"""
if guardar == "si":
    with open('mi_lista.pkl', 'wb') as output:  # Usamos "with open" para manejar archivos mejor
        pickle.dump(lista_1, output)
    print("Lista guardada con éxito.")
✔ Se usa with open(...) para manejar el archivo de manera más segura y evitar olvidar cerrarlo.
"""    



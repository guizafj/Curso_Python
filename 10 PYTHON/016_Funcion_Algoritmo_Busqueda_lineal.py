
import pickle
# Busqueda lineal

def buscar(lista, nombre_buscado):
    tamano_lista = len(lista)
    for actual in range(0, tamano_lista):
        if(lista[actual] == nombre_buscado):
            return actual
        return -1

def main():
     # Cargar la lista desde el archivo .pkl
    with open('mi_lista.pkl', 'rb') as archivo:
        importa_lista = pickle.load(archivo)
    
    lista_de_alumnos = sorted(importa_lista)    
    posicion_del_alumno = buscar(lista_de_alumnos, "12") 

    if posicion_del_alumno != -1:
        print(f"Alumno(a) {lista_de_alumnos} está en la  posicion {posicion_del_alumno}")  
    else: 
        print("Alumno no encontrado")        

if __name__ == "__main__":
    main()

# Se inserta un archivo importado

def importar_lista(archivo):
    lista = []
    with open(archivo) as tf:
        lines = tf.read().split('","')
        for line in lines:
            lista.append(line)
        return lista
    
def buscar_1(lista, nombre_buscado):
    tamano_de_lista = len(lista)
    for actual in range(0,tamano_de_lista):
        if (lista[actual] == nombre_buscado):
            return actual
    return -1

def main():
    lista_de_alumnos = sorted(importa_lista('../data/lista_aluno s'))
    posicion_del_alumno = buscar(lista_de_alumnos, "Wanessa")
    print("Alumno(a) {} está en la posicion {}".format(lista_de_alumnos[posicion_del_alumno], posicion_del_alumno))

if __name__ == "__main__":
    main()


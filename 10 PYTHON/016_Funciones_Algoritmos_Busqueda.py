from array import array
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


def importar_lista(archivo):
    lista = []
    with open(archivo) as tf:
        lines = tf.read().split('","')
        for line in lines:
            lista.append(line)
        return lista
    
def buscar(lista, nombre_buscado):
    tamano_de_lista = len(lista)
    for actual in range(0,tamano_de_lista):
        if (lista[actual] == nombre_buscado):
            return actual
    return -1

def main():
    lista_de_alumnos = sorted(importa_lista('../data/lista_aluno s'))
    posicion_del_alumno = busca(lista_de_alumnos, "Wanessa")
    print("Alumno(a) {} está en la posicion {}".format(lista_de_alumnos[posicion_del_alumno], posicion_del_alumno))

if __name__ == "__main__":
    main()

# Busqueda binaria: / siempre es mejor hacer uso de la busqueda binaria, evitar el uso de busqueda lineal por optmización en el tiempo de ejecución 
""" 
    Importante recalcar que para la solución de búsqueda binaria es necesario tener la lista
    ordenada, por lo que usamos la función sorted() para ordenarla.
"""

def importar_lista(archivo):
    lista = []
    with open(arquivo) as tf:
        lines = tf.read().split('","')
    for line in lines:
            lista.append(line)
    return lista

def buscar(lista, nombre_buscado):
    tamano_de_lista = len(lista) # haciendo uso de la función sorted se organiza la lista en orden alfabetico
    inicio = 0
    fin=tamano_de_lista-1
    while inicio <= fin:
          medio=(inicio + fin)//2
    if lista[medio] == nombre_buscado:
            return medio
    elif lista[medio] < nombre_buscado:
            inicio=medio+1
    elif lista[medio] > nombre_buscado:
            fin = medio-1
    return -1
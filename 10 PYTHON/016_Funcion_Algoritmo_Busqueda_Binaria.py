# Busqueda binaria: / siempre es mejor hacer uso de la busqueda binaria, evitar el uso de busqueda lineal por optmización en el tiempo de ejecución 
""" 
    Importante recalcar que para la solución de búsqueda binaria es necesario tener la lista
    ordenada, por lo que usamos la función sorted() para ordenarla.
"""

def importar_lista(archivo):
    lista = []
    with open(archivo) as tf:
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
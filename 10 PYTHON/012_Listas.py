# la información sobre los metodos de las listas se encuenta en el documento del tema 6 parte 3 = Estructura de datos

#   LISTAS

"""
La lista es un tipo de colección ordenada y modificable. 
Es decir, una secuencia de valores de cualquier tipo, ordenados y de tamaño variable.
Se escriben entre corchetes [].
"""

miLista=["Angel", 43, 667767250] 
mi_Lista02 = [22, True, "una lista", [1, 2]]

#   MÉTODOS DE LAS LISTAS

#   Hacer una lista de una cadena
miLista = list("PYTHON")
print(miLista)

#   Acceder a los elementos de una lista
""" 
  Podemos acceder a cada uno de los elementos de la lista escribiendo el nombre de la lista e indicando el
  índice del elemento entre corchetes.
"""
miLista = [22, True, "una cadena", [1, 2]]
print(miLista[0])

# Aceder a una lista dentro de otra lista
""" 
  [][] primero para indicar a qué posición de la lista exterior queremos acceder, y el
  segundo para seleccionar el elemento de la lista interior
"""
miLista = [[1,2] , [3,4] , [5,6]]
miVar = miLista[1][1]
print(miVar) # tiene un valor de 4

# Modificación de valores dento de una lista
mi_lista = [22, True]
mi_lista [0] = 99
print(mi_lista[0])
print(f"la lista nueva es: {mi_lista[:]}") # [:] con esta expresión se imprime toda la lista


# Operaciones con listas
 
print(miLista == mi_lista) # False

print(mi_lista in miLista)  # False

print(mi_lista == [[1,2] , [3,4] , [5,6]]) # Salida True

print(mi_lista is [[1,2] , [3,4] , [5,6]]) # False / se recomienda el uso de operadores para hacer comparaciones 

#   Función con una lista como parámetro

def miFunccion(listaFrutas):
      for x in listaFrutas:
        print(x)

frutas = ["Manzana", "banana", "cereza"]

miFunccion(frutas)

la = [1, 2, 3, 4, 5]
lb = list('abcde')
lc = list('ABCDE')

zlist = list(zip(la, lb, lc)) # soporta cualquier número # zip # de argumentos posicionales zlist
a, b, c = zip(*zlist) # El * en zip desempaqueta lista de tuplas
print(la, lb, lc, sep = '\n') # Seperador por defecto es espacio
print(la, lb) 

# incluir una función en una lista

lista_funcion = [0, 2, miFunccion,"fran"]
print(lista_funcion[2])
 

mi_Lista01 = ["Angel", "Maria", "Manolo", "Antonio", "Pepe"]
mi_Lista02 = ["Maria", 2, 5.56, True] # Se puede mezclar diferentes elementos

print (mi_Lista01[1]) # Para un elemento en concreto, se empieza a contar desde la posición cero.
print (mi_Lista02[0:2]) # Empezando desde cero incluido hasta el dos sin incluir, esto es, “Angel y María”.

mi_Lista01.append("javier") # Agrega un elemento a la final de la lista
print(mi_Lista01[:])

mi_Lista02.clear() # borra los elementos de la lista
print(mi_Lista02[:])

mi_Lista02 = mi_Lista01.copy() # copia una lista de la otra
print(mi_Lista01[:])
print(mi_Lista02[:])

print(mi_Lista01.count("javier")) # retorna la cantidad de veces que se encuentra un elemento

mi_Lista02.extend(mi_Lista01) # Añade los elementos de una lista a otra.
print(mi_Lista02[:])

print(mi_Lista02.index("javier")) # Devuelve el índice del primer elemento cuyo valor es el especificado.

mi_Lista01.insert(2, "edelmira") # Añade un elemento en la posición especificada.
print(mi_Lista01[:])

print(mi_Lista01.pop(4)) # Borra el elemento en la posición especificada y devuelve el elemento eliminado.

mi_Lista01.remove("Pepe") # Elimina el elemento con el valor especificado
print(mi_Lista01)

mi_Lista01.sort(reverse=True)
print(mi_Lista01)
mi_Lista01.sort()
print("🎕",mi_Lista01)


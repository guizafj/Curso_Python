# recorrer un diccionario con u bucle for

keys = ['nombre', 'apellido', 'edad']
values = ['fran', 'guiza', '34']

base = dict(zip(keys, values)) # creacion de un diccionario
"""En cada iteración del ejemplo le estamos pasando la clave (k) del diccionario y el valor del diccionario correspondiente a esa clave (d[k])
"""
for k in base: # se declara la variable k para recorrer el diccionario
    info = '{}: {}'.format(k, base[k]) # dentro del for se inicializa una nueva variable que recorre el diccionario # Texto formateado con claves y valores
    print(info)


# Asignacion en tuplas 

l_a, l_b = (3, 4) # asignacion de valores dentro de una tupla

l_t = [(1,2), (3,4), (5,6)] # declaracion de una lista de tuplas

for x, y in l_t: # for para recorrer la lista de tuplas asignando los valores contenidos a dos variables (desempaquetado en tuplas)
    print(x + y, end= ' '"\n")

# navegar en un diccionarios con el desempaquetado de tuplas
for k, v in base.items(): # devuelve la tupla con clave valor, en cada iteración del for
    print(f"{k}: {v}")

for k in base.keys(): # Recorre el diccionario, pero solo busca dentro de la lista keys
    print(k, end = ' ')

for v in base.values(): # Recorre el diccionario pero solo va a la lista de valores
    print(v, end = ' ')


# Obtener claves
claves = base.keys() # dict_keys(['nombre', 'apellido', 'edad'])
print(claves, "\n") 

# Obtener valores
valores = base.values()# dict_values(['Guido', 'van Rossum', 60])
print(valores, "\n")  

# Obtener items (pares clave-valor)
pares = base.items() # dict_items([('nombre', 'Guido'), ('apellido', 'van Rossum'), ('edad', 60)])
print(pares, "\n")  

# Si necesitas convertirlos a listas
lista_claves = list(claves)
lista_valores = list(valores)
lista_pares = list(pares)

print(lista_claves, "\n")  # ['nombre', 'apellido', 'edad']
print(lista_valores, "\n")  # ['Guido', 'van Rossum', 60]
print(lista_pares, "\n")  # [('nombre', 'Guido'), ('apellido', 'van Rossum'), ('edad', 60)]

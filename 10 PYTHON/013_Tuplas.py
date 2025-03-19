


#   TUPLAS

"""Una tupla es una colección ordenada e inmutable. 
En Python, las tuplas se escriben entre paréntesis.
"""

#       Declaración de una tupla

miTupla = ("manzana", "banana", "cereza")
print(miTupla[1])

#   Otra forma de declararla

miTupla = tuple(("manzana", "banana", "cereza"))
print(miTupla)


#   Indexación Negativa

miTupla = ("manzana", "banana", "cereza")
print(miTupla[-1])

#   Rango de índices
#   Devuelve el tercer, cuarto y quinto elemento:

miTupla = ("manzana", "banana", "cereza", "naranja", "kiwi", "melon", "mango")
print(miTupla[2:5])

#   Convierta la tupla en una lista para poder cambiarla:

miTupla = ("manzana", "banana", "cereza")
miLista = list(miTupla)
miLista[1] = "kiwi"
miTupla = tuple(miLista)

print(miTupla)

#   Recorrer una tupla

miTupla = ("manzana", "banana", "cereza")
for x in miTupla:
  print(x)

#   Comprobar si existe un elemento
#   Compruebe si "manzana" está presente en la tupla:

miTupla = ("manzana", "banana", "cereza")
if "manzana" in miTupla:
  print("Sí, 'manzana' está en la tupla.")

#   Otra forma, simplemente con un boolean

print("manzana" in miTupla) 

#   Longitud de la tupla

miTupla = ("manzana", "banana", "cereza")
print(len(miTupla))


# Unir dos tuplas

tupla1 = ("a", "b" , "c")
tupla2 = (1, 2, 3)

tupla3 = tupla1 + tupla2
print(tupla3)

#   Cuantas veces se encuentra el elemento 4 en miTupla?

miTupla = ("manzana", "banana", "cereza" , "manzana")
print(miTupla.count("manzana"))	

#   Desempaquetdo de tupla

miTupla=("Angel", 4, 5.345, True, 4)
nombre, num1, num2, valor1, num3=miTupla

print(nombre)
print(num1)
print(num2)
print(valor1)
print(num3)


this_tuple = ("platano", "pera", "manzana", "fresa", "cherry", "orange", "kiwi", "melon", "mango")
print(f"Aqui muestro el elemento en la posicion 1: {this_tuple[1]}")

print(f"En esta linea se puede ver el ultimo elemento: {this_tuple[-1]}")
print(f"En esta linea se puede ver el pen-ultimo elemento: {this_tuple[-2]}")

print(f"Aqui se muestra un rango en la tupla: {this_tuple[2:5]}") # Al especificar un rango, el valor de retorno será una nueva tupla con los elementos especificados.
print(f"Rango con indices negativos: {this_tuple[-4:-1]}")

# Modificando datos en una tupla, se debe convertir en una lista y luego convertir la lista en tupla / Directamente no se pueden modificar u agregar elementos

tupla_x = ("apple", "banana", "cherry") # Declaración de una tupla
print(f"tupla sin modificación: {tupla_x}")
lista_y = list(tupla_x) # se convierte la tupla en una lista
lista_y[1] = "Kiwi" # a la lista se le modifica los datos deseados
tupla_x = tuple(lista_y) # se convierte la lista en una tupla
print(f"Tupla modificada: {tupla_x}") 

# Recorrer una tupla

print("se recorre una tupla: ")
for x in this_tuple:  # Puedes recorrer los elementos de la tupla utilizando un bucle for.
  print(x)

# comprobar si existe el articulo en una tupla

if "platano" in this_tuple:
  print("si 'platano' esta declarado en esta tupla")
else:
  print("platano no encontrado")

# longitud de una tupla
print(f"Aqui se mide la longitud de la tupla: {len(this_tuple)}")

# #Tupla unitaria. Hay que poner al final ","
tupla_01 = ("manzana",)
print(type(tupla_01)) # se verifica el tipo de dato contenido

""" 
  Las tuplas no se pueden cambiar, por lo que no puedes eliminar elementos de él, pero puedes
  eliminarlas por completo haciendo uso de la expresión del 
"""
del tupla_01

# unir dos tuplas

tupla_02 = ("a", "b", "c")
tupla_03 = (1, 2, 3)

tupla_04 = tupla_02 + tupla_03
print(f"Muestra el resultado de unir dos tuplas: {tupla_04}")

# Uso del contructor tuple()

this_tuple_1 = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(this_tuple_1)

# empaquetado de tupla, no se recomienda, es posible definir una tupla sin el uso de paréntesis
miTupla = "Angel", 4, 5.345, True, 4

#Desempaquetado de tupla. Permite asignar todos los elementos de una tupla a diferentes variables:
miTupla = ("Angel", 4, 5.345, True, 4)
nombre, num1, num2, valor1, num3 = miTupla

print(nombre)
print(num1)
print(num2)
print(valor1)
print(num3)
import random 

# Escribe un script que cuente desde 1 hasta un número n proporcionado por 
# el usuario, imprimiendo cada número.
letras = list('abcdefghijklmnopqrstuvwyz')

l_1 = letras[:8] # Creacion de sublistas 
l_2 = letras[8:16]
l_3 = letras[16:]

random.shuffle(l_1) # se mezclan las franjas de las listas de manera aleatoria
random.shuffle(l_2)
random.shuffle(l_3)

"""
  Haciendo uso de zip aprovechamos la ventaja que presenta este metodo ya que es mas legible 
  evita la preocupación de que todas las listas tengan la misma longitud
      """

for a, b, c in zip(l_1, l_2, l_3): # se recorren las 3 sublistas que han sido mezcladas, el recorrido se realiza de manera simultanea
    print(a + b + c, end=' ') # se muestra en pantalla una letra de cada lista en cada iteración 

print(" ")

n = int(input("Introduce un número hasta el que contar: "))
contador = 1
while True:
    if contador == n:       
       break   
    print(contador)
    contador += 1
print(n)
  

letras = list('iabcdiefghijklimnopqrst') # se crea una lista con una cantidad de letras
vocales = 'aeiou' # declaracion e incialicion de una variable con las vocales

random.shuffle(letras) # uso del random para mezclar la lista
print(' '.join(letras)) # se imprime la lista mezclada, agragando un espacio entre cada caracter

"""
En este ejemplo buscamos las posiciones de las vocales en un abecedario desordenado. Para ello
usamos la función enumerate, que nos pide una secuencia y nos devuelve la misma secuencia
asociada a sus índices:
    """

for i, letra in enumerate(letras): # dentro del for se hace uso de 2 variables para recorrer la lista, ademas de usar el metodo enumerate
    if letra in vocales: # la variable letra recorre las vocales
        print(f"{letra} en la posición {i}") # al imprimir la variable i se usa para numerar la posicion

abcde = sorted(letras[:5]) # el enumerate se puede usar envuelto en un list() o recorrerlo con un for
list(enumerate(abcde)) # de esta forma devuelve una secuencia con sus indices
list(enumerate(abcde, 10)) # es posible indicarle en que indice empieza


from random import shuffle

# 1. Dados dos números, escriba un código Python para encontrar el mínimo de estos dos números

n_a = 4
n_b = 7

def minimun(n_a, n_b): 
    if n_a < n_b:
        return n_a 
    else:
        return n_b
    
print(minimun(n_a, n_b))

# 2. Invertir palabras de una cadena dada.

def rev_sentence(sentence):
    words = sentence.split(' ') # : convierte la frase en una lista de palabras.
    rev_sentence = ' '.join(reversed(words)) #  revierte el orden de la lista. / join --> une las palabras de nuevo separadas por espacios.
    return rev_sentence

if __name__ == "__main__":
    sentencia = "Codigo de practica de prueba de geeks"
    print(sentencia)
    print(rev_sentence(sentencia))
    
# 3. Realizar una suma de los elementos de una tupla

test_tup = (7, 8, 9 ,10 ,7, 8)
print("La tupla origina es:", str(test_tup))

res = sum(list(test_tup)) # usando la función predefinida sum y convirtiendo la tupla en una lista es posible sumarla y asignar ese valor a una variable
print("El resultado de la suma de la tupla es:",  str(res)) # se imprime el resultado usando el metodo str

# 4. Escriba un código que calcule una lista de números proporcionados.

def sum_list(num_list):
    if len(num_list) == 1:  # CASO BASE
        return num_list[0] #  # Si la lista tiene solo un elemento, devuelve ese elemento
    else:
        # Caso recursivo: suma el primer número + la suma del resto de la lista
        return num_list[0] + sum_list(num_list[1:])

print(sum_list([3,5,6,7,9]))

# 5. Escriba un código que desordene al azar una lista. / en este ejm hace falta importar el modulo shuffle de la clase random 

l_x = ['Skyrin', 'pertenece', 'a', 'los', 'Nórdicos']
print(l_x)
shuffle(l_x)
print(l_x)

# 6. Escriba un código que pueda contar todas las palabras mayúsculas de un archivo.
archivo = "short.zen.txt"
# Aquí abres un archivo que debe estar en la variable archivo
#  (deberías haber definido archivo = "archivo.txt" antes o pasar el nombre del archivo).
with open(archivo) as fh:  #  se encarga de abrir y cerrar automáticamente el archivo. / 
    # fh es el "file handle" o la variable que representa el archivo abierto.
    count = 0 # Inicializas una variable count que va a contar la cantidad de letras mayúsculas encontradas.
    text = fh.read()     # Lee todo el contenido del archivo como un string completo y lo almacena en text.

for character in text: # Aquí se recorre carácter por carácter todo el texto del archivo.
    if character.isupper(): # Verifica si el carácter es una letra mayúscula (A-Z).
        count += 1 # Si es mayúscula, incrementas el contador en 1.

print(f"El número de letras con mayúsculas en el archivo es: {count}")
print(archivo)

# 7. ¿Si la lista 1 es [4, 6, 8, 1, 0, 3], que sería la lista 1 [-1]?

li_7 = [4, 6, 8, 1, 0, 3]

print(li_7[-1])

# 8. Escriba un programa para producir la serie Fibonacci en Python.

n_fi =int(input("intruduce el valor de 'n': "))
first = 0
second = 1
sum = 0
count = 0
print("secuencia de fibonacci: ")

while(count <= n_fi): # Bucle que se ejecuta hasta que count llegue a n_fi
    print(sum) # Imprime el número actual en la secuencia
    count += 1  # Incrementa el contador
    first = second # Mueve el valor de 'second' a 'first'
    second = sum # Mueve el valor de 'sum' a 'second'
    sum = first + second # Calcula el siguiente número de la secuencia

# Version en la que se incluye un condicional y se deja mas legible el codigo

n_fi = int(input("Introduce el valor de 'n': "))

first = 0
second = 1
count = 0

print("Secuencia de Fibonacci:")

if n_fi <= 0:
    print("Por favor, introduce un número positivo.")
elif n_fi == 1:
    print(first)
else:
    while count < n_fi:
        print(first)
        next_term = first + second
        first = second
        second = next_term
        count += 1

# 9. Escriba un programa en Python para comprobar si un número es primo.

def isprimo(n_nump):
    if n_nump <= 1:
        return False
    elif n_nump == 2:
        return True
    else:
        for i in range(2, int(n_nump ** 0.5) + 1): # se  itera hasta la raíz cuadrada de n_nump. 
            if n_nump % i == 0:
                return False
        return True
    
def app():
    n_user = int(input("escribe un número: "))    

    if isprimo(n_user):
        print("El numero es primo!!")
    else:
        print('El numero no es primo!!')

if __name__ == '__main__':
    app()
    
# 10. Escribir un programa en Python para comprobar si un número es capicúa.
#  Es decir, si se lee igual de derecha a izquierda que de izquierda a derecha.

n_ca = input("introduce un número: ")
n_cb = n_ca[::-1] # es una forma en Python de invertir una cadena de texto.

if n_ca == n_cb:
    print("has ingresado un numero capicúa")
else:
    print("El número ingresado no es capicúa")

# 11. Escribir un algoritmo de ordenación para un conjunto de datos numéricos en Python.

n_lista = ['1', '3','6','8','9'] # Se crea una lista de strings (cada número está entre comillas, por lo tanto son textos)
n_lista = [int(i) for i in n_lista] # Se convierte cada string de la lista en un entero usando una comprensión de lista.
# Ahora la lista será [1, 3, 6, 8, 9] pero como números.
n_lista.sort() #  Se ordena la lista de forma ascendente. En este caso ya estaba ordenada, pero asegura el orden.
print(f"lista ordenada de manera ascendente: {n_lista}")
n_lista.sort(reverse=True) # ordene de manera descendente añadiendo el parámetro reverse=True
print(f"Lasta ordenanda de manera descendente: {n_lista}")
n_lista_ordenada = sorted(n_lista) # sorted(): Es similar a sort(), pero devuelve una nueva lista ordenada sin modificar la original.
print(f"Nueva lista creada desde la anterior: {n_lista_ordenada}")

# sort() con key: Puedes pasarle una función al parámetro key para ordenar según un criterio específico.
n_lista.sort(key=lambda x: abs(x)) # el parámetro key. Le estás diciendo a Python: “ordena cada elemento de la lista usando como criterio el resultado de la función abs(x)”.
# abs(x): es la función abs() de Python que devuelve el valor absoluto de x.
"""
    lambda x: abs(x): es una función anónima (lambda) que toma cada elemento x y devuelve abs(x)
    Cuando quieres ordenar por valor absoluto y no por el valor original (por ejemplo, cuando tienes números negativos).
"""
print(f"lista ordenada con valores absolutos {n_lista}")


# El código es inválido porque en Python raise y except no funcionan con strings, sino con clases de excepción
"""
try:
    if '1' != 1:
        raise "algún error" # No puedes lanzar un string, debes lanzar una excepción como raise ValueError("algún error") o raise Exception("algún error").
    else:
        print("no se ha producido algún error")
except "algún error": # debe capturar una clase de excepción o una instancia, no un string. Debe ser algo como except ValueError as e:
    print("Se ha producido algún error")
"""

# Version valida de código

try:
    if '1' != 1:
        raise ValueError("algún error")
    else:
        print("no se ha producido algún error")
except ValueError as e:
    print(f"Se ha producido algún error: {e}")

# 14. ¿Como se puede acceder al último índice de una lista?

n_lis_ind = [12,23,56,78,9]
print(f"se imprime el ultimo elemento de la lista: {n_lis_ind[-1]}")
print(f"imprime el primer elemento de la lista: {n_lis_ind[0]}")
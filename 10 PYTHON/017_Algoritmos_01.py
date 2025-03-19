

"""
    A la idea del tiempo la llamaremos complejidad temporal y a la de recursos
    del sistema la llamaremos complejidad espacial.
"""

def codigo_1 (number): 
    a=0

    for j in range(1, number +1):
        a += a + j

    for k in range(number, 0, -1): # Instrucciones = 3n+1
        a -= 1 
        a *=2
        return a   
    
def codigo_2(): # F(x) = 3
    a = 0
    a -= 1
    a *= 2

def codigo_3(number): # F(x) = n2+1
    a = 0

    for j in range(1, number + 1):
        for k in range(1, number + 1): 
            a += a + (k * j)

    return a        

# codigo para encontrat el primer numero par de la lista

def codigo_4(array):
    for k in range(len(array)):
        if(array[k] % 2 == 0):
            return k
    
    return None

# Constante O(1) / Es la más sencilla y siempre presenta un tiempo de ejecución constante.

def constante():
    x=50
    ++x
    return x

# Lineal O(x) / El tiempo crece linealmente mientras crece los datos

def lineal(number):
    result = 0
    for x in range(0, number):
        ++result

    return result    

# Polinómico O(xc), c > 0 / Son los algoritmos más comunes
""" 
    Cuando c es 2 se le llama cuadrático, cuando es 3 se le llama cúbico, y
    en general, polinómico. Cuando n es muy grande suelen ser muy complicados. Estos algoritmos suelen
    tener bucles anidados. Si tienen 2 bucles anidados sería un cuadrático.
"""

def polinomico(number):
    x = 0 
    for i in range(1,  number):
        for j in range(1, number):
            x += i + j

    for i in range(1, number):
        for j in range(1, number):
            for k in range(1, number):     
                x += i * j * k
    return x             

# Logarítmico O(log x) no suelen ser muchos

""" 
    Estos algoritmos indican que el tiempo es menor que el tamaño de los datos de
    entrada. No importa indicar la base del logaritmo. Un ejemplo es una búsqueda dicotómica.
"""
""" 
    Este algoritmo busca un elemento en un array  ordenado dividiendo el array en 2 mitades, identifica
    en cuál de las mitades se encuentra, luego divide esa parte en 2 mitades iguales y busca nuevamente hasta
    encontrar el elemento, es un algoritmo recursivo:
"""
 
def bin(a, x, low, high): #  # Definimos una función llamada 'bin' que recibe una lista 'a', un valor 'x' a buscar y dos índices: 'low' y 'high'.
    ans = -1 # Inicializamos la variable 'ans' con -1, indicando que aún no hemos encontrado el valor.
    if low == high:   # Caso base: si low es igual a high, significa que el rango ya se ha reducido al mínimo.
        ans = -1  # En ese caso, devolvemos -1, indicando que no se encontró el valor.
    else:
        mid = (low + ((high-low)//2)) # Calculamos la posición media entre 'low' y 'high'.
        if x < a[mid]: # Si el valor 'x' es menor que el valor en la posición 'mid'...
            ans = bin(a, x, low, mid)  # ...hacemos una llamada recursiva en la mitad izquierda (low hasta mid).
        elif x > a[mid]: # Si el valor 'x' es mayor que 'a[mid]'...
            ans = bin(a, x, mid+1, high)  # ...hacemos la llamada recursiva en la mitad derecha (mid+1 hasta high).
        else: # Si encontramos que 'x' es igual a 'a[mid]'...
            ans = mid # ...entonces hemos encontrado la posición, y guardamos el índice 'mid' en 'ans'.
    return ans # Finalmente, devolvemos 'ans', que será el índice donde se encontró 'x' o -1 si no se encontró.

# Exponencial: O(Cx)
""" 
    Es una de las peores complejidades algorítmicas. Sube demasiado a medida que crece los datos de
entrada. Puede verse en la Figura como crece una función de este tipo. Un ejemplo de este código es la
solución de Fibonacci, el cual genera bucles 2 recursividades en cada ejecución. Ejemplo:
"""
def exponencial(n):
    if n==1 or n==2:
        return 1
    return exponencial(n-1) + exponencial(n-2)



import numpy as np
import time
import math

# función con múltiples parámetros con una sentencia de retorno

numer_1 = int(input("ingresa el primer: "))
numer_2 = int(input("Ingresa otro valor: "))

def multiplica(val1: int, val2: int):
     resultado = val1 * val2
     return resultado

print(multiplica(numer_1, numer_2)) # se llama la función y se le asignan los valores necesarios para que se ejecute la función


# lista con 10 millones de números
x = list(np.random.randint(low=1, high=500000, size= 10000000))

# Complejidad Constante O(k) Constant Time
def constante(x: list) -> list:
    return x

# Medir el tiempo de ejecución

start_time = time.time()
constante(x)
end_time = time.time()

print(f"Tiempo de ejecución Complejidad Constante O(k) : {end_time - start_time} segundos")

# Complejidad O(n) Linear Time
def iterador_normal(x:list) -> list:
     contador = len(x)
     while(contador > 0):
          contador -= 1
     return x

# Medir el tiempo de ejecucion
start_time = time.time()
iterador_normal(x)
end_time = time.time()

print(f"Tiempo de ejecución Complejidad O(n): {end_time - start_time} segundos")

# Complejidad O(n2) Quadratic Time
def iterador_anidado(x:list) -> list:
     contador_externo = len(x)//1000
     contador_interno = len(x)//1000

     while(contador_externo > 0):
          contador_externo -= 1
     
     for i in range(contador_interno):
          i
          return x

# Medir el tiempo de ejecucion
start_time = time.time()
iterador_anidado(x)
end_time = time.time()

print(f"Tiempo de ejecución Complejidad O(n2) Quadratic: {end_time - start_time} segundos")

# Complejidad O(log(n)) Logarithmic Time
def iterador_multiplicado(x:list) -> list:
     iterador = len(x)
     incremento = 1
     while(iterador > 0):
          iterador -= incremento
          incremento *= (incremento + 1)

     return x

# Medir el tiempo de ejecucion
start_time = time.time()
iterador_multiplicado(x)
end_time = time.time()

print(f"Tiempo de ejecución Complejidad O(log(n)) Logarithmic : {end_time - start_time} segundos")

# Complejidad O(log(log(n))) Logarithmic from Logarithmic Time
def iterador_incremento_exponencial(x:list) -> list:
     iterador = len(x)
     incremento = 1
     while(iterador > 0):
          iterador -= pow(incremento, 2)
          incremento += 1
     return x

# Medir el tiempo de ejecucion
start_time = time.time()
iterador_incremento_exponencial(x)
end_time = time.time()

print(f"Tiempo de ejecución Complejidad O(log(log(n))) Logarithmic from Logarithmic: {end_time - start_time} segundos")

# Cálculo de la complejidad Algorítmica del Ejemplo / 'La Complejidad es n*n*n, n cubo'
y = list(np.random.randint(low=1,high=500000, size=999))

def calculo_bit_o_ejemplo(y:list) -> str: 
     iterador = -len(y) # k
     incremento = 1 # k
     q_list = y # k

     while(iterador < 0): # log(n)
          iterador /= incremento # k
          incremento += 1 # k
     for p in y: # n
          for q in y: # n -> n * n
               for r in y: # n -> n * n * n
                    r
     return "La Complejidad es n*n*n, n cubo"

# Medir el tiempo de ejecucion
start_time = time.time()
calculo_bit_o_ejemplo(y)
end_time = time.time()

print(f"Tiempo de ejecución Cálculo de la complejidad Algorítmica del Ejemplo: {end_time - start_time} segundos")

import time

""" 
    La clasificación de burbujas es un algoritmo simple. Intercambia los elementos adyacentes en cada
    iteración repetidamente hasta que se ordena la matriz dada.
"""

def bublle_sort(arr, n):
    for i in range(n):
        # Iterando de 0 a n-i-1 ya que los últimos i elementos ya están ordenados
        for j in range(n - i -1):
            # Comprobando el siguiente elemento
            if arr[j] > arr[j +1 ]:
                # Intercambiando los elementos adyacentes
                arr[j], arr[j +1] = arr[j +1], arr[j]

if __name__ == "__main__":
    # Inicialización del array
    arr = [12,34,54,6,7,2,90,87,5]
    print(f"lista sin ordenar: {arr}")

    bublle_sort(arr, len(arr))
    print(f"Lista ordenada: {arr}")


# Medir el tiempo de ejecucion
start_time = time.time()
bublle_sort(arr, len(arr))
end_time = time.time()

print(f"Tiempo de ejecución Cálculo de la complejidad Algorítmica del Ejemplo: {end_time - start_time} segundos")
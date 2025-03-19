""" 
    La clasificación es una de las funciones más utilizadas en programación. Y si no usamos el
    algoritmo correcto llevará tiempo extra completar la clasificación.
"""

# Insertion Sort / No es recomendable para clasificar matrices grandes.

""" 
    Ordena un array usando el algoritmo de inserción.
    Parámetros:
        arr: Lista a ordenar.
        n: Longitud de la lista.
"""
def insertion_sort(arr, n): 
    for i in range(1, n): 
        """ 
            Itera desde el segundo elemento (i = 1) hasta el último elemento del array.   En cada iteración, 
            posicion_actual es la posición del elemento actual, y posicion_elemento es el valor de ese elemento.
        """
        posicion_actual = i # posición actual y elemento
        posicion_elemento = arr[i] ## iterar hasta llega al primer elemento o

# el elemento actual es más pequeño que el elemento anterior
        """
            Compara el elemento actual con los elementos anteriores. Si el elemento actual es menor
              que el elemento anterior, mueve el elemento anterior una posición hacia la derecha.
                Repite este proceso hasta que el elemento actual esté en la posición correcta.
        """
        while posicion_actual > 0 and posicion_elemento < arr[posicion_actual -1]: ## actualizar el elemento actual con el elemento anterior
          arr[posicion_actual] = arr[posicion_actual -1] ## moviéndose a la posición anterior
          posicion_actual -=1 ## actualizar el elemento de posición actual
          arr[posicion_actual] = posicion_elemento 

if __name__ == "__main__":
    #inicializacion del array
    arr = [3, 4, 7, 8, 1, 9, 5, 2, 6,11,23]
    print(f"Lista sin ordenar: {arr}")
    insertion_sort(arr, len(arr))

    print(f"Lista ordeana: {arr}")
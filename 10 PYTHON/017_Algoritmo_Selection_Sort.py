# implementación del algoritmo selection sort

def selection_sort(arr, n):
    for i in range(n):  # Itera sobre cada elemento del array. 
        #En cada iteración, asume que el elemento actual (arr[i]) es el mínimo.
    # para almacenar el índice del elemento minimo
        min_element_index = i
        for j in range(i + 1, n): # Compara el elemento actual con los elementos restantes del array.
            # comprobando y reemplazando el indice minimo del elemento
            if arr[j] < arr[min_element_index]:
                min_element_index = j
            # Intercambiando el elemento actual con el elemento minimo
        arr[i], arr[min_element_index] = arr[min_element_index], arr[i]

if __name__ == "__main__":
    # Inicialización del array
    arr = [3,4,5,67,42,4,6,78,2,1,0]
    print(f"lista sin ordenar: {arr}")
    selection_sort(arr, len(arr))

    #imprimiendo el arry
    print(f"lista ordeana: {arr}")
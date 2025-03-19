def merge(arr, left_index, mid_index, right_index):
    """
    Función para fusionar dos sub-matrices ordenadas.
    :param arr: Matriz original.
    :param left_index: Índice inicial de la sub-matriz izquierda.
    :param mid_index: Índice medio de la matriz.
    :param right_index: Índice final de la sub-matriz derecha.
    """
    # Crear copias de las sub-matrices izquierda y derecha
    left_array = arr[left_index:mid_index + 1]
    right_array = arr[mid_index + 1:right_index + 1]

    print(f"Matriz izquierda: {left_array}")
    print(f"Matriz derecha: {right_array}")

    # Obtener las longitudes de las sub-matrices
    left_array_length = len(left_array)
    right_array_length = len(right_array)

    # Índices para iterar sobre las sub-matrices
    i = 0  # Índice para la sub-matriz izquierda
    j = 0  # Índice para la sub-matriz derecha

    # Índice para reemplazar elementos en la matriz original
    k = left_index

    # Comparar elementos de ambas sub-matrices y fusionarlos en orden
    while i < left_array_length and j < right_array_length:
        if left_array[i] <= right_array[j]:
            arr[k] = left_array[i]  # El elemento de la izquierda es menor o igual
            i += 1
        else:
            arr[k] = right_array[j]  # El elemento de la derecha es menor
            j += 1
        k += 1

        # Mostrar el estado actual de la matriz
        print(f"Matriz actualizada: {arr}")

    # Agregar los elementos restantes de la sub-matriz izquierda (si los hay)
    while i < left_array_length:
        arr[k] = left_array[i]
        i += 1
        k += 1
        print(f"Matriz actualizada: {arr}")

    # Agregar los elementos restantes de la sub-matriz derecha (si los hay)
    while j < right_array_length:
        arr[k] = right_array[j]
        j += 1
        k += 1
        print(f"Matriz actualizada: {arr}")


def merge_sort(arr, left_index, right_index):
    """
    Función recursiva para ordenar una matriz usando Merge Sort.
    :param arr: Matriz original.
    :param left_index: Índice inicial de la sub-matriz.
    :param right_index: Índice final de la sub-matriz.
    """
    # Caso base: si la sub-matriz tiene un solo elemento, ya está ordenada
    if left_index >= right_index:
        return

    # Calcular el índice medio
    mid_index = (left_index + right_index) // 2

    print(f"Dividiendo: {arr[left_index:right_index + 1]}")

    # Llamadas recursivas para dividir la matriz en mitades
    merge_sort(arr, left_index, mid_index)  # Ordenar la mitad izquierda
    merge_sort(arr, mid_index + 1, right_index)  # Ordenar la mitad derecha

    # Fusionar las dos mitades ordenadas
    merge(arr, left_index, mid_index, right_index)


if __name__ == "__main__":
    # Inicialización de la matriz
    arr = [3, 4, 5, 6, 39, 23, 434, 56, 7, 9, 0, 86, 22, 12, 34]
    print(f"Matriz sin ordenar: {arr}")

    # Llamar a merge_sort para ordenar toda la matriz
    merge_sort(arr, 0, len(arr) - 1)

    print(f"Matriz ordenada: {arr}")
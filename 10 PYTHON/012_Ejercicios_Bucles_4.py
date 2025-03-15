




# Escribe un programa que imprima la tabla de multiplicar del número 7, 
# desde el 7x1 hasta el 7x10, usando un bucle for.

numero = 7
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")


# programa que compara los valores de dos listas, mostrando el valor maximo en cada comparación
lista_1a = [10, 20, 30, 40]
lista_1b = [5, 25, 50, 10]

for a,b in zip(lista_1a, lista_1b):
    m = max(a,b) # al utilizar la expresión max: esta devuelve el valor maximo entre a y b
    print(m, end = ' ')



# Escribe un programa que sume todos los números enteros del 1 al 100 usando un bucle for.

suma = 0

for numero in range(1, 101):
    suma += numero
print("La suma de los números del 1 al 100 es:", suma)


a = 31
b = a // 2
# División entera. P. ej. 13 // 2 == 6
while b > 1:
    if a % b == 0: # % es el operador   resto. P. ej. 10 % 5 == 0
        print(f"{b} es factor de {a}")
        break

    else:
        print(f'{a} es primo')
        b -= 1

print ('\nFuera del Bucle.')

a = 5

while a:   
    print(a, end=' ')
    if a == 2: # Se usa 'if' en lugar de una comparación suelta
        break
    a -=1 # Se reduce a para evitar un bucle infinito

print('\n fuera del bucle')
print(f"valor de a: {a}")

nl_b = 7

while bool(nl_b):
    nl_b -= 1
    if nl_b % 2 == 0: # se verifican los numeros pares 
        continue # se evitan los numeros pares segun la sentencia del if
    print(nl_b, end= ' ')

print("fuera del bucle")


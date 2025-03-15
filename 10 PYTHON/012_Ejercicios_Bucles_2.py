


# Utiliza un bucle for para generar e imprimir la lista de los cuadrados 
# de los primeros 10 números enteros (1 al 10).

cuadrados = []
for numero in range(1, 11):
    cuadrados.append(numero ** 2)
print("Cuadrados de los números del 1 al 10:", cuadrados)


"""
    ejemplo, donde se evalua si un número es primo o no dentro de un bucle while
"""

ln_a = 89
ln_b = ln_a // 2 # se realiza division entera (se lleva a cabo redondeo de factores)
print(ln_b)

while ln_b > 1:
    if ln_a % ln_b == 0: # se usa el operador de resto o residuo
        print(f"{ln_b} es factor de {ln_a}")
        break
    ln_b -= 1
else:
    print(f"\n{ln_a} es primo")
    
print("\nfuera del bucle")


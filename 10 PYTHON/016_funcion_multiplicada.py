# función con múltiples parámetros con una sentencia de retorno

numer_1 = int(input("ingresa el primer: "))
numer_2 = int(input("Ingresa otro valor: "))

def multiplica(val1: int, val2: int):
     resultado = val1 * val2
     return resultado

print(multiplica(numer_1, numer_2)) # se llama la función y se le asignan los valores necesarios para que se ejecute la función

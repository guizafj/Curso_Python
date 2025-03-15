import sys
import math


# Escribe un script que solicite al usuario su edad y asegúrate de que el 
# número proporcionado esté entre 1 y 100. Si el número está fuera de ese rango, 
# pídele que lo introduzca nuevamente.

edad = int(input("Introduce tu edad (entre 1 y 100): "))
while edad < 1 or edad > 100:
    print("Error: la edad debe estar entre 1 y 100.")
    edad = int(input("Introduce tu edad nuevamente: "))
print("Edad válida introducida:", edad)

"""
The program:
Your program must determine in which category belongs a given integer. The possible integers are named intervals that are also given.
The intervals do not overlap.
The integer always belongs to a category.

INPUT:
Line 1: X the integer to categorize.
Line 2: N an integer for the number of categories.
Next N lines: Two integers F and T for the inclusive bounds of the interval, followed by a word category, its name.

OUTPUT:
The name of the category with the interval that contains X.

CONSTRAINTS:
0 < N < 100
-1000 ≤ F ≤ T ≤ 1000
F ≤ X ≤ T

EXAMPLE:
Input
10
3
-1000 -1 negative
0 0 null
1 1000 positive
Output
positive

"""

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

x = int(input())
n = int(input())
for i in range(n):
    inputs = input().split()
    f = int(inputs[0])
    t = int(inputs[1])
    category = inputs[2]

    if x <0:
        n = "negative"
    elif x == 0:
        n = "null"
    elif x > 0:
        n = "positivo"  
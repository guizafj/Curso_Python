s_nombreIntroducido = input("Introduce tu nombre: ")

print("Bienvenido", s_nombreIntroducido)

# -------------------------------------

"""   IMPORTANTE: Todo lo introducido por input() se considera string, aunque sea un número, 
por lo que, si necesitamos operar matemáticamente con números, tendremos que hacer un casting: 
"""

s_edad = int(input("Introduce tu edad: "))

print("El año que viene tu tendras ", s_edad + 1, "años")

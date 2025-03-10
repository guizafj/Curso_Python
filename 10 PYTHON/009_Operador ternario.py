

#	Operador ternario

num = 12

var = "par" if (num % 2 == 0) else "impar"

print(var)

#	Sería como escribir

num = 12

if num % 2 == 0:
    print("Par") 
else:
    print("Impar")


# Implementación de operador condicional
ls_nombre = str(input("Ingresa tu nombre: ")).title()
ln_edad = 34 if (ls_nombre == "javier") else 17
print(f"{ls_nombre} tu edad es: {ln_edad}")

ls_tiempo = str(input("¿Llueve o hace sol? "))
print("vamos", "a la piscina" if (ls_tiempo == "sol") else " al cine")

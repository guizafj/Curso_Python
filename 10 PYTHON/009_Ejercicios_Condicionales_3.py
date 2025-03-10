

# Escribe un script que solicite una calificación al usuario (0 - 100). 
# Si la calificación es mayor o igual a 90, imprime "Excelente", si es mayor 
# o igual a 70 y menor que 90, imprime "Bueno", si es mayor o igual a 50 y 
# menor que 70, imprime "Suficiente", y si es menor que 50, imprime "Insuficiente".
#mejorar el condicional para que valide el tipo de dato, que no introduzca negativos,
# que no ingrese numeros mayores de 100

calificacion = float(input("Ingresa tu calificación (0-100): "))
if calificacion >= 90:
    calificacion = "aprovado"
    print("Tu promedio a sido:", calificacion.capitalize())
elif calificacion >= 70:
    calificacion = "bueno"
    print("Tu promedio a sido:", calificacion.capitalize())
elif calificacion >= 50:
    calificacion = "suficiente"
    print("Tu calificacion a sido:", calificacion.capitalize())
else:
    calificacion = "insuficiente"
    print("Tu calificacion a sido:", calificacion.capitalize())

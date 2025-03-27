from math import pi

def area(r):
    # Verificamos los tipos correctos
    if type(r) not in [float, int]:
        raise TypeError("solo números enteros o de coma flotante")

    # Verificamos los valores negativos
    if r < 0:
        raise ValueError("No se permiten valores negativos")
    
    areaC = pi*(r**2)
    return areaC

valores = [1, 3, 0, -1, -3, 2+3j, True, 'hola']

for v in valores:
    areaCalculada = area(v)
    print(f'Para el valor {v} el área es {areaCalculada}')
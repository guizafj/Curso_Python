def indexador(objeto, indice):
    return objeto[indice]

# print(indexador('Python', 4))

try:    
    indexador('Python', 10)
except IndexError: # se realiza la capatrua del Indexerror
    print("has puesto un indice muy grande")
finally: # Esta expresión se usa para asegurar el cierre de de un fichero o una conexión 
    print('Esto se ejecuta incluso cuando salta la excepción')

print("Estamos fuera del try-catch")

try:
    indexador('Python', 'h')
    # para evitar que el flujo del programa se dentenga es recomndable usar el bloque except
except (IndexError, TypeError):
    print("Error")
    # El uso de finally solo asegura que el codigo de su bloque se ejecute, pero impide que el flujo del programa se detenga
finally: # Esta expresión se usa para asegurar el cierre de de un fichero o una conexión 
    print('Esto se ejecuta incluso cuando salta la excepción')

print("Estamos fuera del try-catch")

 # Captura todos los errores. No recomendado.
"""
    try:
        indexador('Python', 'h')
    except: 
        print('Error.')

    print('Hemos salido del try-catch')
"""

try:
    indexador('Python', 'h')
except IndexError: 
    print("Error de indice")
except TypeError:
    print("El indice tiene que ser un número")
finally: # Esta expresión se usa para asegurar el cierre de de un fichero o una conexión 
    print('Esto se ejecuta incluso cuando salta la excepción')

print("Estamos fuera del try-catch")

try:
    raise IndexError('Excepción lanzada manualmente')
except IndexError as e: #  # Aquí `e` es la variable que almacena la excepción capturada
    print(f'He capturado mi propia excepción: {e}')


""" 
ex_a = 10
ex_b = 21
la sentencia assert:
    su uso es muy útil para detectar errores en 
    depuración, pero no se recomienda el uso de assert en producción.
# assert(ex_a > ex_b), 'A tiene que ser mayor que B' # si se cumple la condición no salta el error
# print("Continua el ciclo del programa normal, se ha cumplido la condicion")
"""

class miPropiaExcepcion(Exception): # Esta clase hereda de la clase raiz Exception
    
    def __init__(self, valor):
        self.valor = valor

    def __str__(self): # define como hay que representar una clase si se la quiere mostrar como un string (una cadena de texto)
         return str(self.valor)
    
#raise (miPropiaExcepcion("Mensaje de error"))

def indexado(objeto, indice):
    return objeto[indice]
"""
    En este caso, indexador produce una excepción, que capturamos en el bloque except, por lo que ejecutamos el código dentro de ese bloque.
Luego, ejecutamos el código finally y, tras ello, como ejecutamos el código fuera de nuestro bloque try/except/finally.
"""
try:
    indexador('Python', 10)
except IndexError:
    print('Capturamos la excepción')
finally:
    print('Esto se ejecuta incluso cuando salta la excepción')
print('Se ejecutará este print?')

def divide(x, y):
    try:
        resultado = x/y
    except ZeroDivisionError:
        print("No se pude dividir por cero")
    else:
        print(f"El resultado es:{resultado} ")
    finally:
        print('Ejecutamoss el finally')

divide(4,12)

divide(4,0)
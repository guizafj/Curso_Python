class Repetidor(): # Definir la clase sin argumentos en la cabecera.

    def __init__(self, veces, item):
        self.veces = veces  # Número de repeticiones
        self.item = item # Elemento a repetir
        self.counter = 0   # Contador de iteraciones

    def __iter__(self):
        return self     # Un iterador debe devolverse a sí mismo

    def __next__(self):
        if self.counter == self.veces:
            raise StopIteration('Iterador consumido') # Indica que el iterador terminó

        self.counter += 1
        return self.item     # Devuelve el valor repetido

# Prueba del iterador
repetidor = Repetidor(3, "Python")

for item in repetidor:
    print(item)


class Repetidor_1():

    def __init__(self, veces, *items):
        self.veces = veces
        self.items = items
    
    def __iter__(self):
        return iter(self.items * self.veces) # Devuelve iterador de la lista

for r in Repetidor_1(3, 'a', 'b', 'c'):
    print(r, end=' ')
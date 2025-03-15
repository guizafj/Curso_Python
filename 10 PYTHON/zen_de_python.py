zen = '''\
... Bello es mejor que feo.
... Explícito es mejor que implícito.
... Simple es mejor que complejo.
... Complejo es mejor que complicado.
... Plano es mejor que anidado.
... Espaciado es mejor que denso.
... La legibilidad es importante.
... Los casos especiales no son lo suficientemente especiales como para romper las reglas.
... Sin embargo la practicidad le gana a la pureza.
... Los errores nunca deberían pasar silenciosamente.
... A menos que se silencien explícitamente.
... Frente a la ambigüedad, evitar la tentación de adivinar.
... Debería haber una, y preferiblemente solo una, manera obvia de hacerlo.
... A pesar de que eso no sea obvio al principio a menos que seas Holandés.
... Ahora es mejor que nunca.
... A pesar de que nunca es muchas veces mejor que *ahora* mismo.
... Si la implementación es difícil de explicar, es una mala idea.
... Si la implementación es fácil de explicar, puede que sea una buena idea.
... Los espacios de nombres son una gran idea, ¡tengamos más de esos!
... 
'''
f = open('short.zen.txt', 'w') # Se guarda un archivo en formato txt
f.writelines(zen) # Escribe el fichero
f.close() # Cierra el fichero

f = open('short.zen.txt', 'r') # se abre un archivo declarado en ' '
f.readline()
f.readline()
f.readline() # Devuelve una cadena vacia cuando termina el archivo

f = open('short.zen.txt', 'r') # se puede abrir un archivo en una variable
f.__next__() # se puede recorrer linea a linea usando el metodo next
next(f)
next(f)

for linea in open('short.zen.txt'): # uso de for para recorrer e imprimir un archivo
   print(linea.upper(), end='')
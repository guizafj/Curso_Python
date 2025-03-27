# Creación de la clase padre
class Padre():
    def __init__(self, ojos, cejas):
        # Definicion de los atributos en el constructor de la clase
        self.ojos = ojos
        self.cejas = cejas

# Creacion de la clase hijo que hereda de la clase padre
class Hijo(Padre):
    # Definicion de los atributos en el constructor
    def __init__(self, ojos, cejas, cara):
        # se sobreescriben los atributos
        self.ojos = ojos
        self.cejas = cejas
        self.cara = cara # se especifica el nuevo atributo

tomas = Hijo('Marrones', 'Negras', 'Larga') # se instancia o se crea un objeto de la clase hijo
print(tomas.ojos, tomas.cejas, tomas.cara)    

# Mismo ejemplo llamando al constructor de la clase madre:

#Creacion de la clase padre
class Madre(object): 
    def __init__(self, ojos, cejas):
        # Definicion de los atributos
        self.ojos = ojos
        self.cejas = cejas

# Creacion de la clase hija que hereda de la clase madre
class Hija(Madre):
    # Creacion del constructor de la clase especificando los atributos
    def __init__(self, ojos, cejas, cara):
        # Especificacion de la clase y llamado a su construtor mas los atributos
        Padre.__init__(self, ojos, cejas)   # Este metodo se utiliza en caso de herencia multiple
        self.cara = cara       #Especificamos el nuevo atributo para Hija

mile = Hija('azules', 'negras', 'Larga')
print(mile.ojos, mile.cejas, mile.cara)

# Utilizando super(). De esta forma es casi el mismo codigo, pero no se hace necesario especificar la clase padre

# creación de la clase abuelo
class Abuelo(object):
    def __init__(self, ojos, cejas):
        #Definimos los Atributos
        self.ojos = ojos
        self.cejas = cejas

# Clase que hereda de la clase padre (abuelo)
class Nieto(Abuelo):
    #creamos el constructor de la clase especificando atributos
    def __init__(self, ojos, cejas, cara):
        #Solicitamos a super llamar de la clase padre esos atributos
        super().__init__(ojos, cejas)
        self.cara = cara # Especificacion del nuevo atributo

miguel = Nieto('verdes', 'negras', 'redonda')
print(miguel.ojos, miguel.cejas, miguel.cara)

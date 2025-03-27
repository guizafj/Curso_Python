"""
    La clase empleado contiene un constructor para inicializar sus atributos
        Los datos utilizados son: nombre completo, cedula y teléfono.
    Cada atributo de la clase cuenta con sus respectivos get y set.
"""

class Empleado:
    def __init__(self, nombre, cedula, telefono):
        self.__nombre = nombre
        self.__cedula = cedula
        self.__telefono = telefono
    
    def set_nombre(self, nombre):
        self.__nombre = nombre
    
    def get_nombre(self):
        return self.__nombre
    
    def set_cedula(self, cedula):
        self.__cedula = cedula
    
    def get_cedula(self):
        return self.__cedula

    def set_telefono(self, telefono):
        self.__telefono = telefono
    
    def get_telefono(self):
        return self.__telefono

"""
    Clase de empleado por tiempo definido Esta clase hereda de la clase empleado. 
    Los nuevos atributos son:
            Número de plaza
            Salario base
            Duración de contrato en meses
    Además, cuenta con un método que calcula el salario total El empleado recibe un aumento del 2% sobre su salario base.        
"""

class EmpleadoDefinido(Empleado):
    def __init__(self, nombre, cedula, telefono, nPlaza, salarioBase, duracion_contrato):
    #constructor de la clase empleado
        super().__init__(nombre, cedula, telefono)
        #Nuevos atributos
        self.__nPlaza = nPlaza
        self.__salarioBase = salarioBase
        self.__duracion_contrato = duracion_contrato
        
    def set_nPlaza(self, nPlaza):
        self.__nPlaza = nPlaza
    
    def get_nPlaza(self):
        return self.__nPlaza
    
    def set_salarioBase(self, salarioBase):
        self.__salarioBase = salarioBase

    def get_salarioBase(self):
        return self.__salarioBase
    
    def set_duracion_contrato(self, duracion_contrato):
        self.__duracion_contrato = duracion_contrato

    def get_duracion_contrato(self):
        return self.__duracion_contrato
    
    #calcula el salario total
    def calcularSalarioTotal(self):
        return self.__salarioBase + (self.__salarioBase * 0.02)
    
"""
    Clase de empleado por tiempo indefinido Esta clase hereda de la clase empleado. 
    Los nuevos atributos son:
            Número de plaza
            Salario base
            Categoría (1, 2, 3)
    Además, cuenta con un método que calcula el salario total.
      Los empleados recieben un aumento de acuerdo a su categoría:
            Categoría 1: 3%
            Categoría 2: 5%
            Categoría 3: 8%
"""

class EmpleadoIndefinido(Empleado):
    def __init__(self, nombre, cedula, telefono, nPlaza, salarioBase, categoria):
        #constructor de la clase empleado
        super().__init__(nombre, cedula, telefono)
        #Nuevos atributos
        self.__nPlaza = nPlaza
        self.__salarioBase = salarioBase
        self.__categoria = categoria
    
    def set_nPlaza(self, nPlaza):
        self.__nPlaza = nPlaza
    
    def get_nPlaza(self):
        return self.__nPlaza
    
    def set_salarioBase(self, salarioBase):
        self.__salarioBase = salarioBase
    
    def get_salarioBase(self):
        return self.__salarioBase
    
    def set_categoria(self, categoria):
        self.__categoria = categoria
    
    def get_categoria(self):
        return self.__categoria
    
    #calcula el salario total
    def calcularSalarioTotal(self):
        if self.__categoria == 1:
            return self.__salarioBase + (self.__salarioBase * 0.03)
        elif self.__categoria == 2:
            return self.__salarioBase + (self.__salarioBase * 0.05)
        elif self.__categoria == 3:
            return self.__salarioBase + (self.__salarioBase * 0.08)
        else:
            return self.__salarioBase
        
"""
    Empleado subcontratado Esta clase hereda de la clase empleado.
      El nuevo atributo es:
          Empresa responsable
"""

class EmpleadoSubcontratado(Empleado):
    def __init__(self, nombre, cedula, telefono, empresaResponsable):
        super().__init__(nombre, cedula, telefono)
        self.__empresaResponsable = empresaResponsable
    
    def set_empresaResponsable(self, empresa):
        self.__empresaResponsable = empresa
    
    def get_empresaResponsable(self):
        return self.__empresaResponsable
    

"""
    Ejecución del código
    La siguiente celda ejecuta las clases creadas anteriormente. Ejecuta 8 tipos de empleados
    desglosados de la siguiente manera:
        2 contratados
        4 indefinidos    
        2 subcontratados
"""

#Empleados subcontratados
subContratado1 = EmpleadoSubcontratado("Roberto Flores Morales", 123456789, 88888888, "Coca-Cola")
subContratado2 = EmpleadoSubcontratado("Ana Mora Cruz", 223446789, 77777777, "Pepsi")

print("*** Empleados subcontratados ***")
print("\n****Empleado 1****")
print("Nombre: " + subContratado1.get_nombre() +
"\nCédula: " + str(subContratado1.get_cedula()) +
"\nTeléfono: " + str(subContratado1.get_telefono()) +
"\nEmpresa responsable: " + subContratado1.get_empresaResponsable())

print("\n****Empleado 2****")
print("Nombre: " + subContratado2.get_nombre() +
"\nCédula: " + str(subContratado2.get_cedula()) +
"\nTeléfono: " + str(subContratado2.get_telefono()) +
"\nEmpresa responsable: " + subContratado2.get_empresaResponsable())

#Empleados por tiempo definido
empleadoD = EmpleadoDefinido("Jeff Muñoz Castro", 345687324, 66666666, 3, 500000, 3)
empleadoD2 = EmpleadoDefinido("María Gonzáles Pérez", 983456783, 99999999, 6, 450000, 2)

print("\n*** Empleados de tiempo definido ***")
print("\n****Empleado 1****")
print("Nombre: " + empleadoD.get_nombre() +
"\nCédula: " + str(empleadoD.get_cedula()) +
"\nTeléfono: " + str(empleadoD.get_telefono()) +
"\nNúmero de plaza: " + str(empleadoD.get_nPlaza()) +
"\nDuracion contrato: " + str(empleadoD.get_duracion_contrato()) + " meses" +
"\nSalario total: " + str(empleadoD.calcularSalarioTotal()))

print("\n****Empleado 2****")
print("Nombre: " + empleadoD2.get_nombre() +
"\nCédula: " + str(empleadoD2.get_cedula()) +
"\nTeléfono: " + str(empleadoD2.get_telefono()) +
"\nNúmero de plaza: " + str(empleadoD2.get_nPlaza()) +
"\nDuración contrato " + str(empleadoD2.get_duracion_contrato()) + " meses" +
"\nSalario total: " + str(empleadoD2.calcularSalarioTotal()))

#empleados por tiempo indefinido
empleadoI = EmpleadoIndefinido("Roberto Rojas Salazar", 434565432, 22222222, 4, 350000,1)
empleadoI2 = EmpleadoIndefinido("Rebeca Suárez Tapia", 897456274, 33445533, 7, 510000, 2)
empleadoI3 = EmpleadoIndefinido("Sara Vega Montes", 989734567, 65786590, 19, 475000, 3)
empleadoI4 = EmpleadoIndefinido("Luis Sánchez Castillo", 546378763, 23546543, 23, 560000, 1)

print("\n*** Empleados de tiempo indefinido ***")
print("\n****Empleado 1****")
print("Nombre: " + empleadoI.get_nombre() +
"\nCédula: " + str(empleadoI.get_cedula()) +
"\nTeléfono: " + str(empleadoI.get_telefono()) +
"\nNúmero de plaza: " + str(empleadoI.get_nPlaza()) +
"\nCategoría: " + str(empleadoI.get_categoria()) +
"\nSalario total: " + str(empleadoI.calcularSalarioTotal()))

print("\n****Empleado 2****")
print("Nombre: " + empleadoI2.get_nombre() +
"\nCédula: " + str(empleadoI2.get_cedula()) +
"\nTeléfono: " + str(empleadoI2.get_telefono()) +
"\nNúmero de plaza: " + str(empleadoI2.get_nPlaza()) +
"\nCategoría: " + str(empleadoI2.get_categoria()) +
"\nSalario total: " + str(empleadoI2.calcularSalarioTotal()))

print("\n****Empleado 3****")
print("Nombre: " + empleadoI3.get_nombre() +
"\nCédula: " + str(empleadoI3.get_cedula()) +
"\nTeléfono: " + str(empleadoI3.get_telefono()) +
"\nNúmero de plaza: " + str(empleadoI3.get_nPlaza()) +
"\nCategoría: " + str(empleadoI3.get_categoria()) +
"\nSalario total: " + str(empleadoI3.calcularSalarioTotal()))

print("\n****Empleado 4****")
print("Nombre: " + empleadoI4.get_nombre() +
"\nCédula: " + str(empleadoI4.get_cedula()) +
"\nTeléfono: " + str(empleadoI4.get_telefono()) +
"\nNúmero de plaza: " + str(empleadoI4.get_nPlaza()) +
"\nCategoría: " + str(empleadoI4.get_categoria()) +
"\nSalario total: " + str(empleadoI4.calcularSalarioTotal()))
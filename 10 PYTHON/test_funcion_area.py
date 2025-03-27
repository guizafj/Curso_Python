import unittest
from funcion_area import area
from math import pi

class TestArea(unittest.TestCase):

    def test_area(self):
        print('-----Test valores de resultado conocido----')
        self.assertAlmostEqual(area(1),pi)
        self.assertAlmostEqual(area(0),0)
        self.assertAlmostEqual(area(3),pi*(3**2))

# Test de valores negativos
    def test_negativos(self):
        print('-----Test de valores negativos------')
        #Indicamos el tipo de excepción, la función y el valor esperado.
        self.assertRaises(ValueError, area, -1)

# test de tipos no compatibles
    # Verificamos si el tipo de los parametros es correcto
        # El tipo de excepción debe ser de TypeError
    # Se realiza una prueba para que cada tipo conocido no valido

    def test_tipos(self):
        print('-----Test de tipos no compatibles-----')
        """Test that the area function raises TypeError for incompatible input types."""
        # Boolean values like True are not valid inputs for the area function, as it expects a numeric type.
        self.assertRaises(TypeError, area, True)
        self.assertRaises(TypeError, area, 'hola')
        # Complex numbers are not valid inputs for the area function because the area of a circle is defined only for real numbers.
        self.assertRaises(TypeError, area, 2+3j)    
       
import unittest
import bin_to_dec

class TestBinaryToDecimal(unittest.TestCase):
    def test_binario_decimal_con_entradas_validas(self):
# El método bin de Python hace la conversión de binario a decimal
# Los bucles son útiles: testeamos un rango de números
        for d in range(100):
            binary = bin(d) # En formato '0b10101'
            binary = binary[2:] # Quitar la inicial '0b'
            dec_output = bin_to_dec.decimal(binary)
            self.assertEqual(d, dec_output)
            # Testeamos algunos números más grandes
            test_vals = [4000, 4001, 4002, 1024, 1099511627776, 1099511627777, 1099511627775]
        for d in test_vals:
            binary = bin(d) # En formato '0b10101'
            binary = binary[2:] # Quitar la inicial '0b'
            dec_output = bin_to_dec.decimal(binary)
            self.assertEqual(d, dec_output)

    # Test con strings
        test_bin_str = [ '101010', '1111', '000111', '0', '1']
        expected_dec = [ 42, 15, 7, 0, 1]
        for binary_input, expected_dec_output in zip( test_bin_str, expected_dec) :
            dec = bin_to_dec.decimal(binary_input)
            self.assertEqual(dec, expected_dec_output)            

    def test_binario_decimal_con_entradas_invalidas(self):
    # Testeamos que se genere un error con cadenas que no estén compuestas por 0 y 1.
        valid = '010101'
        valid2 = '1111111'
        invalid = [ '123456', '101010012', 'abc', '@#$%$%^%^&']
        for invalid_input in invalid:
            with self.assertRaises(ValueError):
                bin_to_dec.decimal(invalid_input)

if __name__ == '__main__':
    unittest.main()
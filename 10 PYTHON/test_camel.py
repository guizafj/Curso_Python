import unittest
from unittest.mock import patch
import camel

class TestCamelCase(unittest.TestCase):
    def test_capitalize(self):
        input_words = ['abc', 'ABC', 'aBC', 'ABc']
        capitalized = 'Abc'

        for word in input_words:
            self.assertEqual(capitalized, camel.capitalize(word))
    
    def test_lower(self):
        # this isn't really needed, since we can assume that Python's library functions work correctly :)
        input_words = ['abc', 'ABC', 'aBC', 'ABc']
        lower = 'abc'
        for word in input_words:
            self.assertEqual(lower, camel.lowercase(word))

    def test_camel_case_single_words(self):
        input_and_expected_outputs = {
            'hello' : 'hello',
            'Hello' : 'hello',
            'Thisisaverylongwordlalalalalalalalalalala':
            'thisisaverylongwordlalalalalalalalalalala',
            'a': 'a'
        }       

        for input_val, output_val in input_and_expected_outputs.items():
            self.assertEqual(output_val, camel.camel_case(input_val))   
    

    def test_camel_case_uppercase(self):
        input_and_expected_outputs = {
            'HELLO': 'hello',
            'Hello': 'hello',
            'HeLLo wORlD': 'helloWorld'
        }

        for input_val, output_val in input_and_expected_outputs.items():
            self.assertEqual(output_val, camel.camel_case(input_val))

    def test_camel_case_lowercase(self):
        input_and_expected_outputs = {
            'hello': 'hello',
            'hELLO': 'hello',
            'heLLo WORlD': 'helloWorld'
        }
        for input_val, output_val in input_and_expected_outputs.items():
            self.assertEqual(output_val, camel.camel_case(input_val))

    def test_camel_case_empty_strings(self):
        input_and_expected_outputs = {
            '': '',
            '    ': '',
        }
        for input_val, output_val in input_and_expected_outputs.items():
            self.assertEqual(output_val, camel.camel_case(input_val))       
    
    def test_camel_case_many_words(self):
        input_and_expected_outputs = {
            'two words': 'twoWords',
            'this is a sentence': 'thisIsASentence',
            'Here is a long sentence with many words' :
            'hereIsALongSentenceWithManyWords',
        }
        for input_val, output_val in input_and_expected_outputs.items():
            self.assertEqual(output_val, camel.camel_case(input_val))

    def test_camel_case_extra_spaces(self):
        input_and_expected_outputs = {
            ' Spaces Before': 'spacesBefore',
            'Spaces after' : 'spacesAfter',
            '  spaces Every where ' : 'spacesEveryWhere',
            '\tThere is a \t tab here': 'thereIsATabHere',
            '\nThere is a \n newline here': 'thereIsANewlineHere',
            'There is a newline here\n': 'thereIsANewlineHere',
            '\nThere is a newline here\n': 'thereIsANewlineHere',
        }
        for input_val, output_val in input_and_expected_outputs.items():
            self.assertEqual(output_val, camel.camel_case(input_val))        

    def test_camel_case_emojis(self):
        input_and_expected_outputs = {
            '👽🌎🌺': '👽🌎🌺',
            '👽 🌎🌺🐑🌳🌵🐬': '👽🌎🌺🐑🌳🌵🐬'
        }
        for input_val, output_val in input_and_expected_outputs.items():
            self.assertEqual(output_val, camel.camel_case(input_val))        

    def test_camel_case_international(self):
        input_and_expected_outputs = {
            '你叫 什么 名字': '你叫什么名字',
            'Write a résumé': 'writeARésumé',
            'Über die Brücke': 'überDieBrücke',
            'Fahre über die Brücke': 'fahreÜberDieBrücke',
        }
        for input_val, output_val in input_and_expected_outputs.items():
            self.assertEqual(output_val, camel.camel_case(input_val))        

    def test_input_and_output(self):
        # Patch the input. Using with context manager automatically takes care of  unpatching.
        with patch('builtins.input', return_value='This IS another SENTenCE'):
        # And, patch the output
            with patch('builtins.print') as mock_print:
                camel.main()
                mock_print.assert_called_with('thisIsAnotherSentence')
if __name__ == '__main__':
    unittest.main()
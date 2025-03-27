import re
""" Convierta la palabra para que tenga la primera letra en mayúscula, el resto en
minúsculas"""

def capitalize(word):
    return word[0:1].upper() + word[1:].lower()
    # Los segmentos no producen errores de tipo "index out of bounds".
#Así que esto todavía funciona en cadenas vacías y cadenas de longitud 1
"""convierte una palabra a minúsculas"""
def lowercase(word):

    return word.lower()

def camel_case(sentence):
    remove_multiple_spaces = re.sub(r'\s+', ' ', sentence) # Reemplaza cualquier grupo de espacios en blanco con un solo espacio
    remove_surrounding_space = remove_multiple_spaces.strip() # elimina cualquier espacio en blanco restante
    words = remove_surrounding_space.split(' ') # Segmenta por espacios
    first_word = lowercase(words[0]) # Pasa a minúsculas la primera palabra
    # Escribe con mayúscula la segunda palabra y las siguientes y las pone en una nueva lista.
    capitalized_words = [ capitalize(word) for word in words[ 1: ] ]
    # Reúne todas las palabras en una lista
    camel_cased_words = [first_word] + capitalized_words
    # Vuelve a juntar las palabras
    camel_cased_sentance = ''.join(camel_cased_words)
    return camel_cased_sentance

def main():
    sentence = input('Introduzca la frase: ')
    camelcased = camel_case(sentence)
    print(camelcased)

if __name__ == '__main__':
    main()
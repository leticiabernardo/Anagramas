from dictionary import Dictionary
from permutation import Permutation

dict = Dictionary()
dict.create_dictionary()

while True:
    print(50 * "-")
    my_word = str(input("Digite a palavra embaralhada a ser encontrada: "))
    my_word_len = len(my_word)

    if my_word_len == 1:
        print("Por favor, digite uma palavra com, pelo menos, duas letras...")
    else:
        perm = Permutation()
        perm.initial_call(my_word)
        break

from search import Search


def main():
    s = Search()

    while True:
        print(50 * "-")
        my_word = str(input("Digite a palavra embaralhada a ser encontrada: "))
        my_word_len = len(my_word)

        if my_word_len == 1:
            print("Por favor, digite uma palavra com, pelo menos, três letras...")
        else:
            total_time, anagrams = s.search_anagrams_fixed_len(my_word)
            if anagrams:
                for i in range(len(anagrams)):
                    print(anagrams[i])
                print("Foram encontrados: {} anagramas".format(len(anagrams)))
            else:
                print("Não foram encontrados anagramas correspondentes...")
            print("Realizado em {}". format(total_time))
            break


if __name__ == "__main__":
    main()

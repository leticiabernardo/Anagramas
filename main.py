from search import Search


def main():
    print(50 * "-")
    print("Carregando sistema...")
    s = Search()

    while True:
        print(50 * "-")
        my_anagram = str(input("Digite a palavra embaralhada a ser encontrada: "))

        if len(my_anagram) < 3:
            print("Por favor, digite uma palavra com, pelo menos, três letras...")
        else:
            total_time, anagrams = s.search_anagrams(my_anagram)

            if anagrams:
                for x in range(len(anagrams)):
                    print(anagrams[x])
                print("Foram encontrados: {} anagramas".format(len(anagrams)))
            else:
                print("Não foram encontrados anagramas correspondentes...")
            print("Realizado em {}". format(total_time))

            # break


if __name__ == "__main__":
    main()

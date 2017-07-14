import os
import shutil
from unicodedata import normalize


def clean_word(string):
    ln = string.strip().split(' ')
    ln = normalize('NFKD', ln[0]).encode('ASCII', 'ignore').decode('ASCII')
    return ln


def check_valid_word(string):
    return True if "-" not in string and not string[0].isupper() else False


def history_record(self, word, num_of_anagrams):
    with open(self.folder + self.controls + self.extension, "a") as fc:
        fc.write("\n{}: {} anagramas encontrados".format(word, num_of_anagrams))


class Dictionary:
    def __init__(self):
        self.folder = "words/"
        self.dictionary_name = "words_pt"
        self.controls = "controls"
        self.extension = ".txt"
        self.effective_word_count = 0

    def create_dictionary(self):
        if os.path.exists(self.folder) and \
                os.path.exists(self.folder + self.controls + self.extension):
            print("O dicionário já foi carregado...")
        else:
            if os.path.exists(self.folder):
                shutil.rmtree(self.folder)

            if not os.path.exists(self.folder):
                os.makedirs(self.folder)

            print("Carregando o dicionário...\n"
                  "Isso pode demorar alguns minutos...\n"
                  "Por favor, aguarde...")

            file = open(self.dictionary_name + self.extension, "r")
            dict_all = file.read()
            file.close()

            dict_all_list = dict_all.strip().split('\n')
            dict_total = len(dict_all_list)

            valid_dict = {}

            for num in range(dict_total):
                if check_valid_word(dict_all_list[num]):
                    self.effective_word_count += 1
                    word_length = len(dict_all_list[num])

                    if word_length in valid_dict.keys():
                        valid_dict[word_length] = valid_dict[word_length] + dict_all_list[num] + "\n"
                    else:
                        valid_dict[word_length] = dict_all_list[num] + "\n"

                    if self.effective_word_count % 500 == 0:
                        print("Foram carregadas {} palavras".format(self.effective_word_count))

            for key in valid_dict:
                f = open(self.folder + "words" + str(key) + self.extension, "w")
                f.write(valid_dict[key])
                f.close()

            with open(self.folder + self.controls + self.extension, "w") as fc:
                fc.write("Número total de palavras: {}\n"
                         "Número de palavras efetivas: {}\n\n"
                         "Histórico:\n{}"
                         "".format(dict_total, self.effective_word_count, 50*'-'))

    def search_in_dictionary(self, length, anagram, *args):
        file = open(self.folder + "words" + str(length) + self.extension, "r+")
        dict_words = file.readlines()
        file.close()

        list_of_anagrams = args[0]
        exists_words = []
        print("Buscando palavras, aguarde...")

        for y in range(len(list_of_anagrams)):
            for x in range(len(dict_words)):

                if clean_word(dict_words[x]) == list_of_anagrams[y]:
                    word = dict_words[x].replace('\n', '')

                    if word not in exists_words:
                        exists_words.append(word)

        history_record(self, anagram, len(exists_words))

        return exists_words

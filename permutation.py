from dictionary import Dictionary
import datetime


class Permutation:
    def __init__(self):
        self.anagram = ""
        self.new_word = []
        self.anagrams_discovered = []

    def generate_word(self, index, length_word):
        for x in range(length_word):

            if index < length_word:
                exists_in_list = True
                for y in range(index + 1):
                    if self.new_word[y] == x:
                        exists_in_list = True
                        break
                    else:
                        exists_in_list = False

                if not exists_in_list:
                    self.new_word.pop(index)
                    self.new_word.insert(index, x)
                    self.generate_word(index + 1, length_word)

            if index == length_word and x == index - 1:
                word = ""
                for character in self.new_word:
                    word += self.anagram[character]

                self.anagrams_discovered.append(word)

    def initial_call(self, anagram):
        length_word = len(anagram)

        self.anagram = anagram
        self.new_word = length_word * [-1]
        self.generate_word(0, length_word)

        start_time = datetime.datetime.now().time().strftime('%H:%M:%S.%f')

        dicts = Dictionary()
        exists_word = dicts.search_in_dictionary(length_word, anagram, self.anagrams_discovered)

        if len(exists_word) == 0:
            print("Não foram encontradas palavras para este anagrama...")
        else:
            for x in exists_word:
                print(x)

        end_time = datetime.datetime.now().time().strftime('%H:%M:%S.%f')
        total_time = (datetime.datetime.strptime(end_time, '%H:%M:%S.%f') -
                      datetime.datetime.strptime(start_time, '%H:%M:%S.%f'))
        print("Realizado em {}". format(total_time))

import datetime
from itertools import permutations
from dictionary import Dictionary
import utils.helpers as helpers


class Search:
    def __init__(self):
        self.anagram = []
        self.new_word = []
        self.anagrams_discovered = []
        self.new_dictionary = Dictionary().load_dictionary()
        self.d = Dictionary()

    @staticmethod
    def _binary_search(my_list, target):
        start = 0
        end = len(my_list) - 1

        while start <= end:
            middle = (start + end) // 2

            if helpers.clean_word(my_list[middle]) == helpers.clean_word(target):
                return my_list[middle]
            else:
                if helpers.clean_word(target) < helpers.clean_word(my_list[middle]):
                    end = middle - 1
                else:
                    start = middle + 1

        return False

    def search_anagrams_fixed_len(self, anagram):
        self.anagram = anagram
        existing_anagrams = []
        all_anagrams = []

        start_time = datetime.datetime.now().time().strftime('%H:%M:%S.%f')

        counter = 0
        for subset in permutations(list(anagram), len(anagram)):
            word = ''.join(subset)
            counter += 1
            if word not in all_anagrams:
                all_anagrams.append(word)

                ret = self._binary_search(self.new_dictionary, word)
                if ret and ret not in existing_anagrams:
                    existing_anagrams.append(ret)

        print("Permutações", counter)
        print("Únicas", len(all_anagrams))
        end_time = datetime.datetime.now().time().strftime('%H:%M:%S.%f')
        total_time = (datetime.datetime.strptime(end_time, '%H:%M:%S.%f') -
                      datetime.datetime.strptime(start_time, '%H:%M:%S.%f'))

        return total_time, existing_anagrams

    def search_anagrams(self, anagram):
        self.anagram = anagram
        existing_anagrams = []

        start_time = datetime.datetime.now().time().strftime('%H:%M:%S.%f')

        z = 0
        for i in range(len(anagram), 2, -1):
            for subset in permutations(list(anagram), i):
                z += 1
                ret = self._binary_search(self.new_dictionary, ''.join(subset))
                if ret and ret not in existing_anagrams:
                    existing_anagrams.append(ret)

        print(z)
        end_time = datetime.datetime.now().time().strftime('%H:%M:%S.%f')
        total_time = (datetime.datetime.strptime(end_time, '%H:%M:%S.%f') -
                      datetime.datetime.strptime(start_time, '%H:%M:%S.%f'))

        return total_time, existing_anagrams

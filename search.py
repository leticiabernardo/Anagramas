from datetime import datetime 
import utils.helpers as helpers


class Search:
    def __init__(self):
        self.anagram = []
        self.dictionary_name = "files/words_pt.txt"
        self.my_dictionary = self._load_dictionary()

    def _load_dictionary(self):
        tmp_dictionary = {}

        file = open(self.dictionary_name, "r")
        dict_all = file.read()
        file.close()

        dict_all = dict_all.strip().split('\n')

        for i in range(len(dict_all)):
            if helpers.check_valid_word(dict_all[i]):
                sorted_word = ''.join(sorted(helpers.clean_word(dict_all[i])))

                if sorted_word not in tmp_dictionary.keys():
                    tmp_dictionary[sorted_word] = list()

                tmp_dictionary[sorted_word].append(dict_all[i])

        return tmp_dictionary

    def search_anagrams(self, anagram):
        existing_anagrams = list()

        sorted_word = ''.join(sorted(helpers.clean_word(anagram)))
        start_time = datetime.now().time().strftime('%H:%M:%S.%f')

        if sorted_word in self.my_dictionary.keys():
            existing_anagrams = self.my_dictionary[sorted_word]

        end_time = datetime.now().time().strftime('%H:%M:%S.%f')
        total_time = (datetime.strptime(end_time, '%H:%M:%S.%f') -
                      datetime.strptime(start_time, '%H:%M:%S.%f'))

        return total_time, existing_anagrams


    def search_like_anagrams(self, anagram):
        existing_anagrams = list()

        sorted_word = ''.join(sorted(helpers.clean_word(anagram)))
        start_time = datetime.now().time().strftime('%H:%M:%S.%f')

        for key_word in self.my_dictionary.keys():
            if sorted_word in key_word:
                existing_anagrams += self.my_dictionary[key_word]

        end_time = datetime.now().time().strftime('%H:%M:%S.%f')
        total_time = (datetime.strptime(end_time, '%H:%M:%S.%f') -
                      datetime.strptime(start_time, '%H:%M:%S.%f'))

        return total_time, existing_anagrams 

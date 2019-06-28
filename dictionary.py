import utils.helpers as helpers


class Dictionary:
    def __init__(self):
        self.folder = "files/"
        self.original_dictionary_name = "words_pt"
        self.new_dictionary_name = "dictionary"
        self.controls = "controls"
        self.extension = ".txt"

    def load_dictionary(self):
        print("Carregando o dicionário...\n"
              "Isso pode demorar alguns minutos...\n"
              "Por favor, aguarde...")

        file = open(self.folder + self.original_dictionary_name + self.extension, "r")
        dict_all = file.read()
        file.close()

        return self._clean_dictionary(dict_all.strip().split('\n'))

    @staticmethod
    def _clean_dictionary(dictionary_list):
        valid_dict = []

        for num in range(len(dictionary_list)):
            if helpers.check_valid_word(dictionary_list[num]):
                valid_dict.append(dictionary_list[num])

        return valid_dict

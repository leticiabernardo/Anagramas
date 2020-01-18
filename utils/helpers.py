
def clean_word(string):
    from unicodedata import normalize

    ln = string.strip().split(' ')
    ln = normalize('NFKD', ln[0]).encode('ASCII', 'ignore').decode('ASCII').lower()
    return ln


def check_valid_word(string):
    return True if "-" not in string and not string[0].isupper() and " " not in string and len(string) > 2 else False

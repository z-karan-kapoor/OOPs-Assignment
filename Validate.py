import re

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'


class Validate:
    """This is to validate name input by the user"""
    def valid_name(self, name):
        if name.replace(" ", "").isalpha():
            return 1
        else:
            return 0

    """This is to validate email input by the user"""
    def check(self, email):
        # pass the regular expression and the string into the fullmatch() method
        if (re.fullmatch(regex, email)):
            return 1        #Valid input
        else:
            return 0        #Invalid input

    """This is to Search the string in the text I/O file"""
    def search_str(self, file_path, word):
        with open(file_path, 'r') as fp:
            for l_no, line in enumerate(fp):
                # search string
                if word in line:
                    return 1        # String found in a file
                    break
        return 0            # String doesn't found

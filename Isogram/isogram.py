import re

def is_isogram( word ):
    if type(word) == str:
        w = re.findall('[a-z]', word.lower())
        if len(w) == len(set(w)):
          return True 
        else:
          return False
    else:
        raise TypeError('Argument should be a string')

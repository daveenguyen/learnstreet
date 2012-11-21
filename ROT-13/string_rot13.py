#ROT-13 Project
from string import ascii_uppercase, ascii_lowercase
import math
def string_rot13(str):
    # ROT-13 is a simple substitution cypher. It stands for
    # "ROTate by 13 places." The cypher replaces any letter
    # (a-z or A-Z) with the one that appears 13 sequential places
    # behind it. Note that for the last half of the alphabet, the
    # ROT-13 character loops back around to the beginning of the
    # alphabet. Also note that characters that aren't in the alphabet
    # are passed through.
    "Return a string in its ROT-13 format"

    total = ""
    
    for x in range(len(str)):
        if str[x] in ascii_uppercase:
            total += ascii_uppercase[(ascii_uppercase.index(str[x])+13)%26]
        elif str[x] in ascii_lowercase:
            total += ascii_lowercase[(ascii_lowercase.index(str[x])+13)%26]
        else:
            total += str[x]

    return total
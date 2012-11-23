#Morse Code project
to_morse = {
        'a': '.-',         'b': '-...',      'c': '-.-.',
        'd': '-..',        'e': '.',         'f': '..-.',
        'g': '--.',        'h': '....',      'i': '..',
        'j': '.---',       'k': '-.-',       'l': '.-..',
        'm': '--',         'n': '-.',        'o': '---',
        'p': '.--.',       'q': '--.-',      'r': '.-.',
        's': '...',        't': '-',         'u': '..-',
        'v': '...-',       'w': '.--',       'x': '-..-',
        'y': '-.--',       'z': '--..',
        '0': '-----',      '1': '.----',     '2': '..---',
        '3': '...--',      '4': '....-',     '5': '.....',
        '6': '-....',      '7': '--...',     '8': '---..',
        '9': '----.',
        ',': '--..--',     '.': '.-.-.-',    '?': '..--..',
        ';': '-.-.-.',     ':': '---...',    "'": '.----.',
        '-': '-....-',     '/': '-..-.',     '_': '..--.-',
        '(': '-.--.',      ')': '-.--.-'
}
from_morse = dict((b,a) for a,b in to_morse.items()) 

def morse(string_word):
    '''Convert a single word, string_word, to Morse code using to_morse above.'''
    '''Note that Morse code is not case-sensitive, so you will want to convert upper case letters to lower case.'''
    string_word = string_word.lower()
    code = ""
    for x in string_word:
        # if x in to_morse:
        code += to_morse[x]+" "
    return code

def str_morse(sentence):
    '''Translate multiple words in a sentence encoded in Morse code, using your morse() function above.'''
    words = sentence.split(" ")
    code = ""
    for word in words:
        code += morse(word)
        code += " "
    return code


def string(morse_word):
    '''Convert a single Morse code word, morse_word, into normal text using from_morse above.'''
    morse_ltrs = morse_word.split(" ")
    word = ""
    for ltr in morse_ltrs:
        for key in to_morse:
            if ltr == to_morse[key]:
                word += key
    return word

def morse_str(morse_sentence):
    '''Convert a sentence in Morse code, splitting out the words and passing them to your new string() function above.'''
    morse_words = morse_sentence.split("  ")
    sentence = ""
    for word in morse_words:
        sentence += string(word)
        sentence += " "
    return sentence.strip()
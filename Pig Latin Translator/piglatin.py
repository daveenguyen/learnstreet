#Pig Latin Translator Project

#convert a english word into piglatin
def to_latin(english_word):
    # This method accepts an English word ('english_word') passed
    # in as a string. It translates the word into Pig Latin and return
    # the translation as a string. Pig Latin "translation" rules are simple:
    piglatin_word = ''
    # 1) words that start with a vowel (a, e, i, o, u) simply have '-way'
    # appended to the end of the word, and
    vowels = ('a','e','i','o','u')
    english_word = english_word.lower()
    if english_word[0] in vowels:
        piglatin_word = english_word + '-way'
    # 2) words that start with a consonant have all their consonant letters
    # up to the first vowel moved to the end of the word, and '-ay' is appended
    # ('y' is counted as a vowel in this context).
    else:
        index = 0
        for char in english_word:
            if char in vowels:
                break
            elif char == 'y':
                break
            else:
                index += 1
        piglatin_word = english_word[index:] + '-' + english_word[:index] + 'ay'
    # Thus, the English word "idle" becomes "idle-way" and
    # "bacon" becomes "aconb-ay".
    return piglatin_word

#split sentence into words and call to_latin for each word
def translateTopiglatin(english):
    # This method handles converting entire phrases or sentences from
    # English to Pig Latin. It takes an English character string as its input
    # ('english') and returns the string translated into Pig Latin. Use the
    # Pig Latin word converter written above as to_latin().
    english_words = english.split(" ")
    piglatin_sentence = ""
    for word in english_words:
        piglatin_sentence += to_latin(word)
        piglatin_sentence += " "
    return piglatin_sentence.strip().capitalize()
    
#convert a piglatin word into english
def to_english(latin_word):
    # This method converts a Pig Latin word (the input string 'latin_word')
    # into English and returns the translated word as a string. Think of this as
    # the reverse of the to_latin() function above. Remember the original
    # to-Pig-Latin translation rules:
    # 1) words that start with a vowel (a, e, i, o, u) simply have '-way'
    # appended to the end of the word, and
    # 2) words that start with a consonant have all their consonant letters
    # up to the first vowel moved to the end of the word, and '-ay' is appended.
    # Hence you might want to look for "-way" or "-ay" word endings.
    vowels = ('a','e','i','o','u')
    latin_word = latin_word.lower()
    english_word = ""
    piglatin_parts = latin_word.split('-')
    if 'way' in piglatin_parts[1][-3:]:
        english_word = piglatin_parts[0]
    else:
        english_word = piglatin_parts[1][:-2] + piglatin_parts[0]
    return english_word

#split sentence into words and call to_english for each word
def translateToenglish(piglatin):
    # This method handles converting entire phrases or sentences from Pig Latin
    # back into English. It takes an Pig Latin character string as its input
    # ('piglatin') and returns the string translated into English. Use the English
    # word converter above: to_english().
    # This method should look a lot like translateTopiglatin().
    piglatin_words = piglatin.split(" ")
    english_sentence = ""
    for word in piglatin_words:
        english_sentence += to_english(word)
        english_sentence += " "
    return english_sentence.strip().capitalize()
"""
Kata Simple Pig Latin lvl5
Move the first letter of each word to the end of it, then add "ay" to the end of the word.
Leave punctuation marks untouched.

EXAMPLES:
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !
"""

#Word per word translator, if no punctuation park is detected, do ya thing
#if there is a single puntuation mark as input, do nothing
#else (there are some characters and then a punctuation mark),
#save it, call yourself again and append the mark at the end (recursion)
#regex could do this more efficiently and without recursion
#but I can't be bothered
def wordmapper(word):
    if word.isalpha():
        wordl = list(word)
        letter = wordl.pop(0)
        wordl.extend((letter, "a", "y"))
        return "".join(wordl)
    elif len(word) == 1:
        return word
    else:
        mark = list(word).pop()
        return wordmapper(word) + mark

#Driver Function
def pig_it(text):
    textl = text.split()
    return " ".join(list(map(wordmapper, textl)))
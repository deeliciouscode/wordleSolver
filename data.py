# Get word lists (from different sources)

import os


def load_wordles():
    words = []
    with open("./words/wordle5.txt") as file:
        for line in file:
            words.append(line.strip().lower())

    return words

def load_words():
    words = []
    with open("./words/allwords.txt") as file:
        for line in file:
            words.append(line.strip().lower())
            
    return sorted(list(set(words)))

def clean(words, n=5):
    cleansed = []
    for word in words: 
        if " " in word:
            pass
        if len(word) != n:
            pass
        else:
            cleansed.append(word)
    return cleansed

def get_words(n=5):
    if n == 5:
        _words = load_wordles()
    else:
        _words = load_words()
        _words = clean(_words, n=n)
    return _words


# manipulate database of words
# add stuff
def add_to_wordles(word):
    with open("./words/wordle5.txt", "a") as file:
        file.write("\n" + word)

def add_to_words(word):
    with open("./words/allwords.txt", "a") as file:
        file.write("\n" + word)

def add_word(word, n):
    if len(word) != n:
        raise ValueError("Length of word and n have to be the same. Default for n is 5.")
    if n == 5:
        add_to_wordles(word)
    else:
        add_to_words(word)


# TODO: variable not just for 5 letter length
def delete_word(word, n):
    if n != 5: # temporary
        return 

    words = []
    with open("./words/wordle5.txt", "r") as file:
        for line in file:
            words.append(line.strip().lower())

    words = sorted(list(set(words) - set([word])))

    with open("./words/wordle5_tmp.txt", "w") as file:
        for word in words:    
            file.write(word + "\n")

    os.remove("./words/wordle5.txt")
    os.rename("./words/wordle5_tmp.txt", "./words/wordle5.txt")
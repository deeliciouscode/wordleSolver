import pandas as pd 
import string
from PyInquirer import prompt
from examples import custom_style_2
import random
import argparse
from questions import from_base, yes_no, how_masked
from data import get_words

parser = argparse.ArgumentParser()
parser.add_argument('-n', '--length', help='lenght of the word.')
parser.add_argument('--base', help='word from which to start e.g.: river')
parser.add_argument('--mask', help='mask from which to start e.g.:: GBGOB')
parser.add_argument('--blacked', help='blacked out characters with which to start e.g.:: pertalde')
args = parser.parse_args()

def try_till_accepted(words):
    try:
        i = random.randint(0, len(words) - 1)
        word = words[i]
        print("Let's try the following word:", words[i])
        answers = prompt(yes_no, style=custom_style_2)
        accepted = answers.get("accepted")
        if accepted == "yes":
            answers = prompt(how_masked, style=custom_style_2)
            mask = answers.get("mask").upper()
            return (words, word, mask)
        elif accepted == "no":
            # exclude not accepted word
            words = words[:i] + words[i+1:]
            return try_till_accepted(words)
    except:
        print("we have no words left to try...")
        exit(1)


def filter_possible_words(words, word, mask, blacked=None):
    possible_words = []

    if blacked is None:
        cant_contain = []
    else:
        cant_contain = list(blacked)
    letters_anywhere_but = {}
    letters_specific = {}
    for i in range(len(mask)):
        if mask[i] == "G":
            letters_specific[i] = word[i]
        elif mask[i] == "O":
            letters_anywhere_but[i] = word[i]
        if mask[i] == "B":
            cant_contain.append(word[i])
    
    cant_contain = list(  set(cant_contain) 
                        - set(list(letters_anywhere_but.values())) 
                        - set(list(letters_specific.values())))

    print("cant_contain:", cant_contain)
    print("letters_anywhere_but:", letters_anywhere_but)
    print("letters_specific:", letters_specific)

    def contains_blocked(_word):
        for letter in cant_contain:
            if letter in _word:
                return True
        return False

    def necessary_letters_included(_word):
        for letter in letters_anywhere_but.values():
            if letter not in _word:
                return False
        return True

    def has_letters_in_ruled_out_location(_word):
        for index, letter in letters_anywhere_but.items():
            if _word[index] == letter:
                return True
        return False

    def specific_letters_correct(_word):
        for index, letter in letters_specific.items():
            if _word[index] != letter:
                return False
        return True

    for _word in words:
        if _word == word:
            print("catched at _word == word:", _word, word)
            continue
        elif not specific_letters_correct(_word):
            print("catched at not specific_letters_correct:", _word)
            continue
        elif not necessary_letters_included(_word): 
            print("catched at not necessary_letters_included:", _word)
            continue
        elif has_letters_in_ruled_out_location(_word):
            print("catched at has_letters_in_ruled_out_location:", _word)
            continue
        elif contains_blocked(_word):
            print("catched at contains_blocked:", _word)
            continue
        else:
            possible_words.append(_word)

    return possible_words

def play_game(words, n, word=None, mask=None, blacked=None):
    if word is None:
        (words, word, mask) = try_till_accepted(words)
    if mask == "G" * n:
        print("Winner, Winner, Chicken Dinner!")
        print("The word was:", word)
        exit(1)
    else:
        possible_words = filter_possible_words(words, word, mask, blacked=blacked)
        play_game(possible_words, n)

def main():
    _n = args.length
    if _n is not None:
        _n = int(_n)
    else:
        _n = 5 

    words = get_words(n=_n)

    if args.base is not None:
        _word = args.base.lower()
        _mask = args.mask
        if _mask is not None:
            _mask = _mask.upper()
        _blacked = args.blacked
        if _blacked is not None:
            _blacked = _blacked.lower()
        play_game(words, _n, word=_word, mask=_mask, blacked=_blacked)
    else:
        play_game(words, _n)

if __name__ == "__main__":
    main()
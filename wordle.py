from PyInquirer import prompt
from examples import custom_style_2
import random
import argparse
from questions import yes_no, how_masked
from data import get_words, add_word, delete_word

parser = argparse.ArgumentParser()
parser.add_argument('-n', '--length', help='Lenght of the word.')
parser.add_argument('--add', help='Add word to wordlist.')
parser.add_argument('--delete', help='Delete word from wordlist. Mutually exclusive with --add.')
parser.add_argument('--base', help='Word from which to start e.g.: river')
parser.add_argument('--mask', help='Mask from which to start e.g.:: GBGOB')
parser.add_argument('--blacked', help='Blacked out characters with which to start e.g.:: pertalde')
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
            # remove from words file and exclude not accepted word from current scope
            delete_word(word, len(word))
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
    
    # TODO: deal with letters that are contained and green but there is 
    # no second occurence. Some words should be excluded that are not right now

    print("cant_contain:", cant_contain)
    print("letters_anywhere_but:", letters_anywhere_but)
    print("letters_specific:", letters_specific)

    cant_contain = list(  set(cant_contain) 
                        - set(list(letters_anywhere_but.values())) 
                        - set(list(letters_specific.values())))

    print("############# after #############")
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
            # print("catched at _word == word:", _word, word)
            continue
        elif not specific_letters_correct(_word):
            # print("catched at not specific_letters_correct:", _word)
            continue
        elif not necessary_letters_included(_word): 
            # print("catched at not necessary_letters_included:", _word)
            continue
        elif has_letters_in_ruled_out_location(_word):
            # print("catched at has_letters_in_ruled_out_location:", _word)
            continue
        elif contains_blocked(_word):
            # print("catched at contains_blocked:", _word)
            continue
        else:
            possible_words.append(_word)

    if len(possible_words) < 10:
        print("There are only few options left:", possible_words) 
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

    is_add = args.add is not None 
    is_delete = args.delete is not None

    if is_add and is_delete:
        raise ValueError("--add and --delete are mutually exclusive")

    if is_add:
        add_word(args.add.lower(), _n)
        print("added to wordlist.")
        exit(1)

    if is_delete:
        delete_word(args.delete.lower(), _n)
        print("deleted from wordlist.")
        exit(1)

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
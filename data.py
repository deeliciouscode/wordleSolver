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

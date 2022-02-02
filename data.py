words = []

with open("./words/allwords.txt") as file:
    for line in file:
        words.append(line.strip().lower())

words = sorted(list(set(words)))

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
    _words = clean(words, n=n)
    return _words

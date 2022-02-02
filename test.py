from wordle import filter_possible_words

# need to define actual tests, this was just for manually debugging
def test_filter_possible_words():
    words = ["towdr", "towdi", "towed", "towel", "tower", "trote"]
    word = "emote"
    mask = "OBOOB"
    blacked = "argsvxn"
    possible_words = filter_possible_words(words, word, mask, blacked=None)
    print(possible_words)

test_filter_possible_words()
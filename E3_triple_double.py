# Think Python 2nd Edition book_Ch9.Word play_p88

# Exercise 9.7. This question is based on a Puzzler that was broadcast on the radio program Car Talk:

    # Give me a word with three consecutive double letters. I’ll give you a couple of words
    # that almost qualify, but don’t. For example, the word committee, c-o-m-m-i-t-t-e-e. It
    # would be great except for the ‘i’ that sneaks in there. Or Mississippi: M-i-s-s-i-s-s-ip-
    # p-i. If you could take out those i’s it would work. But there is a word that has three
    # consecutive pairs of letters and to the best of my knowledge this may be the only word.
    # Of course there are probably 500 more but I can only think of one. What is the word?

# Write a program to find it.

def check_single_word(word):
    length = len(word)
    if length < 6:
        return False
    i = 0
    while i <= length - 6:
        if word[i] == word[i + 1] and word[i + 2] == word[i + 3] and word[i + 4] == word[i + 5]:
            return word
        i += 1

def check_word_list(word_list):
    with open(word_list) as f:
        for line in f:
            word = line.strip()
            if check_single_word(word):
                print(word)

check_word_list("words.txt")
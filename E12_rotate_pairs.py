# Think Python 2nd Edition book_Ch11.Dictionaries_p113

# Exercise 11.5. Two words are “rotate pairs” if you can rotate one of them and get the other (see
# rotate_word in Exercise 8.5).

# Write a program that reads a wordlist and finds all the rotate pairs.


from E7_in_bisect import convert_to_list


def rotate_letter(letter, n):
    # return the letter after rotating the input letter by n places
    # if input is not lowercase or uppercase letter, return the input character
    if letter.islower():
        start = ord("a")
    elif letter.isupper():
        start = ord("A")
    else:
        return letter
    c = (ord(letter) - start + n) % 26
    return chr(c + start)


def rotate_word(word, n):
    res = ""
    for i in word:
        res += rotate_letter(i, n)
    return res


def wordlist_to_dict(word_list):
    # store words as keys in a dictionary, search words using in operator
    # it is much faster than bisect method
    d = {}
    for word in word_list:
        d.setdefault(word)
    return d


def in_dict_key(word, d):
    # search a word and return true if the word is in the dictionary
    if word in d:
        return True
    return False
    


def rotate_pairs(word_list):
    # return all rotate pairs in a word list
    d = wordlist_to_dict(word_list)
    t = []
    for word in d:
        # rotate each word by 1 to 13 places
        # 13 places can cover all 26 alphabets, prevent duplicates except when word is rotated by 13 places
        for i in range(1, 14):
            res = rotate_word(word, i)
            if in_dict_key(res, d):
                # remove duplicates
                if [res, word] not in t:
                    t.append([word, res])
    return t


if __name__ == "__main__":

    t = convert_to_list("words.txt")
    print(rotate_pairs(t))
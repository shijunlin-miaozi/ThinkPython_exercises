# Think Python 2nd Edition book_Ch11.Dictionaries_p113

# Exercise 11.2. Read the documentation of the dictionary method setdefault and use it to write a
# more concise version of invert_dict.


# regular version:

def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse


#  concise version:

def invert_dict_setdefault(d):
    inverse = dict()
    for key in d:
        val = d[key]
        inverse.setdefault(val, []).append(key)
    return inverse


if __name__ == "__main__":

    # create a dictionary as an example
    d = dict()
    word = "bananas"
    for i in word:
        d[i] = d.setdefault(i, 0) + 1
    print(d)

    # invert the dictionary
    print(invert_dict(d))
    print(invert_dict_setdefault(d))


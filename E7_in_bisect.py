# Think Python 2nd Edition book_Ch10.Lists_p101

# Exercise 10.10. To check whether a word is in the word list, you could use the in operator, but it
# would be slow because it searches through the words in order.

# Because the words are in alphabetical order, we can speed things up with a bisection search (also
# known as binary search), which is similar to what you do when you look a word up in the dictionary
# (the book, not the data structure). You start in the middle and check to see whether the word you are
# looking for comes before the word in the middle of the list. If so, you search the first half of the list
# the same way. Otherwise you search the second half.

# Either way, you cut the remaining search space in half. If the word list has 113,809 words, it will
# take about 17 steps to find the word or conclude that it’s not there.
# 
# Write a function called in_bisect that takes a sorted list and a target value and returns the index of the 
# value in the list if it's there, or None if it's not.

def convert_to_list(file):
    # convert data into a list
    t = []
    with open(file) as f:
        for line in f:
            word = line.strip()
            t.append(word)
    return t


def find_subset(word_list, target):
    # bisect the list, check wehther the reference word is target word, if so return True
    # otherwise return first half or second half of the list and how much index will shift to get to the next reference word
    # if word list is empty, then target word is not found, return False
    if len(word_list) == 0:
        return [False, 0]
    i = len(word_list) // 2
    if word_list[i] == target:
        return [True, 0]
    if word_list[i] < target:
        t = word_list[(i + 1) :]
        return [t, len(t) // 2 + 1]
    else:
        t = word_list[: i]
        return [t, -len(t) // 2]


def in_bisect_index(word_list, target):
    # loop thru find_subset function until True or False result
    # track index of the word in original list, return index if True
    start = len(word_list) // 2
    [t, i] = find_subset(word_list, target)
    index = start + i
    if t == True:
        return index
    while isinstance(t, list):
        [t, i] = find_subset(t, target)
        index += i
        if t == True:
            return index
        if t == False:
            return None

if __name__ == '__main__':
    sorted_t = convert_to_list("words.txt")
    for i in ["zz", "xx", "yy", "mom", "aa", "longshoremen", "zymurgy"]:
        print(in_bisect_index(sorted_t, i))



# Alternatively, if index is not required (i.e only need to find out whether the target is in the list or not)
# the code is simper:

def in_bisect(word_list, target):
    if len(word_list) == 0:
        return False
    i = len(word_list) // 2
    if word_list[i] == target:
        return True
    elif word_list[i] < target:
        return in_bisect(word_list[(i + 1) :], target)
    else:
        return in_bisect(word_list[: i], target)



# Or there is in-built bisect function from module bisect
# Think Python 2nd Edition book_Ch11.Dictionaries_p113

# Exercise 11.4. If you did Exercise 10.7, you already have a function named has_duplicates that
# takes a list as a parameter and returns True if there is any object that appears more than once in the list.
# Use a dictionary to write a faster, simpler version of has_duplicates.

# Exercise 10.7. Write a function called has_duplicates that takes a list and returns True if there
# is any element that appears more than once. It should not modify the original list.


# below are 3 different methods to test duplicates in a list, in order of increased simplicity:

def has_duplicates_list(t):
    s = t
    s.sort()
    i = 0
    while i < len(s) - 1:
        if s[i] == s[i + 1]:
            return True
        i += 1
    return False


def has_duplicates_dict(t):
    d = dict()
    for i in t:
        if i in d:
            return True  
        d[i] = 1
    return False


def has_duplicates_set(t):
    return len(set(t)) < len(t)



if __name__ == "__main__":

    t = [0, 0, 1, 2, 3, 4, 5]

    print(has_duplicates_list(t))
    print(has_duplicates_dict(t))
    print(has_duplicates_set(t))

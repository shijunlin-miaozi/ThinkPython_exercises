# Think Python 2nd Edition book_Ch10.Lists_p101

# Exercise 10.11. Two words are a “reverse pair” if each is the reverse of the other. Write a program
# that finds all the reverse pairs in the word list.


from E7_in_bisect import in_bisect, convert_to_list


def reverse_pair(word_list):
    t = []
    for word in word_list:
        reverse = word[::-1]
        if in_bisect(word_list, reverse):
            # exclude palindromic words (e.g "aa")
            if reverse != word:
                t.append([word, reverse])
                # remove reverse pair duplicate
                word_list.remove(reverse)
    return t


if __name__ == '__main__':
    t = convert_to_list("words.txt")
    print(reverse_pair(t))

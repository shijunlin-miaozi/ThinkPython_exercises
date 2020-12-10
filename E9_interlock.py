# Think Python 2nd Edition book_Ch10.Lists_p101

# Exercise 10.12. Two words “interlock” if taking alternating letters from each forms a new
# word. For example, “shoe” and “cold” interlock to form “schooled”.

# 1. Write a program that finds all pairs of words that interlock. Hint: don’t enumerate all pairs!

# 2. Can you find any words that are three-way interlocked; that is, every third letter forms a
# word, starting from the first, second or third?


from E7_in_bisect import in_bisect_module, convert_to_list


def interlock_2(word_list):
    t = []
    for word in word_list:
        # break down the word into 2 words
        wd1 = word[::2]
        wd2 = word[1::2]
        if in_bisect_module(word_list, wd1):
            if in_bisect_module(word_list, wd2):
                t.append(word)
    return t


def break_word(word, n):
    # break word into n sub-words
    t = []
    for i in range(n):
        sub_wd = word[i::n]
        t.append(sub_wd)
    return t


def interlock_3(word_list):
    t = []
    for word in word_list:
        if len(word) > 5:
            [wd1, wd2, wd3] = break_word(word, 3)
            if in_bisect_module(word_list, wd1):
                if in_bisect_module(word_list, wd2):
                    if in_bisect_module(word_list, wd3):
                        t.append(word)
    return t


if __name__ == '__main__':
    t = convert_to_list("words.txt")
    print(interlock_2(t))
    print(interlock_3(t))

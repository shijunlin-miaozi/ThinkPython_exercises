# Think Python 2nd Edition book_Ch10.Lists_p101

# Exercise 10.8. This exercise pertains to the so-called Birthday Paradox, which you can read about at http: // en. wikipedia. org/ wiki/ Birthday_ paradox .
    # If there are 23 students in your class, what are the chances that two of you have the same birthday?
    # You can estimate this probability by generating random samples of 23 birthdays and checking for
    # matches. Hint: you can generate random birthdays with the randint function in the random module.


import random

def check_for_match(list_data):
    # compare all possible pairs of num in the list, return True if any pair has same num
    # loop thru each element in the list (i), compare it to each element that come after in the list(j)
    length = len(list_data)
    for i in range(length - 1):
        j = i + 1
        while j < length:
            if list_data[i] == list_data[j]:
                return True
            j += 1

def calc_probability(group_size, sample_size):
    # generate list of random birthdays based on group size given, check whether there is duplicate in the list
    # run it multiple times based on sample size to calculate the probablity of having duplicate
    match = 0
    for i in range(sample_size):
        t = []
        for j in range(group_size):
            t.append(random.randint(1, 365))
        if check_for_match(t):
            match += 1
    return match / sample_size

print(calc_probability(23, 10000))
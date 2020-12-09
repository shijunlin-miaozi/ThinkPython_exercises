# Think Python 2nd Edition book_Ch9.Word play_p88

# Exercise 9.9. Here’s another Car Talk Puzzler you can solve with a search (http: // www.cartalk. com/ content/ puzzlers ):

    # “Recently I had a visit with my mom and we realized that the two digits that make
    # up my age when reversed resulted in her age. For example, if she’s 73, I’m 37. We
    # wondered how often this has happened over the years but we got sidetracked with other
    # topics and we never came up with an answer.
    # “When I got home I figured out that the digits of our ages have been reversible six times
    # so far. I also figured out that if we’re lucky it would happen again in a few years, and
    # if we’re really lucky it would happen one more time after that. In other words, it would
    # have happened 8 times over all. So the question is, how old am I now?”
    
# Write a Python program that searches for solutions to this Puzzler. Hint: you might find the string method zfill useful.


def is_reversed_age(kid_age, mom_age):
    # to check whether kid's age and mom's age are reverse of each other
    if str(kid_age).zfill(2) == str(mom_age).zfill(2)[::-1]:
        return True

def find_age_pair (frequency):
    # assume mom gave birth between age 15 and 80 (age difference 15 to 80)
    # for each age difference check in kid's lifetime (assume up to 100) how many times their ages are reverse of each other
    # return age difference when 8 times reversed age pair happened
    i = 0
    age_diff = 15
    while age_diff < 80:
        for kid_age in range(100):
            mom_age = kid_age + age_diff
            if is_reversed_age(kid_age, mom_age):
                i += 1
                if i == frequency:
                    print("age difference is ", age_diff)
        age_diff += 1

find_age_pair(8)
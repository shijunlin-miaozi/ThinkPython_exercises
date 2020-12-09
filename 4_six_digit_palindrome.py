# Think Python 2nd Edition book_Ch9.Word play_p88

# Exercise 9.8. Here’s another Car Talk Puzzler (http: // www. cartalk. com/ content/puzzlers ):

    # “I was driving on the highway the other day and I happened to notice my odometer.
    # Like most odometers, it shows six digits, in whole miles only. So, if my car had 300,000
    # miles, for example, I’d see 3-0-0-0-0-0.
    # “Now, what I saw that day was very interesting. I noticed that the last 4 digits were
    # palindromic; that is, they read the same forward as backward. For example, 5-4-4-5 is a
    # palindrome, so my odometer could have read 3-1-5-4-4-5.
    # “One mile later, the last 5 numbers were palindromic. For example, it could have read
    # 3-6-5-4-5-6. One mile after that, the middle 4 out of 6 numbers were palindromic. And
    # you ready for this? One mile later, all 6 were palindromic!
    # “The question is, what was on the odometer when I first looked?”
    
# Write a Python program that tests all the six-digit numbers and prints any numbers that satisfy these requirements.

def six_digit_palindrome():
# consider all 3-digit num and add it's revered 3-digit num to it, forming all palindromic 6-digit num
# return results in a list
    t = []
    i = 100
    while i < 1000:
        six_digit = int(str(i) + str(i)[::-1])
        t.append(six_digit)
        i += 1
    return t

print(six_digit_palindrome())
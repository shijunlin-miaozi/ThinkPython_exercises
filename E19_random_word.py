# Think Python 2nd Edition book_Ch13.data structure selection_p126

# # Exercise 13.5. Write a function named choose_from_hist that takes a histogram as defined in
# Section 11.2 and returns a random value from the histogram, chosen with probability in proportion
# to frequency. For example, for this histogram:
# >>> t = ['a', 'a', 'b']
# >>> hist = histogram(t)
# >>> hist
# {'a': 2, 'b': 1}
# To choose an element from a sequence at random, you can use choice:
# >>> t = [1, 2, 3]
# >>> random.choice(t)
# 2
# >>> random.choice(t)
# 3
# your function should return 'a' with probability 2/3 and 'b' with probability 1/3.

import random
from bisect import bisect
from E18_word_freq import book_to_word_hist

def make_histogram(word):
	hist = {}
	for letter in word:
		hist[letter] = hist.setdefault(letter, 0) + 1
	return hist

def choose_from_hist(hist):
	letter_list = []
	for letter, freq in hist.items():
		letter_list.extend(letter * freq)
	return random.choice(letter_list)


''' above method is ok for analyzing letter histogram from words (short length). It will be very expensive 
if to analyze word histogram from a book (need to make list containing e.g. > 120k words). below is an alternative
using cummulative sum of freq to keep list length to num of unique words (e.g. < 7k)'''


def random_word(hist):
	words = list(hist.keys())
	cum_freqs = [hist[words[0]]]
	for i in range(1, len(words)):
		cum_freqs.append(hist[words[i]] + cum_freqs[i - 1])
	index = bisect(cum_freqs, random.randint(0, cum_freqs[-1] - 1))
	return words[index]


if __name__ == '__main__':

	hist = make_histogram('apple')
	print(choose_from_hist(hist))

	hist_austen = book_to_word_hist('Pride_and_Prejudice_by_Jane_Austen.txt', 167)
	print(random_word(hist_austen))
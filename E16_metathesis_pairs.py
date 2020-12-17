# Think Python 2nd Edition book_Ch12.Tuples_p123

# Exercise 12.3. Two words form a “metathesis pair” if you can transform one into the other by
# swapping two letters; for example, “converse” and “conserve”. Write a program that finds all of
# the metathesis pairs in the dictionary. Hint: don’t test all pairs of words, and don’t test all possible
# swaps.

from E7_in_bisect import convert_to_list
from E12_rotate_pairs import wordlist_to_dict
from E15_anagrams import find_anagrams


def count_diff(wd1, wd2):
	# compare 2 words with same length, return num of differences at each index position
	if len(wd1) != len(wd2):
		return False
	ctr = 0
	for x, y in zip(wd1, wd2):
		if x != y:
			ctr += 1
	return ctr


def metathesis_pairs(anagram_list):
	# loop thru anagram list, compare any two words and check whether they are metathesis pair
	# return list of tuples containing metathesis pairs
	lt = []
	for i in anagram_list:
		for wd1 in i[1]:
			for wd2 in i[1]:
				if count_diff(wd1, wd2) == 2 and wd1 < wd2:
					lt.append((wd1, wd2))
	return lt


if __name__ == '__main__':

	t = convert_to_list("words.txt")
	word_dict = wordlist_to_dict(t)
	lt = find_anagrams(word_dict)
	print(metathesis_pairs(lt))
	
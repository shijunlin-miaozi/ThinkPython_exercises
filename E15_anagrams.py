# Think Python 2nd Edition book_Ch12.Tuples_p123

# Exercise 12.2. More anagrams!

# 1. Write a program that reads a word list from a file (see Section 9.1) and prints all the sets of
# words that are anagrams.

# Here is an example of what the output might look like:
	# ['deltas', 'desalt', 'lasted', 'salted', 'slated', 'staled']
	# ['retainers', 'ternaries']
	# ['generating', 'greatening']
	# ['resmelts', 'smelters', 'termless']

# Hint: you might want to build a dictionary that maps from a collection of letters to a list
# of words that can be spelled with those letters. The question is, how can you represent the
# collection of letters in a way that can be used as a key?

# 2. Modify the previous program so that it prints the longest list of anagrams first, followed by
# the second longest, and so on.

# 3. In Scrabble a “bingo” is when you play all seven tiles in your rack, along with a letter on
# the board, to form an eight-letter word. What collection of 8 letters forms the most possible
# bingos?


from E7_in_bisect import convert_to_list
from E12_rotate_pairs import wordlist_to_dict


def histogram(s):
	# return a tuple containing frequency of each letter in a string; tuple is in ascending alphabetical order
	d = {}
	for i in s:
		d[i] = d.setdefault(i, 0) + 1
	lt = []
	for letter, freq in d.items():
		lt.append((letter, freq))
	lt.sort()
	return tuple(lt)


def find_anagrams(word_dict):
	# find histogram of each word in word dict to form key in a dict that maps each histogram to list of words with same histogram (anagrams)
	# return list (in descending num of anagrams order ) of tuples containing num of anagrams, list of nangrams and histogram
	d = {}
	for word in word_dict:
		h = histogram(word)
		d[h] = d.setdefault(h, []) + [word]
	lt = []
	for h in d:
		if len(d[h]) > 1:
			lt.append((len(d[h]), d[h], h))
	lt.sort(reverse=True)
	return lt


if __name__ == '__main__':

	t = convert_to_list("words.txt")
	word_dict = wordlist_to_dict(t)
	lt = find_anagrams(word_dict)
	
	# print list of anagrams in descending order (longest to shortest)
	for i in lt:
		print(i)
	
	# print collection of 8 letters that forms the most possible bingos:
	
	# find list of anagrams that are formed by 8 letters
	res = []
	for i in lt:
		lh = 0
		for j in i[2]:
			lh += j[1]
			if lh == 8:
				res.append(i)

	t = []
	for i in res[0][2]:
		t.append(i[0])
	print("8 letters are ", t)

	print("the most possible bingos are:")
	for i in res[0][1]:
		print(i)
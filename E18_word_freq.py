
# >>>>>>>>>>>>>>>>>>>>>>>> WORK IN PROGRESS >>>>>>>>>>>>>>>>>>>>>>>>>>

# Think Python 2nd Edition book_Ch13.data structure selection_p125

# Exercise 13.1. Write a program that reads a file, breaks each line into words, strips whitespace and
# punctuation from the words, and converts them to lowercase.
# Hint: The string module provides a string named whitespace, which contains space, tab, newline,
# etc., and punctuation which contains the punctuation characters. Let’s see if we can make Python swear:
# >>> import string
# >>> string.punctuation
# '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
# Also, you might consider using the string methods strip, replace and translate.

# Exercise 13.2. Go to Project Gutenberg (http: // gutenberg. org ) and download your favorite
# out-of-copyright book in plain text format.
# Modify your program from the previous exercise to read the book you downloaded, skip over the
# header information at the beginning of the file, and process the rest of the words as before.
# Then modify the program to count the total number of words in the book, and the number of times
# each word is used.
# Print the number of different words used in the book. Compare different books by different authors,
# written in different eras. Which author uses the most extensive vocabulary?

# Exercise 13.3. Modify the program from the previous exercise to print the 20 most frequently used
# words in the book.

# Exercise 13.4. Modify the previous program to read a word list (see Section 9.1) and then print all
# the words in the book that are not in the word list. How many of them are typos? How many of
# them are common words that should be in the word list, and how many of them are really obscure?

import string

def book_to_word_dict(filename):
	whitespace = string.whitespace.replace(' ', '')
	punctuation = string.punctuation
	translation = str.maketrans('', '', whitespace + punctuation + '“”') 
	d = {}
	with open (filename) as f:
		for line in f:
			lt = line.translate(translation).strip().lower().split()
			for word in lt:
				d[word] = d.setdefault(word, 0) + 1
	return d


def sort_word_dict(d):
	lt = []
	for word, freq in d.items():
		lt.append((freq, word))
	lt.sort(reverse=True)
	return lt

	
if __name__ == '__main__':

	# import time
	# start_time = time.time()
	# print('---xx %.2fs seconds ---' % (time.time() - start_time))

	d = book_to_word_dict('temp.txt')
	lt = sort_word_dict(d)
	print(len(d))
	print(len(lt))


# >>>>>>>>>>>>>>>>>>>>>>>> WORK IN PROGRESS >>>>>>>>>>>>>>>>>>>>>>>>>>
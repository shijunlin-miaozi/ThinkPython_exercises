
# >>>>>>>>>>>>>>>>>>>>>>>> WORK IN PROGRESS >>>>>>>>>>>>>>>>>>>>>>>>>>

# Think Python 2nd Edition book_Ch13.data structure selection_p125

# Exercise 13.1. 
# Write a program that reads a file, breaks each line into words, strips whitespace and
# punctuation from the words, and converts them to lowercase.
# Hint: The string module provides a string named whitespace, which contains space, tab, newline,
# etc., and punctuation which contains the punctuation characters. Let’s see if we can make Python swear:
# >>> import string
# >>> string.punctuation
# '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
# Also, you might consider using the string methods strip, replace and translate.

# Exercise 13.2. 
# Go to Project Gutenberg (http: // gutenberg. org ) and download your favorite
# out-of-copyright book in plain text format.
# Modify your program from the previous exercise to read the book you downloaded, skip over the
# header information at the beginning of the file, and process the rest of the words as before.
# Then modify the program to count the total number of words in the book, and the number of times
# each word is used.
# Print the number of different words used in the book. Compare different books by different authors,
# written in different eras. Which author uses the most extensive vocabulary?

# Exercise 13.3. 
# Modify the program from the previous exercise to print the 20 most frequently used
# words in the book.

# Exercise 13.4. 
# Modify the previous program to read a word list (see Section 9.1) and then print all
# the words in the book that are not in the word list. How many of them are typos? How many of
# them are common words that should be in the word list, and how many of them are really obscure?

import string

def book_to_word_dict(filename, start_line=1): # start_line used to skip header info (line num as in txt file), otherwise it reads file from beginning
	whitespace = string.whitespace.replace(' ', '') # remove ' '(space) as it neeeds to stay to split line into words
	punctuation = string.punctuation
	trans_table = str.maketrans('', '', whitespace + punctuation + '“”') 
	d, end_line = {}, float('inf')
	with open (filename) as f:
		for index, line in enumerate(f):
			if 'End of the Project Gutenberg EBook' in line:
				end_line = index
			if start_line - 1 <= index < end_line:
				clean_line = line.translate(trans_table).lower().split()
				for word in clean_line:
					if not word.isdigit():
						d[word] = d.setdefault(word, 0) + 1
	return d


if __name__ == '__main__':

	d = book_to_word_dict('Pride_and_Prejudice_by_Jane_Austen.txt', 167)
	print(len(d))

	sorted_word_list = sorted([(freq, word) for word, freq in d.items()], reverse=True)
	for i in range(20):
		print(sorted_word_list[i][1])


# >>>>>>>>>>>>>>>>>>>>>>>> WORK IN PROGRESS >>>>>>>>>>>>>>>>>>>>>>>>>>
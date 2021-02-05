
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

def book_to_word_hist(filename, start_line=1): # start_line used to skip header info (line num as in txt file), otherwise it reads file from beginning
	hist = {}
	with open (filename) as f:
		for index, line in enumerate(f):
			if line.startswith('End of the Project Gutenberg EBook'):
				break
			if start_line - 1 <= index:
				for word in line.replace('—', ' ').split():
					clean_word = word.strip(string.whitespace + string.punctuation + '“”‘’').lower()
					if not clean_word.isdigit():
						hist[clean_word] = hist.setdefault(clean_word, 0) + 1
	return hist


if __name__ == '__main__':

	d_austen = book_to_word_hist('Pride_and_Prejudice_by_Jane_Austen.txt', 167)
	print(f"Austen's book:\n  word count: {sum(d_austen.values()): ,}\n  unique words: {len(d_austen): ,}\n")

	d_hardy = book_to_word_hist("Tess_of_the_d'Urbervilles_by_Thomas_Hardy.txt", 291)
	print(f"Hardy's book:\n  word count: {sum(d_hardy.values()): ,}\n  unique words: {len(d_hardy): ,}\n")

	sorted_word_list_austen = sorted(d_austen.items(), key=lambda x: x[1], reverse=True)
	print(f"Top 20 frequently used words in Austen's book: ")
	for i in range(20):
		print(f"{sorted_word_list_austen[i][0]: >8}  {sorted_word_list_austen[i][1]}")

	word_list = set([line.strip() for line in open("words.txt")])
	book_word = set(d_austen.keys())
	book_word_not_in_list = book_word - word_list
	print(f"\nthere are {len(book_word_not_in_list)} words from austen's book are not in wordlist:\n")
	print(book_word_not_in_list)
			
# Think Python 2nd Edition book_Ch12.Tuples_p123

# Exercise 12.1. Write a function called most_frequent that takes a string and prints the letters
# in decreasing order of frequency. Find text samples from several different languages and see
# how letter frequency varies between languages. 
# Compare your results with the tables at http: en. wikipedia. org/ wiki/ Letter_ frequencies.


def most_frequent(s):
	# take a string and return a list of tuples in descending frequency order, each tuple contains frequency and letter
	d = {}
	for i in s:
		d[i] = d.setdefault(i, 0) + 1
	lt = []
	for letter, freq in d.items():
		lt.append((freq, letter))
	lt.sort(reverse = True)
	return lt


if __name__ == '__main__':

	sample_text = "Letter frequency is simply the amount of times letters of the alphabet appear on average in written language. Letter frequency analysis dates back to the Arab mathematician Al-Kindi (c. 801–873 AD), who formally developed the method to break ciphers. Letter frequency analysis gained importance in Europe with the development of movable type in 1450 AD, where one must estimate the amount of type required for each letterform. Linguists use letter frequency analysis as a rudimentary technique for language identification, where it's particularly effective as an indication of whether an unknown writing system is alphabetic, syllabic, or ideographic. The use of letter frequencies and frequency analysis plays a fundamental role in cryptograms and several word puzzle games, including Hangman, Scrabble and the television game show Wheel of Fortune. One of the earliest descriptions in classical literature of applying the knowledge of English letter frequency to solving a cryptogram is found in Edgar Allan Poe's famous story The Gold-Bug, where the method is successfully applied to decipher a message instructing on the whereabouts of a treasure hidden by Captain Kidd.[1] Letter frequencies also have a strong effect on the design of some keyboard layouts. The most frequent letters are on the bottom row of the Blickensderfer typewriter, and the home row of the Dvorak keyboard layout. The frequency of letters in text has been studied for use in cryptanalysis, and frequency analysis in particular, dating back to the Iraqi mathematician Al-Kindi (c. 801–873 AD), who formally developed the method (the ciphers breakable by this technique go back at least to the Caesar cipher invented by Julius Caesar, so this method could have been explored in classical times). Letter frequency analysis gained additional importance in Europe with the development of movable type in 1450 AD, where one must estimate the amount of type required for each letterform, as evidenced by the variations in letter compartment size in typographer's type cases."
	lt = most_frequent(sample_text)
	for i in lt:
		print(i[1])

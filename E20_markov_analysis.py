# Think Python 2nd Edition book_h13.data structure selection_p131

''' 
Exercise 13.8. Markov analysis:

1. Write a program to read a text from a file and perform Markov analysis. The result should be
a dictionary that maps from prefixes to a collection of possible suffixes. The collection might
be a list, tuple, or dictionary; it is up to you to make an appropriate choice. You can test your
program with prefix length two, but you should write the program in a way that makes it easy
to try other lengths.

2. Add a function to the previous program to generate random text based on the Markov analysis.
Here is an example from Emma with prefix length 2:

	He was very clever, be it sweetness or be angry, ashamed or only amused, at such
	a stroke. She had never thought of Hannah till you were never meant for me?" "I
	cannot make speeches, Emma:" he soon cut it all himself.

For this example, I left the punctuation attached to the words. The result is almost syntactically
correct, but not quite. Semantically, it almost makes sense, but not quite.
What happens if you increase the prefix length? Does the random text make more sense?

3. Once your program is working, you might want to try a mash-up: if you combine text from
two or more books, the random text you generate will blend the vocabulary and phrases from
the sources in interesting ways.
'''

import random

def process_file(filename, start_line=1): # start_line used to skip header info (line num as in txt file), otherwise it reads file from beginning
	word_str = ''
	with open (filename) as f:
		for index, line in enumerate(f):
			if line.startswith('End of the Project Gutenberg EBook'):
				break
			if start_line - 1 <= index:
				word_str += line.replace('—', ' ') + ' '
	words = tuple(word_str.split())
	return words


def map_prefix_to_suffix(words, prefix_len):
	d = {}
	for i in range(len(words) - prefix_len):
		d.setdefault(' '.join(words[i : i + prefix_len]), []).append(words[i + prefix_len])
	return d


def create_random_text(words, prefix_len, num_of_sentences):
	ctr, prefix_suffix_mapping = 0, map_prefix_to_suffix(words, prefix_len)
	while True:
		prefix = random.choice(list(prefix_suffix_mapping.keys()))
		if prefix[0].isupper():
			break
	sentences = prefix
	while ctr < num_of_sentences:
		suffix = random.choice(prefix_suffix_mapping[prefix])
		sentences += ' ' + suffix
		if '.' in suffix:
			ctr += 1
		prefix = ' '.join(sentences.split()[- prefix_len:])
	return sentences


if __name__ == '__main__':

	words_austen = process_file('Pride_and_Prejudice_by_Jane_Austen.txt', 167)
	words_hardy = process_file("Tess_of_the_d'Urbervilles_by_Thomas_Hardy.txt", 291)
	combined_words = words_austen + words_hardy

	print(f"Random text from Pride and Prejudice:\n\n{create_random_text(words_austen, 3, 5)}\n\n")
	print(f"Random text from Pride and Prejudice and Tess combined:\n\n{create_random_text(combined_words, 3, 5)}")

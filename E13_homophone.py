# Think Python 2nd Edition book_Ch11.Dictionaries_p113

# Exercise 11.6. Here’s another Puzzler from Car Talk (http: // www. cartalk. com/ content/ puzzlers ):

	# This was sent in by a fellow named Dan O’Leary. He came upon a common one-syllable,
	# five-letter word recently that has the following unique property. When you remove the
	# first letter, the remaining letters form a homophone of the original word, that is a word
	# that sounds exactly the same. Replace the first letter, that is, put it back and remove
	# the second letter and the result is yet another homophone of the original word. And the
	# question is, what’s the word?

	# Now I’m going to give you an example that doesn’t work. Let’s look at the five-letter
	# word, ‘wrack.’ W-R-A-C-K, you know like to ‘wrack with pain.’ If I remove the first
	# letter, I am left with a four-letter word, ’R-A-C-K.’ As in, ‘Holy cow, did you see the
	# rack on that buck! It must have been a nine-pointer!’ It’s a perfect homophone. If you
	# put the ‘w’ back, and remove the ‘r,’ instead, you’re left with the word, ‘wack,’ which is
	# a real word, it’s just not a homophone of the other two words.

	# But there is, however, at least one word that Dan and we know of, which will yield two
	# homophones if you remove either of the first two letters to make two, new four-letter
	# words. The question is, what’s the word?

# To check whether two words are homophones, you can use the CMU Pronouncing Dictionary. You
# can download it from http: // www. speech. cs. cmu. edu/ cgi-bin/ cmudict or from http:
# thinkpython2. com/ code/ c06d and you can also download http: // thinkpython2.com/ code/ pronounce. py , 
# which provides a function named read_dictionary that reads the pronouncing dictionary and returns a Python 
# dictionary that maps from each word to a string that describes its primary pronunciation.

# Write a program that lists all the words that solve the Puzzler.


from E7_in_bisect import convert_to_list
from E12_rotate_pairs import wordlist_to_dict, in_dict_key


def read_dictionary(filename='pron_dict_raw.txt'):
    # Reads from a file and builds a dictionary that maps from string to pronunciation
    d = dict()
    fin = open(filename)
    for line in fin:
        # skip over the comments
        if line[0] == '#': continue
        t = line.split()
        word = t[0].lower()
        pron = ' '.join(t[1:])
        d[word] = pron
    return d


def homophone_word(word, pron_dict, word_dict):
	wd1 = word[1:]
	wd2 = word[0] + word[2:]
	if in_dict_key(wd1, word_dict) and in_dict_key(wd1, word_dict):
		if word in pron_dict and wd1 in pron_dict and wd2 in pron_dict:
			pron = pron_dict[word]
			if pron_dict[wd1] == pron and pron_dict[wd2] == pron:
				return True
	return False



if __name__ == '__main__':

	pron_dict = read_dictionary()
	t = convert_to_list("words.txt")
	word_dict = wordlist_to_dict(t)
	
	for word in word_dict:
		if homophone_word(word, pron_dict, word_dict):
			print(word)




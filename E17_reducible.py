# Think Python 2nd Edition book_Ch12.Tuple_p124

# Exercise 12.4. Here’s another Car Talk Puzzler (http: // www. cartalk. com/ content/puzzlers ):

	# 
	# Now, letters can be removed from either end, or the middle, but you can’t rearrange any
	# you do that, you’re eventually going to wind up with one letter and that too is going
	# to be an English word—one that’s found in the dictionary. I want to know what’s the
	# longest word and how many letters does it have?
	# I’m going to give you a little modest example: Sprite. Ok? You start off with sprite,
	# you take a letter off, one from the interior of the word, take the r away, and we’re left
	# with the word spite, then we take the e off the end, we’re left with spit, we take the s off,
	# we’re left with pit, it, and I.

# Write a program to find all words that can be reduced in this way, and then find the longest one.
# This exercise is a little more challenging than most, so here are some suggestions:

# 1. You might want to write a function that takes a word and computes a list of all the words that
# can be formed by removing one letter. These are the “children” of the word.

# 2. Recursively, a word is reducible if any of its children are reducible. As a base case, you can
# consider the empty string reducible.

# 3. The wordlist I provided, words.txt, doesn’t contain single letter words. So you might want
# to add “I”, “a”, and the empty string.

# 4. To improve the performance of your program, you might want to memoize the words that are
# known to be reducible.


def file_to_dict(file="words.txt"):
    # store words as keys in a dictionary
	d = {}
	with open(file) as f:
		for line in f:
			word = line.strip()
			d.setdefault(word)
	# add these 3 additional items for reducible function to work
	for i in ('a', 'i', ''):
		d.setdefault(i)
	return d


def find_children(word, word_dict):
	# return children of the word in a list
	children = []
	for i in range(len(word)):
		child = word[:i] + word[(i+1):]
		if child in word_dict:
			children.append(child)
	return children


cache = {'': True}

def is_reducible(word, word_dict):
	# return True if a word is reducible (i.e it's children are reducible)
	# use cache to save time
	if word in cache:
		return cache[word]
	children = find_children(word, word_dict)
	# loop thru all children, if any is True, return True, otherwise return False
	for i in children:
		if is_reducible(i, word_dict) == True:
			cache[word] = True
			return True
		else:
			continue
	cache[word] = False
	return False


def all_reducible(word_dict):
	# find all reducible words in a word dictionary
	lt = []
	for word in word_dict:
		if is_reducible(word, word_dict):
			lt.append(word)
	return lt


if __name__ == '__main__':

	d = file_to_dict()

	# print all reducible words in a word dictionary
	lt = all_reducible(d)
	print(lt)


	# print longest reducible word in the dictionary
	res = []
	for word in lt:
		res.append((len(word), word))
	res.sort(reverse=True)
	print('longest reducible word is: ', res[0][1])

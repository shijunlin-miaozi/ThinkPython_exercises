# Think Python 2nd Edition book_Chxx.xx_pxx

'''
Exercise 18.3. The following are the possible hands in poker, in increasing order of value and
decreasing order of probability:

	- pair:             two cards with the same rank
	- two pair:         two pairs of cards with the same rank
	- three of a kind:  three cards with the same rank
	- straight:         five cards with ranks in sequence (aces can be high or low, so Ace-2-3-4-5 is a straight and so is 10-Jack-Queen-King-Ace, but Queen-King-Ace-2-3 is not.)
	- flush:            five cards with the same suit
	- full house:       three cards with one rank, two cards with another
	- four of a kind:   four cards with the same rank
	- straight flush:   five cards in sequence (as defined above) and with the same suit

	The goal of these exercises is to estimate the probability of drawing these various hands.

1. Download the following files from http: // thinkpython2. com/ code :
Card.py : A complete version of the Card, Deck and Hand classes in this chapter.
PokerHand.py : An incomplete implementation of a class that represents a poker hand, and
some code that tests it.

2. If you run PokerHand.py, it deals seven 7-card poker hands and checks to see if any of them
contains a flush. Read this code carefully before you go on.

3. Add methods to PokerHand.py named has_pair, has_twopair, etc. that return True or
False according to whether or not the hand meets the relevant criteria. Your code should
work correctly for “hands” that contain any number of cards (although 5 and 7 are the most
common sizes).

4. Write a method named classify that figures out the highest-value classification for a hand
and sets the label attribute accordingly. For example, a 7-card hand might contain a flush
and a pair; it should be labeled “flush”.

5. When you are convinced that your classification methods are working, the next step is to estimate
the probabilities of the various hands. Write a function in PokerHand.py that shuffles
a deck of cards, divides it into hands, classifies the hands, and counts the number of times
various classifications appear.

6. Print a table of the classifications and their probabilities. Run your program with larger and
larger numbers of hands until the output values converge to a reasonable degree of accuracy.
Compare your results to the values at http: // en. wikipedia. org/ wiki/ Hand_
rankings .
'''

from E22_card import Hand, Deck


class PokerHand(Hand):
    """Represents a poker hand."""

    def make_hist(self):
        """Builds a histogram of the suits, ranks and rank_freq that appear in the hand.
        Stores the result in attribute suits, ranks and rank_freq.
        """
        self.suits, self.ranks, self.rank_freq = {}, {}, []
        for card in self.cards:
            for d, key in zip((self.suits, self.ranks), (card.suit, card.rank)):
                d[key] = d.setdefault(key, 0) + 1
        self.rank_freq = sorted(list(self.ranks.values()), reverse=True)


    def compare_rank_freq(self, *reqs):
        """check whether hand's rank frequencies meet requirements"""
        for req, have in zip(reqs, self.rank_freq):
            if have < req:
                return False
        return True


    def has_pair(self):
        """ two cards with the same rank """
        return self.compare_rank_freq(2)


    def has_2pair(self):
        """ two pairs of cards with the same rank"""
        return self.compare_rank_freq(2, 2)


    def has_3ofakind(self):
        """ three cards with the same rank"""
        return self.compare_rank_freq(3)


    def has_4ofakind(self):
        """ four cards with the same rank"""
        return self.compare_rank_freq(4)


    def has_fullhouse(self):
        """ three cards with one rank, two cards with another"""
        return self.compare_rank_freq(3, 2)


    def has_flush(self):
        """five cards with the same suit
        Returns True if the hand has a flush, False otherwise.      
        Note that this works correctly for hands with more than 5 cards.
        """
        for val in self.suits.values():
            if val >= 5:
                return True
        return False


    def has_straight(self):
        """ five cards with ranks in sequence (aces can be high or low, so Ace-2-3-4-5 is a straight and so is 10-Jack-Queen-King-Ace, but Queen-King-Ace-2-3 is not.)"""
        ctr, uni_rank = 0, self.ranks.keys()
        if len(uni_rank) >= 5:
            if set(uni_rank) >= {10, 11, 12, 13, 1}:
                return True
            for i in range(1, 14):
                if self.ranks.get(i, 0):
                    ctr += 1
                    if ctr == 5:
                        return True
                else:
                    ctr = 0
        return False


    def has_straightflush(self):
        """ five cards in sequence (as defined above) and with the same suit"""
        hand = PokerHand()
        for suit, freq in self.suits.items():
            if freq >= 5:
                for card in self.cards:
                    if card.suit == suit:
                        hand.add_card(card)
                hand.make_hist()
                if hand.has_straight():
                    return True
        return False


    def classify(self):
        labels = ['straightflush', '4ofakind', 'fullhouse', 'flush', 
                    'straight', '3ofakind', '2pair', 'pair'] 
        self.make_hist()
        for label in labels:
            f = getattr(self, 'has_' + label)
            if f():
                self.label = label
                return
            else:
                self.label = None


def calc_probability(deck_num, card_num):
    res = {}
    for i in range(deck_num):
        deck = Deck()
        deck.shuffle()
        hand_num = divmod(52, card_num)[0]
        for i in range(hand_num):
            hand = PokerHand()
            deck.move_cards(hand, card_num)
            hand.sort()
            hand.classify()
            res[hand.label] = res.setdefault(hand.label, 0) + 1
    for key, val in res.items():
        res[key] = val / (deck_num * hand_num)
    return sorted(res.items(), key=lambda x:x[1], reverse=True)


if __name__ == '__main__':

    for card_num in (5, 7):
        res = calc_probability(10000, card_num)

        print(f"probabilities for {card_num}-card poker hands:")
        for label, prob in res:
            print(f"\t{label}\t{prob: .2%}")
        print()
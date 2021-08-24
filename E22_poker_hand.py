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

    def suit_hist(self):
        """Builds a histogram of the suits that appear in the hand.
        Stores the result in attribute suits.
        """
        self.suits = {}
        for card in self.cards:
            self.suits[card.suit] = self.suits.setdefault(card.suit, 0) + 1


    def has_flush(self):
        """five cards with the same suit
        Returns True if the hand has a flush, False otherwise.      
        Note that this works correctly for hands with more than 5 cards.
        """
        self.suit_hist()
        for val in self.suits.values():
            if val >= 5:
                return True
        return False


    def rank_hist(self):
            """Builds a histogram of the ranks that appear in the hand.
            Stores the result in attribute ranks.
            """
            self.ranks = {}
            for card in self.cards:
                self.ranks[card.rank] = self.ranks.setdefault(card.rank, 0) + 1


    def has_pair(self):
        """ two cards with the same rank 
        """
        self.rank_hist()
        for val in self.ranks.values():
            if val >= 2:
                return True
        return False


    def has_2pair(self):
        """ two pairs of cards with the same rank
        """
        self.rank_hist()
        ctr = 0
        for val in self.ranks.values():
            if val >= 2:
                ctr += 1
                if ctr == 2:
                    return True
        return False


    def has_3ofakind(self):
        """ three cards with the same rank
        """
        self.rank_hist()
        for val in self.ranks.values():
            if val >= 3:
                return True
        return False


    def has_straight(self):
        """ five cards with ranks in sequence (aces can be high or low, so Ace-2-3-4-5 is a straight and so is 10-Jack-Queen-King-Ace, but Queen-King-Ace-2-3 is not.)
        """
        self.rank_hist()
        lt = sorted(self.ranks.keys())
        if len(lt) >= 5:
            if set(lt) >= {10, 11, 12, 13, 1}:
                return True
            for i in range(len(lt) - 4):
                if lt[i:i+5] == [lt[i]+n for n in range(5)]:
                    return True
        return False


    def has_fullhouse(self):
        """ three cards with one rank, two cards with another
        """
        self.rank_hist()
        lt = [val for val in self.ranks.values() if val >= 2]
        if len(lt) >= 2 and (3 in lt or 4 in lt):
            return True
        return False


    def has_4ofakind(self):
        """ four cards with the same rank
        """
        self.rank_hist()
        for val in self.ranks.values():
            if val >= 4:
                return True
        return False


    def has_straightflush(self):
        """ five cards in sequence (as defined above) and with the same suit
        """
        self.suit_hist()
        flush = PokerHand()
        for key, val in self.suits.items():
            if val >= 5:
                for card in self.cards:
                    if card.suit == key:
                        flush.add_card(card)
                if flush.has_straight():
                    return True
        return False


    def classify(self):
        res, labels = [], ["pair", "2pair", "3ofakind", "straight", 
                            "flush", "fullhouse", "4ofakind", "straightflush"]
        for value, check in zip((range(8)), 
                            (self.has_pair(), self.has_2pair(), self.has_3ofakind(), self.has_straight(), 
                            self.has_flush(), self.has_fullhouse(), self.has_4ofakind(), self.has_straightflush())):
            if check:
                res.append(value)
        self.label = labels[max(res)] if res else None


def calc_probability(deck_num, card_num):
    res = {}
    for i in range(deck_num):
        deck = Deck()
        deck.shuffle()
        round_num = divmod(52, card_num)[0]
        for i in range(round_num):
            hand = PokerHand()
            deck.move_cards(hand, card_num)
            hand.sort()
            hand.classify()
            res[hand.label] = res.setdefault(hand.label, 0) + 1
    for key, val in res.items():
        res[key] = val / (deck_num * round_num)
    return sorted(res.items(), key=lambda x:x[1], reverse=True)


if __name__ == '__main__':
    for card_num in (5, 7):
        res = calc_probability(10000, card_num)
        print(f"probabilities for {card_num}-card poker hands:")
        for label, prob in res:
            print(f"\t{label}\t{prob: .2%}")
        print()



    # make a deck
    # deck = Deck()
    # deck.shuffle()
    # cards =[Card(1, 13),
    #         Card(1, 12),
    #         Card(1, 11),
    #         Card(1, 10),
    #         Card(1, 1),
    #         Card(2, 10),
    #         Card(3, 4),
    #         ]
    # for card in cards:
        # print(card)
        # deck.add_card(card)

    # deal the cards and classify the hands
    # for i in range(7):
    #     hand = PokerHand()
    #     deck.move_cards(hand, 7)

    #     hand.sort()
    #     print(hand)
    #     print('\t0) has_pair:', hand.has_pair())
    #     print('\t1) has_2pair:', hand.has_2pair())
    #     print('\t2) has_3ofakind:', hand.has_3ofakind())
    #     print('\t3) has_straight:', hand.has_straight())
    #     print('\t4) has_flush:', hand.has_flush())
    #     print('\t5) has_fullhouse:', hand.has_fullhouse())
    #     print('\t6) has_4ofakind:', hand.has_4ofakind())
    #     print('\t7) has_straightflush:', hand.has_straightflush())
    #     print('')

    # hand.classify()
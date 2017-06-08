# build generate the 52 cards
# show prints out all the cards
# shuffle the deck randon
# reset the deck back to  bild stage
# draw method should return the top card from deck
# draw will be used by player
import random
# import shuffle

x = random.randint(0,10)
print x

class Card(object):
    # parent is the object class
    def __init__(self, suite, val):
        self.suite = suite
        self.val = val
    def show(self):
        print "{} of {}".format(self.val, self.suite)
        return self

class Deck(object):
    def __init__(self):
        self.cards = []
        self.build()
    def build(self):
        self.cards = []
        for value in range(1,14):
            self.cards.append( Card("Spade", str(value)) )
            self.cards.append( Card("Club", str(value)) )
            self.cards.append( Card("Diamond", str(value)) )
            self.cards.append( Card("Hearts", str(value)) )
    def show(self):
        for card in self.cards:
            card.show()

    def doShuffle(self):
        # random.shuffle(self.cards)
        random.shuffle(self.cards)
        return self
        # self.cards

# add methods to interact with
# draw from the deck

        # always return self as func by defalut return none

# myCard = Card("Spade", 1)
# myCard.show().build()
# Deck1 = Deck()
# Deck1.build()
myDeck = Deck()
myDeck.doShuffle().show()

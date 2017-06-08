class Card(object):
    # parent is the object class
    """docstring for Deck."""
    def __init__(self, suite, val):
        # duncderscore = 2 double underscore, built in method
        # initialization
        # self every class parameter. this in JS is same as self in python
        # every classs method takes self sa the 1st parameter
        # super(Deck, self).__init__()
        # store it in the instance - parameters
        # self is the instance of the given class that we r calling the method from
        self.suite = suite
        self.val = val
    def show(self):
        print "{} or {}".format(self.val, self.suite)
        return self
class Deck(object):
    """docstring for Deck."""
    def __init__(self, arg):
        super(Deck, self).__init__()
        self.arg = arg
        # build generate the 52 cards
        # show prints out all the cards
        # shuffle the deck randon
        # reset the deck back to  bild stage
        # draw method should return the top card from deck
        # draw will be used by player

class Player(object):
    """docstring for Player."""
    def __init__(self, arg):
        super(Player, self).__init__()
        self.arg = arg
                # add methods to interact with
                # draw from the deck
                
        # always return self as func by defalut return none
# class Player(object):
#     """docstring for Player."""
#     def __init__(self, arg):
#         super(Player, self).__init__()
#         self.arg = arg

myCard = Card("D", 1)
myCard.show()
# print

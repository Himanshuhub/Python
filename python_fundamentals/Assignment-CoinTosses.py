# Assignment: Coin Tosses
from random import randint

def CoinToss():
    print "Starting the program"
    head = 0
    tail = 0
    for i in range(1,5001):
        toss = round(randint(0,1))
        if (toss == 1 and i<5000):
            head = head + 1
            print "Attempt #1: Throwing a coin... It's a head! ... Got "+ str(head)+" head(s) so far and "+str(tail) +" tail(s) so far"
        elif (toss == 0 and i<5000):
            tail = tail + 1
            print "Attempt #1: Throwing a coin... It's a tail! ... Got "+ str(head)+" head(s) so far and "+str(tail) +" tail(s) so far"
        elif (toss == 1 and i == 5000):
            print "Attempt #5000: Throwing a coin... It's a head ! ... Got "+str(head)+" head(s) so far and "+str(tail)+" tail(s) so far Ending the program, thank you!"
        elif (toss == 0 and i == 5000):
            print "Attempt #5000: Throwing a coin... It's a tail ! ... Got "+str(head)+" head(s) so far and "+str(tail)+" tail(s) so far Ending the program, thank you!"

CoinToss()

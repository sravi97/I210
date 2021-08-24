#import random function
from random import randrange
def diceprob(r):
    #initialize rolls and count
    rolls = 0
    count = 0
    #while the count is under 100 run through this loop
    while count < 100:
        roll = randrange(1,7) + randrange(1,7)
        #adds one to the roll
        rolls += 1
        #if the roll is equal to the number we want add one
        if roll == r:
            count += 1
    #print statement
    return ("It took {} to get 100 rolls of {}".format(rolls, r))
print(diceprob(2))
print(diceprob(3))
print(diceprob(4))
print(diceprob(5))
print(diceprob(6))
print(diceprob(7))


    

import cards

# this function creates num cards and sorts them into
# alphabetical order (so we can see multiples)
def make_hand(num):
    hand = []
    
    #fill in code here

    for card in range(num):
       hand.append(cards.get_card())
    return hand

# A hand's value is 20 points for a pair (but not 3+ of a kind)
# + 5 points per Jack, Queen, or King,
# + 7 points per Ace.
def hand_value(my_cards):
    total = 0

    #fill in code here
    for card in my_cards:
        if card in "JQK":
            total += 5
        elif card in "A":
            total += 7
        elif my_cards.count(card)==2:
            total += 20
        
    return total


#main - test code (don't change this!)
my_hand = make_hand(5)
print("The hand:", my_hand)
print("Its value:", hand_value(my_hand))
    

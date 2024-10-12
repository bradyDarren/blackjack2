import random

# card deck made to resemble a standard 52 card deck. 
# Designated as tuples considering there will be no additional cards added to the card deck.
suits = ("diamonds", "hearts", "clubs", "spades")
ranks = ("ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "jack", "king", "queen")
card_values = (1,2,3,4,5,6,7,8,9,10,11)

s_rand = random.choice(suits)
r_rand = random.choice(ranks)

card_deck = {}

card_deck[s_rand] = {r_rand:card_values[1]} 

print(card_deck)
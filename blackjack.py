import random

# card deck made to resemble a standard 52 card deck. 
card_deck = {"diamonds":{"ace":[1,11], 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, "jack":10, "king":10, "queen":10},
             "hearts":{"ace":[1,11], 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, "jack":10, "king":10, "queen":10},
             "clubs":{"ace":[1,11], 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, "jack":10, "king":10, "queen":10},
             "spades":{"ace":[1,11], 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, "jack":10, "king":10, "queen":10}}


def hit(deck):
    # outputs random card suit
    rand_suit = random.choice(list(deck.keys()))
    # print(rand_suit) - test line

    # outputs random rank of card.
    rand_rank = random.choice(list(deck[rand_suit].keys()))
    # print(rand_rank) - test line

    # outputs the random cards value.
    card_value = deck[rand_suit][rand_rank]
    # print(card_value) - test line

    return card_value, rand_rank

def rank_eval(score):
    card = hit(card_deck) 
    if card[1] == "ace":
        if score >= 11: 
            score += 1
        else: 
            score += 11
    else: 
        score += card[0]
    return score

print(rank_eval(11))
print(rank_eval(5))


# def start():
#     user_start = input("Would you like to play a game of black jack? Type 'y' or 'n': ").lower
#     if user_start == 'n':
#         print("Thank you! Have a nice day!")
#     else:


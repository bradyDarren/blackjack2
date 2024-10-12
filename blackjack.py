import random

# card deck made to resemble a standard 52 card deck. 
card_deck = {"diamonds":{"ace":[1,11], 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, "jack":10, "king":10, "queen":10},
             "hearts":{"ace":[1,11], 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, "jack":10, "king":10, "queen":10},
             "clubs":{"ace":[1,11], 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, "jack":10, "king":10, "queen":10},
             "spades":{"ace":[1,11], 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, "jack":10, "king":10, "queen":10}}


def hit_me(deck):
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
    card = hit_me(card_deck) 
    if card[1] == "ace":
        if score >= 11: 
            score += 1
        else: 
            score += 11
    else: 
        score += card[0]
    return score

def blackjack():
    user_score = 0
    comp_score = 0 
    user_start = input("Would you like to play a game of blackjack? Type 'y' or 'n': ")
    user_score = [rank_eval(user_score), rank_eval(user_score)]
    comp_score = [rank_eval(comp_score), rank_eval(comp_score)]
    print(f"Your cards: {user_score}, current score: {user_score[0]}")
    print(f"Computer's first card: {comp_score[0]}")
    # while user_start != 'n':
    #     user_start = input("Type 'y' to get another card, type 'n' to pass: ")
    #     user_cards.append(rank_eval(user_score)[0])
    #     print(user_cards)

    #     if user_start == "n":
    #         print(f"Your final hand: {user_cards}, current score: {user_score}")
    #         print(f"Computer's first card: {comp_cards}, final score {comp_score}")
        
    # if user_score > 21:
    #     print(f"Busted. ")
blackjack()



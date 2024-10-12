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
    # print(card) - test line
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
    user_cards = [rank_eval(user_score), rank_eval(user_score)]
    user_score += sum(user_cards)
    comp_cards = [rank_eval(comp_score), rank_eval(comp_score)]
    comp_score += sum(comp_cards)
    print(f"Your cards: {user_cards}, current score: {sum(user_cards)}")
    print(f"Computer's first card: {comp_cards[0]}")
    while user_start != 'n':
        user_start = input("Type 'y' to get another card, type 'n' to pass: ")
        third_card = rank_eval(user_cards)
        user_cards.append(third_card)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        break

    #     if user_start == "n":
    #         print(f"Your final hand: {user_cards}, current score: {user_score}")
    #         print(f"Computer's first card: {comp_cards}, final score {comp_score}")
        
    # if user_score > 21:
    #     print(f"Busted. ")
blackjack()



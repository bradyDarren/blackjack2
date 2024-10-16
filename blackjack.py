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
            score = 1
        else: 
            score = 11
    else: 
        score = card[0]
    return score

def blackjack():
    user_score = 0
    comp_score = 0 
    user_start = input("Would you like to play a game of blackjack? Type 'y' or 'n': ").lower()
    if user_start == "y":
        user_cards = []
        comp_cards = []
        for card in range(2):
            user_cards.append(rank_eval(user_score))
            # print(user_cards) - test line
            user_score = sum(user_cards)
            # print(user_score) - test line
            comp_cards.append(rank_eval(comp_score))
            # print(comp_cards) - test line
            comp_score = sum(comp_cards)
            # print(comp_score) - test line
        print(f"Your cards: {user_cards}, current score: {sum(user_cards)}")
        print(f"Computer's hand: {comp_cards[0]}")
        while user_start != 'n':
            user_start = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if user_start == "n":
                while sum(comp_cards) <= sum(user_cards):
                    comp_cards.append(rank_eval(comp_score))                        
                print(f"Your final hand: {user_cards}, current score: {sum(user_cards)}")
                print(f"Computer's final hand: {comp_cards}, final score {sum(comp_cards)}")
                if sum(comp_cards) > 21:
                    print("Bust. Challenger Wins !!!")

            else: 
                user_cards.append(rank_eval(user_score))
                print(f"Your cards: {user_cards}, current score: {sum(user_cards)}")
                if sum(user_cards) > 21: 
                    print(f"Computer's final hand: {comp_cards}, final score {sum(comp_cards)}")
                    print("Bust. House Wins !!!")
                    break
                else: 
                    print(f"Computer's hand: {comp_cards[0]}")

        if sum(user_cards) > sum(comp_cards) and sum(user_cards) <= 21:
            print("Challenger wins!!")
        
        if sum(comp_cards) > sum(user_cards) and sum(comp_cards) <= 21:
            print("House wins!!!")

    else: 
        print("Thanks for coming. See you later!!!!")    
            
blackjack()



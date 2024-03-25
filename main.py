import random

class Card:

    suits = ["hearts", "spades", "clubs", "diamonds"]

    ranks = {
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "10": 10,
        "j": 11,
        "q": 12,
        "k": 13,
        "a": 14,
    }

    def __init__(self, suit=None, rank=None):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return (f"{self.suit} {self.rank}")

    @classmethod
    def deck_build(cls):
        deck = []
        for suit in Card.suits:
            for rank in Card.ranks:
                card = Card()
                card.suit = suit
                card.rank = rank
                deck.append(card)
        return deck

def split_deck(deck):
    mid_index = len(deck) // 2
    user1_deck = deck[:mid_index]
    user2_deck = deck[mid_index:]
    return user1_deck, user2_deck

def print_out_first_card(user1_deck,user2_deck):
    print(f"User 1's Deck: {user1_deck[0]} ")
    print(f"User 2's Deck: {user2_deck[0]} ")

def war_of_cards(user1_deck, user2_deck):
    index = 2

    while Card.ranks[user1_deck[index].rank] == Card.ranks[user2_deck[index].rank]:
        print("War!")
        index += 1
        if len(user1_deck) <= index or len(user2_deck) <= index:
            print("Both players do not have enough cards for war!")
            return

    card1 = user1_deck[index]
    card2 = user2_deck[index]

    if Card.ranks[card1.rank] > Card.ranks[card2.rank]:
        print(f"User 1's Card: {user1_deck[index]}")
        print(f"User 2's Card: {user2_deck[index]}")
        print("User 1 won")
        user2_deck.extend(user2_deck[:index+1])
        del user1_deck[:index+1]
        del user2_deck[:index+1]
    elif Card.ranks[card1.rank] < Card.ranks[card2.rank]:
        print(f"User 1's Card: {user1_deck[index]}")
        print(f"User 2's Card: {user2_deck[index]}")
        print("User 2 won")
        user1_deck.extend(user1_deck[:index+1])
        del user1_deck[:index+1]
        del user2_deck[:index+1]
    else:
        return

def bigger_card(user1_deck, user2_deck):
    card1 = user1_deck[0]
    card2 = user2_deck[0]

    if Card.ranks[card1.rank] > Card.ranks[card2.rank]:
        print("User 1 won")
        user1_deck.append(card1)
        user1_deck.append(card2)
        user1_deck.pop(0)
        user2_deck.pop(0)
    elif Card.ranks[card1.rank] < Card.ranks[card2.rank]:
        print("User 2 won")
        user2_deck.append(card1)
        user2_deck.append(card2)
        user1_deck.pop(0)
        user2_deck.pop(0)
    else:
        print("War")
        war_of_cards(user1_deck, user2_deck)

def no_cards(user1_deck,user2_deck):
    if len(user1_deck)==0:
        print("User 2 won!")
    if len(user2_deck)==0:
        print("User 1 won!")

def main():

    full_deck = Card.deck_build()
    random.shuffle(full_deck)
    user1_deck, user2_deck = split_deck(full_deck)
    while True:
        if len(user1_deck)!=0 and len(user2_deck)!=0:
            print_out_first_card(user1_deck, user2_deck)
            bigger_card(user1_deck, user2_deck)
            input("Press enter to continue")
        else:
            no_cards(user1_deck,user2_deck)
            break

if __name__=="__main__":
    main()



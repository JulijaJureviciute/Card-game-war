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


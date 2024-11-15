import random
from .card import Card

class Deck:
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['9', 'J', 'Q', 'K', '10', 'A']
    values = {'9': 0, 'J': 2, 'Q': 3, 'K': 4, '10': 10, 'A': 11}

    def __init__(self):
        self.cards = [Card(suit, rank, Deck.values[rank]) for suit in Deck.suits for rank in Deck.ranks]
        random.shuffle(self.cards)

    def deal(self, num):
        return [self.cards.pop() for _ in range(num)]
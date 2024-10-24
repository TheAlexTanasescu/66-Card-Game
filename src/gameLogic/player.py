class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def play_card(self, card):
        self.hand.remove(card)
        return card
    
    def check_marriages(self):
        marriages = []
        suits = {}
        
        for card in self.hand:
            if card.rank in ['K', 'Q']:
                if card.suit not in suits:
                    suits[card.suit] = []
                suits[card.suit].append(card)

        for suit, cards in suits.items():
            if len(cards) == 2:
                marriages.append((cards[0], cards[1]))

        return marriages

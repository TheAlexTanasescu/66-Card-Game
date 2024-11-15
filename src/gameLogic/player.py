class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def play_card(self, card):
        self.hand.remove(card)
        return card
    
    def show_hand(self):
        print("\n")
        print("Your Hand: ")
        tracker = 0
        for card in self.hand:
            print(f"{tracker}: {card}")
            tracker += 1
        print("\n")
    
    def choose_card(self):
        print("Select a card to play: ", end='')
        chosen_card_input = input()
        chosen_card_output = self.play_card(self.hand[int(chosen_card_input)])
        print("\n")
        return chosen_card_output

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

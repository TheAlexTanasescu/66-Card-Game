from .deck import Deck
from .player import Player
from .rules import play_trick, calculate_score

class Game:
    def __init__(self):
        self.deck = Deck()
        self.player = Player("Player")
        self.ai = Player("AI")
        self.trump_card = self.deck.cards.pop()
        print(f"Trump card: {self.trump_card}")

    def start(self):
        self.player.hand = self.deck.deal(6)
        self.ai.hand = self.deck.deal(6)

        for _ in range(6):
            lead_card = self.player.play_card(self.player.hand[0])  # Simplified for example
            ai_card = self.ai.play_card(self.ai.hand[0])  # Simplified for example
            print(f"Player plays: {lead_card}, AI plays: {ai_card}")
            winner = play_trick(lead_card, ai_card, self.trump_card.suit)
            print(f"{winner} wins the trick!")

        # Check for marriages and calculate score
        player_marriages = self.player.check_marriages()
        ai_marriages = self.ai.check_marriages()

        player_score = calculate_score(player_marriages)
        ai_score = calculate_score(ai_marriages)

        print(f"Player score from marriages: {player_score}")
        print(f"AI score from marriages: {ai_score}")

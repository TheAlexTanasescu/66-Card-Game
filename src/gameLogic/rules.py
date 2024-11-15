def play_trick(card1, card2, trump_suit):
    if card1.suit == card2.suit:
        return card1 if card1.value > card2.value else card2
    elif card1.suit == trump_suit:
        return card1
    elif card2.suit == trump_suit:
        return card2
    else:
        return card1  # If neither plays a trump


def calculate_score(marriages):
    points = 0
    for king, queen in marriages:
        points += 20  # Marriages score 20 points
    return points
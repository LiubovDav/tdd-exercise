VALID_CARDS = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']

def blackjack_score(hand):
    if len(hand) > 5:
        return "Invalid"

    score = 0
    num_of_aces = 0
    for card in hand:
        if card not in VALID_CARDS:
            return "Invalid"
        elif isinstance(card, int):
            score += card
        elif card != "Ace":
            score += 10
        else:
            num_of_aces += 1

    print(f"score without aces = {score}")

    if score > 21:
        return "Bust"

    if score + num_of_aces > 21:
        return "Bust"

    if num_of_aces == 0:
        return score
    elif num_of_aces == 1:
        if score <= 10:
            score += 11
        else:
            score += 1
    else:
        score += num_of_aces - 1
        if score <= 10:
            score += 11
        else:
            score += 1

    print(f"score with aces = {score}")

    if score > 21:
        return "Bust"

    return score

print(blackjack_score(["Ace", "Ace", "King"]))

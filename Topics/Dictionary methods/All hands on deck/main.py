def calculate_average_rank(cards):
    card_ranks = {
        "2": 2, "3": 3, "4": 4, "5": 5,
        "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,
        "Jack": 11, "Queen": 12, "King": 13, "Ace": 14,
    }

    total_rank = sum(card_ranks[card] for card in cards)

    average_rank = total_rank / len(cards)

    return average_rank


hand = []
for _ in range(6):
    deal_card = input()
    hand.append(deal_card)

print(calculate_average_rank(hand))

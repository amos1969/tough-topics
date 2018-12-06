suits = ["Hearts", "Spades", "Diamonds", "Clubs"]
cards = ["Ace", "2", "3"]
deck = []
for suit in suits:
    for card in cards:
        deck.append((suit, card))

print(deck)
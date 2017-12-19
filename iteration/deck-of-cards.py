suits = ["hearts", "diamonds", "clubs", "spades"]
ranks = [str(n) for n in range(2, 11)] + list('JQKA')

#cards = [(rank, suit) for suit in suits for rank in ranks]
# What effect does changing the order of the for loops have?
cards = [(rank, suit) for rank in ranks for suit in suits]

for card in cards:
    print(card)
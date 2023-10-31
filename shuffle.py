import random

# Define the suits and ranks of a deck of cards
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

# Create a deck of cards
deck = []
for suit in suits:
    for rank in ranks:
        deck.append(f'{rank} of {suit}')

# Shuffle the deck
random.shuffle(deck)

# Draw 5 cards and display them
for i in range(5):
    print(deck[i])

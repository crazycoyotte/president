# Import
import card
import random
import deck

# Variables

# Functions
def generate_deck():
    """Deck generation
    :return list"""
    values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    colors = ["pique", "coeur", "carreaux", "trefle"]
    maindeck = [card.Card(value, color) for value in values for color in colors]
    return maindeck


deck_generated = generate_deck()
deck = deck.__init__(deck_generated)
for card in deck:
    print(f"{card.value} - {card.name} - {card.color}")


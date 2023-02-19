# Import
import card
import random
import deck


# Variables

# Functions


deck = deck.Deck()
deck_generated = deck.generate_deck()

for card in deck_generated:
    print(card.__str__())

print("")
print("Mélange du deck")
print("")
deck.shuffle_deck(deck_generated)
for card in deck_generated:
    print(card.__str__())

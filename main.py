# Import
import hand
import deck


# Variables
human_hand = []
ai1_hand = []
ai2_hand = []
ai3_hand = []

# Functions

#Main program

#shuffled deck generation
deck = deck.Deck()
deck_generated = deck.generate_deck()
for card in deck_generated:
    print(card.__str__())
deck.shuffle_deck(deck_generated)
#for card in deck_generated:
#    print(card.__str__())

#cards deal
for i in range(13):
    human_hand.append(deck_generated[0])
    del deck_generated[0]
    ai1_hand.append(deck_generated[0])
    del deck_generated[0]
    ai2_hand.append(deck_generated[0])
    del deck_generated[0]
    ai3_hand.append(deck_generated[0])
    del deck_generated[0]

print("")
print("Main du joueur")
print("")
card_number = 0
cards_in_hand = ""
for card in human_hand:
    card_number += 1
    cards_in_hand += f"[{card_number}] : {card.__str__()} - \t"
    if card_number == 3 or card_number == 6 or card_number == 9 or card_number == 12:
        cards_in_hand += "\n"
print(cards_in_hand)
print("quelle carte souhaitez-vous jouer ?")



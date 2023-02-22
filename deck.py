# import
import card
import random


class Deck:
    def __init__(self):
        pass

    def generate_deck(self):
        """Deck generation
        :return list"""
        values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        colors = ["♠", "♥", "♦", "♣"]
        main_deck = [card.Card(value, color) for value in values for color in colors]
        return main_deck

    def shuffle_deck(self, deck):
        """Shuffle the deck"""
        random.shuffle(deck)
        return self
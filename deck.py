# import
import card
import random


class Deck:
    def __init__(self, list):
        self.list = list

    def shuffle_deck(self):
        """Shuffling the deck
        """
        random.shuffle(self)
        return self

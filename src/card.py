"""
Author: Agilan Hariharan
Last Modified: Thursday, April 17, 2025
Description: This file defines the Card and Deck classes for the Blackjack game.
"""

import random

# constants
SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
VALUES = { '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
           '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}

class Card:
    def __init__(self, suit, rank):
        # initialize a card with a suit and rank
        self.suit = suit
        self.rank = rank

    def __str__(self):
        # string representation of the card
        return f"{self.rank} of {self.suit}"

    def value(self):
        # get the numeric value of the card
        return VALUES[self.rank]

class Deck:
    def __init__(self):
        # create a full deck and shuffle it
        self.cards = [Card(s, r) for s in SUITS for r in RANKS]
        random.shuffle(self.cards)

    def deal(self):
        # deal one card from the deck, if any are left
        return self.cards.pop() if self.cards else None

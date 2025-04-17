"""
Author: Agilan Hariharan
Last Modified: Thursday, April 17, 2025
Description: This file defines the Player class for the Blackjack game.
"""

from util import calculate_hand_value

class Player:
    def __init__(self, name):
        # intialize name + empty hand
        self.name = name
        self.hand = []

    def add_card(self, card):
        # add a card to the player's hand
        self.hand.append(card)

    def get_value(self):
        # return the total value of the hand
        return calculate_hand_value(self.hand)

    def is_busted(self):
        # check if the player's hand value exceeds 21
        return self.get_value() > 21

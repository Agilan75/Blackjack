"""
Author: Agilan Hariharan
Last Modified: Thursday, April 17, 2025
Description: This file defines the Dealer class for the Blackjack game.
"""

from util import calculate_hand_value

class Dealer:
    def __init__(self):
        self.name = "Dealer"
        self.hand = []

    def add_card(self, card):
        # add a card to the dealer's hand
        self.hand.append(card)

    def get_value(self):
        # calculate the total value of the dealer's hand
        return calculate_hand_value(self.hand)

    def should_hit(self):
        # dealer hits if hand value is less than 16
        return self.get_value() < 16

    def is_busted(self):
        # check if dealer's hand value exceeds 21
        return self.get_value() > 21

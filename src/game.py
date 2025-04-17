"""
Author: Agilan Hariharan
Last Modified: Thursday, April 17, 2025
Description: This file defines the Game class which handles the logic for a single round of Blackjack.
"""

from card import Deck
from player import Player
from dealer import Dealer
from util import display_hand

class Game:
    def __init__(self):
        # initialize a new deck, player, and dealer
        self.deck = Deck()
        self.player = Player("Your")
        self.dealer = Dealer()

    def play_round(self):
        # reset hands and shuffle a new deck
        self.player.hand = []
        self.dealer.hand = []
        self.deck = Deck()

        # deal two cards to both player and dealer
        for _ in range(2):
            self.player.add_card(self.deck.deal())
            self.dealer.add_card(self.deck.deal())

        # player's turn
        while True:
            display_hand(self.player.name, self.player.hand)
            display_hand(self.dealer.name, self.dealer.hand, hide_first_card=True)

            # if player goes over 21, they lose
            if self.player.is_busted():
                print("You busted! Dealer wins. :(n \n")
                return 'lose'

            # ask for player input: hit or stay
            choice = input("Hit (h) or Stay (s)? ").lower()
            while choice not in ['h', 's']:
                choice = input("Invalid. Hit (h) or Stay (s)? ").lower()

            if choice == 'h':
                self.player.add_card(self.deck.deal())
            else:
                break

        # dealer's turn: dealer hits until threshold met
        while self.dealer.should_hit():
            self.dealer.add_card(self.deck.deal())

        # reveal final hands
        display_hand(self.player.name, self.player.hand)
        display_hand(self.dealer.name, self.dealer.hand)

        # determine outcome
        player_value = self.player.get_value()
        dealer_value = self.dealer.get_value()

        if self.dealer.is_busted():
            print("Dealer busted! You win. :) \n")
            return 'win'
        elif player_value > dealer_value:
            print("You win! :) \n")
            return 'win'
        elif player_value < dealer_value:
            print("Dealer wins. :( \n")
            return 'lose'
        else:
            print("It's a tie! :/ \n")
            return 'tie'

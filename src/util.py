"""
Author: Agilan Hariharan
Last Modified: Thursday, April 17, 2025
Description: This file provides utility functions for the Blackjack game
"""

def calculate_hand_value(hand):
    # calculate the total value of the hand
    value = sum(card.value() for card in hand)
    
    # count how many aces are in the hand
    aces = sum(1 for card in hand if card.rank == 'A')
    
    # change aces from 11 to 1 if the total value exceeds 21
    while value > 21 and aces:
        value -= 10
        aces -= 1
    
    return value

def display_hand(name, hand, hide_first_card=False):
    # print the name of the player or dealer
    print(f"{name} hand:")
    
    if hide_first_card:
        # hide the first card for the dealer during initial round
        print("Hidden Card:", *[str(card) for card in hand[1:]])
    else:
        # show all cards
        print(*[str(card) for card in hand])
    
    # only show total value if cards are not hidden
    if not hide_first_card:
        print(f"Total: {calculate_hand_value(hand)}\n")

"""
Author: Agilan Hariharan
Last Modified: Thursday, April 17, 2025
Description: This is the main file for the Blackjack game to intitalize the game.
"""

from game import Game  

def main():
    game = Game()  # create a new instance of the game
    wins, losses, ties = 0, 0, 0  # score tracking

    while True:
        # get the result
        result = game.play_round()

        # update the score
        if result == 'win':
            wins += 1
        elif result == 'lose':
            losses += 1
        else:
            ties += 1

        # show the current score
        print(f"Score => Wins: {wins}, Losses: {losses}, Ties: {ties}\n")

        # ask the player if they want to play another round
        play_again = input("Play again? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing!")
            break

main()

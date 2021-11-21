"""
Game of Nimm asks two players to take stones from a pile of 20.
Each can take 1 or 2 stones at a time.
The last player to take a stone loses.
"""

import random


def main():
    TOTAL_STONES = 20 
    remaining_stones = TOTAL_STONES
    turn_number = 1
    player_number = get_player_number(turn_number)
    while remaining_stones > 0: 

        #Ask user to remove 1 or 2 stones from the pile.
        print("There are " + str(remaining_stones) + " stones left")
        user_input = int(input("Player " + str(player_number) + " Would you like to remove 1 or 2 stones? "))
        if valid_answer(user_input):
            remaining_stones -= user_input
            turn_number += 1
            player_number = get_player_number(turn_number)
        else:
            print("GAME OVER")
            break

def get_player_number(turn_number):
    if int(turn_number) % 2 == 0:
        player_number = 2
        return player_number
    if int(turn_number) % 2 != 0:
        player_number = 1
        return player_number


def valid_answer(user_input):
    """
    Returns a valid value from user - either 1 or 2
    """
    if user_input == 1:
        return True
    if user_input == 2:
        return True
    return False






if __name__ == '__main__':
    main()

from karel.stanfordkarel import *

"""
File: Midpoint.py
------------------------
Place a beeper in the middle of the first row.
"""

def main():
    first_diagonal()
    second_diagonal()
    return_home()
    clear_first_diagonal()
    return_to_start()
    mid_point()

def mid_point():
    while no_beepers_present():
        move()


def return_to_start():
    while not_facing_west():
        turn_left()
    while front_is_clear():
        move()
    if front_is_blocked():
        turn_around()

def first_diagonal(): 
    #pre condition: Karel is facing East 
    #post condition: Karel is facing East
    while front_is_clear():
        put_beeper()
        move()
        turn_left()
        move()
        turn_right()
    if front_is_blocked():
        put_beeper()
        turn_around()
        move_to_wall()
        turn_around()

def second_diagonal():
    #pre: Karel is facing West
    #post: 
    while no_beepers_present():
        move()
        turn_right()
        move()
        turn_left()
    if beepers_present():
        turn_right()
        move_to_wall()
        put_beeper()

def return_home():
    turn_right()
    while front_is_clear():
        move()
    while not_facing_east():
        turn_left()

def clear_first_diagonal():
    while front_is_clear():
        pick_beeper()
        move()
        turn_left()
        move()
        turn_right()
    if front_is_blocked():
        pick_beeper()
        turn_right()
        move_to_wall()
        turn_right()

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def turn_around():
    turn_left()
    turn_left()

def move_to_wall():
    while front_is_clear():
        move()

if __name__ == '__main__':
    run_karel_program('Midpoint.w')

from karel.stanfordkarel import *

"""
File: PuzzleKarel.py
--------------------
Karel should finish the puzzle by picking up the last beeper (puzzle piece) and placing it in the right spot.
Karel should end in the same position Karel starts in -- the bottom left corner of the world.
"""
def main():
    #karel to pick up last beeper and move up to complete puzzle by placing beeper, then returning to Kerel's original position
    for i in range(2): 
        move()
    pick_beeper()
    move()
    turn_left()
    for i in range(2):
        move()
    put_beeper()
    for i in range(2):
        turn_left()
    while front_is_clear():
        move()
    turn_right()
    while front_is_clear():
        move()
    turn_around() #turn around to face East 

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def turn_around():
    turn_left()
    turn_left()





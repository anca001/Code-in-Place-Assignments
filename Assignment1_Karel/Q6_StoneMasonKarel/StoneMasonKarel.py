from karel.stanfordkarel import *

"""
File: StoneMasonKarel.py
------------------------
When you finish writing code in this file, StoneMasonKarel should be
able to solve the "repair the quad" problem from Assignment 1.
You should make sure that your program works for all of the
sample worlds supplied in the starter code.
"""

def main(): #Karel to keep building columns while front is clear, if front becomes blocked Karel will only build one more column 
    while front_is_clear():
        build_column()
        turn_around()
        move_to_wall()
        next_column()
    if front_is_blocked():
        build_column()





def turn_right():  
    turn_left()
    turn_left()
    turn_left()

def turn_around(): #after building column, Karel facing North
    turn_left()
    turn_left()

def move_to_wall(): #after building column, so Karel can return to base
    while front_is_clear():
        move()

def next_column(): #move 4 avenues to the next column 
    turn_left()
    for i in range(4):
        move()

def build_column(): #turn left to check North from initial position, put beepers and move if there are no beepers, if the front is blocked, Karel will check if there is a beeper, if no beeper is present at the top of column, Karel will place one
        turn_left()
        while front_is_clear():
            if no_beepers_present():
                put_beeper()
                move()
            else:
                move()
        if front_is_blocked():
            if no_beepers_present():
                    put_beeper()






if __name__ == '__main__':
    run_karel_program('SampleQuad1.w')

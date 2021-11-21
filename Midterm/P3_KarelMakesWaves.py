from karel.stanfordkarel import *

def main():
    # TODO write your solution here
    while front_is_clear():
        build_wave()
        resume_position()


# There is no need to edit code beyond this point

def build_wave():
    put_beeper()
    move()
    put_beeper()
    turn_left()
    move()
    put_beeper()

def resume_position():
    turn_around()
    move()
    turn_left()
    move()
    move()

def turn_right():
    for i in range(3):
        turn_left()

def turn_around():
    for i in range(2):
        turn_left()


if __name__ == "__main__":
    run_karel_program()

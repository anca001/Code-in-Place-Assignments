"""
TODO: Write a description here
"""

import random

MIN_NUMBER = 10
MAX_NUMBER = 99


def main():
    correct_guesses = 0


    while correct_guesses < 3:
        first_num = random.randint(MIN_NUMBER, MAX_NUMBER)
        second_num = random.randint(MIN_NUMBER, MAX_NUMBER)
        print('What is ' + str(first_num) + '+' + str(second_num) + '?')
        user_input = int(input('Your answer: '))
        total_result = int(first_num) + int(second_num)
        if user_input != total_result:
            correct_guesses = 0
            print('Incorrect. The expected answer is ' + str(total_result))

        elif user_input == total_result:
            correct_guesses += 1
            print("Correct! You've gotten " + str(correct_guesses) + " correct in a row")
        
        if correct_guesses == 3:
            print("Congratulations! You mastered addition.")





if __name__ == '__main__':
    main()

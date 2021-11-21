"""
Prints out a randomly generated addition problem
and checks if the user answers correctly.
"""

import random 


MIN_NUMBER = 10
MAX_NUMBER = 99

def main():
#the first_num and second_num are both between 10 and 99

    first_num = random.randint(MIN_NUMBER, MAX_NUMBER)
    second_num = random.randint(MIN_NUMBER, MAX_NUMBER)

    total_result = int(first_num) + int(second_num)
    #total_result is the sum of these two and what will be used the compare the user's response

    print(str('What is ') + str(first_num) + '+' + str(second_num) + '?')
    user_input = int(input("Your answer: "))
    #program prompts user for their answer to the addition problem
    #the program checks and compares that the user input is exactly the same as the total_result function
    if user_input == total_result:
        print('Correct!')
    else:
        print('Incorrect. The expected answer is ' + str(total_result))



if __name__ == '__main__':
    main()

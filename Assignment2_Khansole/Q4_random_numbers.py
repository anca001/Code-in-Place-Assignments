"""
Prints out 10 random numbers between 0 and 100.
"""

import random

def main():
    for i in range (NUM_RANDOM): 
        generate_numbers = random.randint(MIN_RANDOM,MAX_RANDOM)
        print(generate_numbers)

MIN_RANDOM = 0
MAX_RANDOM = 100
NUM_RANDOM = 10

if __name__ == '__main__':
    main()

"""
Asks user whether they wish to order food or cook then proceeds
to generate a random takeaway to order food from or a recipe to cook
"""

import random

COOK = 1
ORDER = 2

def main():
    print('Hello')
    ask_user = input("If you wish to cook enter 'cook', if you wish to order enter 'order' : " )
    if ask_user == 'cook':
        print(random.choice(food_list))
    if ask_user == 'order':
        print(random.choice(takeaway_list))


food_list = ['Chilli con carne', 'Pasta carbonara', 'Mac & cheese', 'Risotto', 'Carrot soup', 'Borscht', 'Mashed potatoes', 'Burgers', 'Egg fried rice']
takeaway_list = ['Bundobust', 'Archies', 'McDonalds', 'KFC', 'Wagamama', 'Shoryu', 'Nandos']


if __name__ == '__main__':
    main()

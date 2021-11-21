"""
Food decision maker: 
Asks user whether they wish to order food or cook then proceeds
to generate a random takeaway to order food from or a recipe to cook

Later addition: you can now also input an ingredient you have and the program
will generate a recipe with that particular ingredient for you to cook
"""

import random

COOK = 1
ORDER = 2

Recipes = {'Carbonara': ['eggs', 'pasta', 'parmesan', 'bacon'], 'Mashed potatoes': ['potatoes', 'milk', 'butter'], 
'Egg fried rice': ['rice', 'eggs', 'soy sauce', 'peas'], 'Mac & cheese': ['butter', 'milk', 'flour', 'cheddar', 'pasta'], 
'Risotto': ['rice', 'stock', 'wine', 'mushrooms', 'tomatoes'], 'Korean spicy beef soup': ['beef', 'soy sauce', 'noodles', 'mushrooms'],
'Chilli con carne': ['ground beef', 'onion', 'chilli', 'garlic', 'chopped tomatoes', 'beans'],
'Carrot soup': ['carrots', 'parsnip', 'potatoes', 'chopped tomatoes', 'stock'], 'Burgers': ['ground beef', 'buns', 'cheese']}

takeaway_list = ['Bundobust', 'Archies', 'McDonalds', 'KFC', 'Wagamama', 'Shoryu', 'Nandos', 'Pho', 'Dominos']

def main():
    print('Hello')
    ask_user = input("If you wish to cook enter 'cook', if you wish to order enter 'order' : " )
    if ask_user == 'cook':
        found_recipes = []
        while len(found_recipes) == 0:
            user_input = input("Enter main ingredient you want to use : ")
            for recipe in Recipes.keys():
                ingredients = Recipes[recipe]
                for ingredient in ingredients:
                    if user_input == ingredient:
                        found_recipes.append(recipe)
            if len(found_recipes) > 0:
                print(random.choice(found_recipes))
            else:
                print('recipe not found')
    if ask_user == 'order':
        print(random.choice(takeaway_list))









if __name__ == '__main__':
    main()

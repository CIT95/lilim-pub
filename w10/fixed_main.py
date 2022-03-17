# # Week 10 Learn Together

# Funky Dice Program

# Imports
import random
from os import system

# Variables
# 1. result had one too many =
result = ""
funky_dice = {}
end_program = False

# Functions


def set_dice_face(side):
    global funky_dice
    face = input("What do you want this side of the dice to be?\n>> ")
    funky_dice[side] = face
    return f"\nThe value of Side {side} is set to '{face}'."


def roll():
    global result
    result = funky_dice[random.randint(1, 6)]
    return result


def get_result():
    roll_result = roll()
    return f"\nYou roll the funky dice and get {roll_result}."


# Program

print("\nWelcome to Funky Dice!")
print("We give you a blank dice and you decide what the sides will be.")
# 2. line 40 did not have the "" closing the message
print("The sides can be anything from numbers, names, or even nothing.")
print("It's entirely up to you.\n")

# 3. (syntax) error for while did not include :
while not end_program:
    for value in range(6):
        print(set_dice_face(value + 1))

    roll_option = input("\nDo you want to roll your dice?\n"
                        "Type 'Y' for yes and 'N' for no.\n"
                        ">> ").lower()

    if roll_option == "y":
        end_roll = False
        print(get_result())

        while not end_roll:
            again = input("\nDo you want to roll again?\n"
                          "Type 'Y' for yes and 'N' for no.\n"
                          ">> ").lower()
            # 4.switched the 'y' and 'n'
            if again == 'y':
                print(get_result())
            elif again == 'n':
                end_roll = True

        new_dice = input("\nDo you want to make a new dice?\n"
                         "Type 'Y' for yes and 'N' for no.\n"
                         ">> ").lower()

        # To either end or repeat the program
        # 5. line 73 did not include ==
        if new_dice == 'y':
            system('cls')
            print("\nYou already know the rules.\n")
        else:
            end_program = True

    else:
        # 6. line 81 did not have the proper idention
        end_program = True

print("\nSee you next time.")

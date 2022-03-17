import random
# Setting lists for usage
location = ["Workplace", "Store", "Park"]
items = ["Phone", "Car Keys", "Wallet", "ID", "Money", "Water Bottle"]

# First user input to determine where they are going for the day.
decision1 = int(input('Where are you going today?Type in one of the following:'
                      ' 0 for "Workplace", 1 for "Store", 2 for "Park"\n'))

# Using Comparison operators
if decision1 >= 3 or decision1 < 0:
    print("You have typed in a invalid option")
else:
    print(f"You are going to the:{location[decision1]}")
 

# 2nd user input to continue the process of today's objective
    clothes = int(input('Have you made yourself look presentable today?'
                        'Type "0" for yes and "1" for no.\n'))
    if clothes >= 2 or decision1 < 0:
        print("You have typed in a invalid option")
    elif clothes == 1:
        print("Guess you better get started then, the clock is ticking!")
    else:
        print("Awesome! You look spiffy.")


# Using random genenator to doublecheck items
        items = random.choice(items)
        print(f"Wait, aren't you forgetting something? Like your: {items}?")
        forgotten_item = input('Type "Y" for yes and "N" for no.\n').lower()
        if forgotten_item == "y":
            print("Good thing I was here to remind you.")
        else:
            print("Alright then, let's head out the door.")

# Sadly I had trouble coming up with a loops =(
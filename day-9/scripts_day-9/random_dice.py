import random

def roll_dice():
    dice_1 = random.randint(1,6)
    dice_2 = random.randint(1,6)

    add_dice = dice_1 + dice_2
    print(f"You rolled a dice of {dice_1} and {dice_2}")
    print(f"sum of two dice is {add_dice}")
roll_dice()
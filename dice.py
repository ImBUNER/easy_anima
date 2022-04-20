import random

# Function that roll a dice.
# "side" is the number of sides the dice has
def roll(side):
    dice_result = random.randint(1, side)
    if side == 100:
        # In this rol, with a 90+ result in a 100 size dice, you have to roll them again
        if dice_result >= 90:
            dice_result = dice_result + random.randint(1, 100)
    return(dice_result)
    
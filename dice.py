import random

# Function that roll a dice.
# "side" is the number of sides the dice has
def roll(side):
    dice_result = random.randint(1, side)
    if side == 100:
        # Because the roll rules, with a 90+ result in a 100 size dice, you have to roll them again
        if dice_result >= 90:
            dice_result = dice_result + random.randint(1, 100)
    return(dice_result)





# Con esta función puedo tirar los dados que quiera el usuario
# NO me deja mostrarlo por pantalla porq es una lista. 

# def roll(num, side):
#     all_dices=[]
#     for _ in range(num):
#         dice_result = random.randint(1, side)
#         # Because the roll rules, with a 90+ result in a 100 size dice, you have to roll them again
#         if side == 100 and dice_result >= 90:
#             dice_result = dice_result + random.randint(1, 100)
#         all_dices.append(dice_result)
#     return(all_dices)
# Άσκηση 9-13

from random import randint

class Dice:
    """Modelization of a dice"""
    def __init__(self, sides=6):
        self.sides = sides

    def roll_dice(self):
        x = randint(1, self.sides)
        print(f"Rolling dice... \nResult: {x}\n")

dice_1 = Dice()
dice_1.roll_dice()
dice_1.roll_dice()
dice_1.roll_dice()
dice_1.roll_dice()
dice_1.roll_dice()
dice_1.roll_dice()
dice_1.roll_dice()
dice_1.roll_dice()
dice_1.roll_dice()
dice_1.roll_dice()

print("\nNOTE! Now the dice has 10 numbers/sides:\n\n")

dice_2 = Dice(10)
dice_2.roll_dice()
dice_2.roll_dice()
dice_2.roll_dice()

print("\nNOTE! Now the dice has 20 numbers/sides:\n\n")

dice_3 = Dice(20)
dice_3.roll_dice()
dice_3.roll_dice()
dice_3.roll_dice()

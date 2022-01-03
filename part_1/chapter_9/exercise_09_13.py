# Exercise 9-13

from random import randint

class Dice:
    """Modelization of a dice"""
    def __init__(self, sides=6):
        self.sides = sides

    def roll_dice(self):
        number = randint(1, self.sides)
        print(f"Rolling dice... \nResult: {number}")

# Create a six sided dice
six_sided_dice = Dice()

# Roll the six sided dice ten times
print("\n\nRolling the six sided dice: \n")

for number in range(10):
    six_sided_dice.roll_dice()

# Create a ten sided dice
ten_sided_dice = Dice(10)

# Roll the ten sided dice ten times
print("\n\nRolling the ten sided dice: \n")

for number in range(10):
    ten_sided_dice.roll_dice()

# Create a twenty sided dice
twenty_sided_dice = Dice(20)

# Roll the ten sided dice ten times
print("\n\nRolling the twenty sided dice: \n")

for number in range(10):
    twenty_sided_dice.roll_dice()
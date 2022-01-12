from random import randint

class Dice:
    """A class to represent a dice"""

    def __init__(self, num_sides=6):
        """Initialize attributes of dice"""
        self.num_sides = num_sides

    def roll_dice(self):
        result = randint(1, self.num_sides)
        return result
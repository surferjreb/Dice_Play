import random


class Die:
    """ A class representing a single die"""

    def __init__(self, num_sides):
        """ Assume a six sided die"""
        self.num_sides = num_sides

    def roll(self):
        # Return a random value between 1 and number of sides
        return random.randint(1, self.num_sides)

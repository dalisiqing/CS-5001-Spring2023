import random


class Die:
    """
    A single playing die
    """

    def __init__(self):
        self.current_value = 0

    def roll(self):
        """
        Roll a die
        """
        self.current_value = random.randint(1, 6)

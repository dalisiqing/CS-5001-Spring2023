from die import Die


class PairOfDice:
    """
    Construct a pair of dies in the paly
    """
    def __init__(self):
        self.dice1 = Die()
        self.dice2 = Die()

    def roll_dice(self):
        """
        Roll the pair of dies
        """
        self.dice1.roll()
        self.dice2.roll()

    @property
    def current_value(self):
        """
        Get the sum of current values of the pair of dies
        """
        return self.dice1.current_value + self.dice2.current_value

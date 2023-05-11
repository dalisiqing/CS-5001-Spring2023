from pair_of_dice import PairOfDice


class GameController:
    """
    A controller for the die game
    """
    def __init__(self):
        self.shooter_dices = PairOfDice()
        self.winList = [7, 11]
        self.loseList = [2, 3, 12]

    def start_play(self):
        """
        Start the game
        """
        input("Press enter to roll the dice...")
        print()
        self.shooter_dices.roll_dice()
        if self.shooter_dices.current_value in self.winList:
            self.win()
        elif self.shooter_dices.current_value in self.loseList:
            self.lose()
        else:
            self.point = self.shooter_dices.current_value
            print(f"Your point is {self.point}")
            self.keep_rolling()

    def keep_rolling(self):
        """
        Keep rolling after the start if possible
        """
        input("Press enter to roll the dice...")
        self.shooter_dices.roll_dice()
        if self.shooter_dices.current_value == self.point:
            self.win()
        elif self.shooter_dices.current_value == 7:
            self.lose()
        else:
            print()
            print(f"You rolled {self.shooter_dices.current_value}.")
            self.keep_rolling()

    def win(self):
        """
        Print the message for the win of shooter
        """
        print()
        print(f"You rolled {self.shooter_dices.current_value}. You win!")

    def lose(self):
        """
        Print the message for the lose of shooter
        """
        print()
        print(f"You rolled {self.shooter_dices.current_value}. You lose.")



class Bench:
    """A class representing a sidelines bench"""
    def __init__(self):
        # TODO: Initialize the bench object with whatever
        # attributes and values it will need
        self.players = []

    def send_to_bench(self, name):
        # TODO: Put the player "onto the bench"
        if name not in self.players:
            self.players.insert(0, name)

    def get_from_bench(self):
        # TODO: Return the name of the player who has
        # been on the bench longest.
        if self.players == []:
            print("The bench is empty.")
        else:
            print(f"Got {self.players.pop().name} from bench")

    # TODO: Write the function that will display the
    # current list of players on the bench
    def show_bench(self):
        if self.players != []:
            print('The bench currently includes:')
            for i in self.players:
                print(i.name)
        else:
            print("The bench is empty.")

    # TODO: Write any other methods that might be used
    # by the methods above.
    def cut_player(self, name):
        # TODO: Remove the player with the name player_name
        # from the players list.
        for i in self.players:
            if i.name == name:
                self.players.remove(i)

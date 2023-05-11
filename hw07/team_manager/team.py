from player import Player


class Team:
    """A class representing a dodgeball team"""
    # All methods in Python include arguments representing the object
    # itself. In the method definition, this is represented by the
    # `self` parameter.
    def __init__(self):
        self.name = "Anonymous Team"
        self.players = []

    # Another example of self. The method call only passes one argument,
    # the 'name; value. But the method definition must always include the
    # self parameter.
    def set_team_name(self, name):
        # TODO: set the team name
        self.name = name

    # Note again that `self` is the first parameter.
    def add_player(self, player_name, player_number, player_position):
        # TODO: call the Player class constructor with the appropriate
        # values to create a new player object, then add that
        # player object to the team's players list.
        self.new_player = Player(player_name, player_number, player_position)
        self.players.append(self.new_player)

    def cut_player(self, name):
        # TODO: Remove the player with the name player_name
        # from the players list.
        for i in self.players:
            if i.name == name:
                self.players.remove(i)
                return
        print(f"{name} isn't on the team.")

    def is_position_filled(self, position):
        # TODO: Write the method that checks whether
        # there is currently at least one player on the team
        # occupying the requested position
        for i in self.players:
            if i.position == position:
                print(f'Yes, the {position} position is filled')
                return
        print(f'No, the {position} position is not filled')

    # TODO: Write any necessary methods to support the methods
    # above, and write the method that will display (print to screen)
    # the full team roster in the following format:

    #    The lineup for Seattle Scorpions is:
    #    15       Garcia          catcher
    #    55       Wiggins         corner
    #    99       McCann          sniper
    def display(self):
        print(f'The lineup for {self.name} is:')
        if not self.players == []:
            for i in self.players:
                print(f'\t{i.number}\t{i.name}\t\t{i.position}')
        else:
            print('The team currently has no players')

class Team:
    def __init__(self, name, players, coach):
        self.name = name 
        self.players = players
        self.coach = coach

    def add_player(self, new_player_name):
        self.players.append(new_player_name)

    def has_player(self, player_name):
        if player_name in self.players:
            return True
        else: 
            return False
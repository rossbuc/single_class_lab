class Team:
    def __init__(self, name, players, coach):
        self.name = name 
        self.players = players
        self.coach = coach
        self.points = 0

    def add_player(self, new_player_name):
        self.players.append(new_player_name)

    def has_player(self, player_name):
        if player_name in self.players:
            return True
        else: 
            return False

    def play_game(self, has_won):
        if has_won:
            self.points += 3
            
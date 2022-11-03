class Club:
    def __init__(self, name, date_of_creation, wins, losses, players = []):
        self.name = name
        self.date_of_creation = date_of_creation
        self.players = players
        self.wins = wins
        self.losses = losses

    def __str__(self):
        return f"{self.name}"

    def add_player(self, player):
        self.players.append(player)

    def update_record(self, is_win):
        if is_win:
            self.wins += 1
        else:
            self.losses += 1
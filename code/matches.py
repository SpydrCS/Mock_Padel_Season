class Match:
    def __init__(self, date, location, tournament, players = [], score = "Not started"):
        self.date = date
        self.location = location
        self.tournament = tournament
        self.players = players
        self.score = score

    def __str__(self):
        return f"{self.players[0]} vs {self.players[1]}"

    def add_player(self, player):
        self.players.append(player)

    def set_score(self, score):
        self.score = score
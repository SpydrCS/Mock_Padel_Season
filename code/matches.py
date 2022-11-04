class Match:
    def __init__(self, level, date, location, tournament = "", players = [], score = "Not started"):
        self.level = level
        self.date = date
        self.location = location
        self.tournament = tournament
        self.players = players
        self.score = score

    def __str__(self):
        return f"Level {self.level}: {self.players[0].name} and {self.players[1].name} vs {self.players[2].name} and {self.players[3].name}"

    def add_player(self, player):
        self.players.append(player)

    def set_score(self, score):
        self.score = score

    def set_tournament(self, tournament):
        self.tournament = tournament
class Tournament:
    def __init__(self, name, location, start_date, end_date, players = [], matches = []):
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.players = players
        self.matches = matches

    def __str__(self):
        return f"{self.name}"

    def add_player(self, player):
        self.players.append(player)

    def add_match(self, match):
        self.matches.append(match)
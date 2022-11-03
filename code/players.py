class Player:
    def __init__(self, name, age, sex, dominant_hand, level, wins, losses, past_tournaments = [], past_matches = []):
        self.name = name
        self.age = age
        self.sex = sex
        self.dominant_hand = dominant_hand
        self.level = level
        self.wins = wins
        self.losses = losses
        self.tournaments = past_tournaments
        self.past_matches = past_matches

    def __str__(self):
        return f"{self.name}"

    def add_tournament(self, tournament):
        self.tournaments.append(tournament)

    def add_match(self, match):
        self.past_matches.append(match)

    def update_record(self, is_win):
        if is_win:
            self.wins += 1
        else:
            self.losses += 1
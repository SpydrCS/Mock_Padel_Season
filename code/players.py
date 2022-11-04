from scores import *

class Player:
    def __init__(self, name, age, sex, dominant_hand, level, wins, losses, club = "", tournaments = [], matches = []):
        self.name = name
        self.age = age
        self.sex = sex
        self.dominant_hand = dominant_hand
        self.level = level
        self.wins = wins
        self.losses = losses
        self.tournaments = tournaments
        self.matches = matches
        self.club = club

    def __str__(self):
        return f"{self.name}, Level {self.level}"

    def add_tournament(self, tournament):
        self.tournaments.append(tournament)

    def add_match(self, match):
        self.matches.append(match)

    def add_club(self, club):
        self.club = club

    def update_record(self, is_win):
        if is_win:
            self.wins += 1
        else:
            self.losses += 1

    def get_record_against_player(self, name):
        wins = 0
        losses = 0
        #for (i, match) in enumerate(self.matches):
        #    print(str(i), " ", match)

        for match in self.matches:
            if match.players[0] == self or match.players[1] == self:
                if match.players[2].name == name or match.players[3].name == name:
                    if match.score.get_winner() == 1:
                        wins += 1
                    else:
                        losses += 1
            else:
                if match.players[0].name == name or match.players[1].name == name:
                    #print(match)
                    if match.score.get_winner() == 2:
                        wins += 1
                    else:
                        losses += 1
        
        if wins == 0 and losses == 0:
            print("There are no matches between the two players.")
        else:
            print("Win/Loss vs " + name + " : " + str(wins//4) + "/" + str(losses//4))

    def get_past_partners(self):
        partners = []
        for match in self.matches:
            if match.players[0] == self:
                partners.append(match.players[1])
            elif match.players[1] == self:
                partners.append(match.players[0])
            elif match.players[2] == self:
                partners.append(match.players[3])
            elif match.players[3] == self:
                partners.append(match.players[2])
        
        if partners == []:
            print(self.name + " has no partners yet.")
        else:
            for (i, partner) in enumerate(partners[::4]):
                print(str(i+1), ": ", partner)
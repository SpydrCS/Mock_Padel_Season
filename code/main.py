from clubs import *
from matches import *
from players import *
from tournaments import *

# club, past tournaments and past matches added later
p1 = Player('Dorisa A.', 79, 'F', 'R', 4, 46, 32)
p2 = Player('Grayce B.', 68, 'F', 'R', 3, 46, 34)
p3 = Player('Harvey C.', 68, 'M', 'L', 2, 42, 23)
p4 = Player('Letizia D.', 19, 'F', 'L', 4, 14, 19)
p5 = Player('Benedikta E.', 49, 'F', 'L', 1, 22, 13)
p6 = Player('Mozelle F.', 44, 'F', 'L', 5, 14, 45)
p7 = Player('Ariadne G.', 62, 'F', 'L', 1, 2, 27)
p8 = Player('Estel H.', 47, 'F', 'R', 4, 35, 16)
p9 = Player('Salvador I.', 69, 'M', 'R', 4, 33, 3)
p10 = Player('Millard J.', 61, 'M', 'L', 4, 49, 16)

c1 = Club('Top-Padel Industrial', '82-64-8973', 2, 28, [p1])
c2 = Club('QM Indoor', '96-08-7262', 47, 6, [p2])
c3 = Club('QM Matosinhos', '07-70-6206', 3, 19, [p3])
c4 = Club('QM Gaia', '27-01-8248', 50, 41, [p4])
c5 = Club('Top-Padel Fluvial', '65-12-0361', 1, 44, [p5])
c6 = Club('Top-Padel Fojo', '08-00-9709', 50, 23, [p6])
c7 = Club('Star Padel', '00-15-4410', 5, 32, [p7])
c8 = Club('Mar Padel', '44-15-9580', 13, 49, [p8])
c9 = Club('Padel Inn', '70-45-0499', 49, 19, [p9])
c10 = Club('IdealKorpus', '05-81-2965', 46, 3, [p10])

s1 = Score("6-3 6-4")
s2 = Score("6-2 6-1")
s3 = Score("6-1 7-5")
s4 = Score("6-4 6-1")
s5 = Score("7-5 6-0")
s6 = Score("7-6 6-3")
s7 = Score("6-7 2-6")
s8 = Score("6-1 6-2")
s9 = Score("6-0 6-3")
s10 = Score("0-6 3-6")

# tournament added later
m1 = Match(1, '29-06-2394', 'Russia', '', [p1,p2,p3,p4], s1)
m2 = Match(1, '00-32-9062', 'Russia', '', [p2,p4,p6,p8], s2)
m3 = Match(2, '65-36-1441', 'Syria', '', [p3,p5,p7,p9], s3)
m4 = Match(2, '77-28-3088', 'Japan', '', [p10,p8,p4,p3], s4)
m5 = Match(3, '24-50-4377', 'South Africa', '', [p1,p4,p5,p7], s5)
m6 = Match(3, '84-96-6833', 'China', '', [p4,p7,p3,p6], s6)
m7 = Match(4, '24-65-0345', 'China', '', [p1,p2,p5,p8], s7)
m8 = Match(4, '88-32-8664', 'France', '', [p6,p4,p7,p8], s8)
m9 = Match(5, '58-13-4426', 'China', '', [p9,p10,p5,p6], s9)
m10 = Match(5, '69-16-4895', 'Afghanistan', '', [p4,p5,p7,p8], s10)

t1 = Tournament('nfbfhr Padel Open', 'Indonesia', '50-13-6899', '16-26-4196', [p1,p2,p3,p4], [m1])
t2 = Tournament('emrolm Padel Open', 'Nigeria', '94-02-6364', '17-73-1972', [p2,p4,p6,p8], [m2])
t3 = Tournament('gefrat Padel Open', 'China', '04-59-3776', '64-16-2105', [p3,p5,p7,p9], [m3])
t4 = Tournament('rvqwvn Padel Open', 'Peru', '12-04-7057', '14-84-3727', [p10,p8,p4,p3], [m4])
t5 = Tournament('tzungm Padel Open', 'Indonesia', '66-76-9587', '99-73-9499', [p1,p4,p5,p7], [m5])
t6 = Tournament('yfgotf Padel Open', 'Portugal', '03-77-0155', '92-79-0241', [p4,p7,p3,p6], [m6])
t7 = Tournament('ddlwch Padel Open', 'Paraguay', '10-44-0328', '16-49-7581', [p1,p2,p5,p8], [m7])
t8 = Tournament('gylmtw Padel Open', 'Argentina', '33-34-5205', '00-55-4847', [p6,p4,p7,p8], [m8])
t9 = Tournament('ghbbsq Padel Open', 'China', '54-17-4521', '64-64-8708', [p9,p10,p5,p6], [m9])
t10 = Tournament('djjorj Padel Open', 'China', '04-53-2835', '08-69-7914', [p4,p5,p7,p8], [m10])

players_list = [p1,p2,p3,p4,p5,p6,p7,p8,p9,p10]

clubs_list = [c1,c2,c3,c4,c5,c6,c7,c8,c9,c10]

matches_list = [m1,m2,m3,m4,m5,m6,m7,m8,m9,m10]

tournaments_list = [t1,t2,t3,t4,t5,t6,t7,t8,t9,t10]

def populate():
    for club in clubs_list:
        for player in club.players:
            player.add_club(club)

    for match in matches_list:
        for player in match.players:
            player.add_match(match)
            #print("Player: ", player, " Match: ", match)

    for tournament in tournaments_list:
        for player in tournament.players:
            player.add_tournament(tournament)

    for tournament in tournaments_list:
        for match in tournament.matches:
            match.set_tournament(tournament)

    #p3.get_record_against_player("Ariadne")

def extra_menu(i):
    print("To see the name of all the players and their according catergories, insert 1. To see all the matches, insert 2. To exit, insert 0.")
        
    info3 = int(input())

    if info3 == 0: 
        return

    elif info3 == 1:
        #see players and categories
        for (ind, player) in enumerate(tournaments_list[i-1].players):
            print(str(ind+1), ": ", player)


    elif info3 == 2:
        #see matches
        for match in tournaments_list[i-1].matches:
            print(match)
            print("\n")

    extra_menu(i)

def menu():
    print("Hello, to see all the tournaments, insert 1. To see all players, insert 2. To exit, insert 0.")
    inpt = int(input())

    print("\n -------------------------- \n")

    if inpt == 0:
        return

    elif inpt == 1:
        for (i, tour) in enumerate(tournaments_list):
            print(str(i+1), ": ", tour)

        print("\nInsert the number of the tournament to see more details. To exit, insert 0.")

        i = int(input())

        print("\n -------------------------- \n")

        if i == 0:
            return
        else:
            print("Name: " + tournaments_list[i-1].name)
            print("Location: " + tournaments_list[i-1].location)
            print("Start date: " + tournaments_list[i-1].start_date)
            print("End date: " + tournaments_list[i-1].end_date)
            print("Number of registered players: " + str(len(tournaments_list[i-1].players)))
            print("Number of matches: " + str(len(tournaments_list[i-1].matches)))
            print("To go more in depth, insert 1. To exit, insert 0.")
            print("\n -------------------------- \n")

        info2 = int(input())
        if info2 == 0:
            return
        
        extra_menu(i)

    elif inpt == 2:
        print("\n -------------------------- \n")
        for (indx, player) in enumerate(players_list):
            print(str(indx+1), ": ", player)


populate()
menu()
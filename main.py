import Team
import Player
import GUI
import Match

'''
name1=str(input("first name of first player of team one: "))
lname1=str(input("last name of first player of team one: "))
player1=Player.Player(name1, lname1)
name2=str(input("first name of second player of team one: "))
lname2=str(input("last name of second player of team one: "))
player2=Player.Player(name2, lname2)
team1=Team.Team(player1, player2)
name3=str(input("first name of first player of team two: "))
lname3=str(input("last name of first player of team two: "))
player3=Player.Player(name3, lname3)
name4=str(input("first name of second player of team two: "))
lname4=str(input("last name of second player of team two: "))
player4=Player.Player(name4, lname4)
team2=Team.Team(player3, player4)
'''

team1 = Team.Team(Player.Player("Luka", "Mamulashvili"), Player.Player("Tevdore", "Omiadze"))
team2 = Team.Team(Player.Player("Saba", "Comaia"), Player.Player("Giorgi", "Tapliashvili"))

match = Match.Match(team1, team2, 3, 6, 7, False)
match.startMatch()
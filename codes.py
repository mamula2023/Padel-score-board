MATCHWON1   = -200
MATCHPOINT1 = -100
SETWON1     = -20
SETPOINT1   = -10
GAMEWON1    = -2
GAMEPOINT1  = -1

DEUCE       = 0

GAMEPOINT2  = 1
GAMEWON2    = 2
SETPOINT2   = 10
SETWON2     = 20
MATCHPOINT2 = 100
MATCHWON2   = 200

points={GAMEPOINT1:"GAMEPOINT", GAMEPOINT2:"GAMEPOINT", SETPOINT1:"SETPOINT", SETPOINT2:"SETPOINT", MATCHPOINT1:"MATHCPOINT", MATCHPOINT2:"MATHCPOINT"}
teams={GAMEPOINT1:"ONE", SETPOINT1:"ONE", MATCHPOINT1:"ONE",GAMEPOINT2:"TWO", SETPOINT2:"TWO", MATCHPOINT2:"TWO"}

def logInfo(code):
    print("{point} FOR TEAM {team}".format(point=points[code]), team=teams[code])
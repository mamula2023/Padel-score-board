import Team
import Score

class Game:
    def __init__(self, t1:Team, t2:Team, score:Score, nSets:int, nGames:int,tieTarget:int, golden:bool):
        self.__score__  = score
        self.__teamOne__= t1
        self.__teamTwo__= t2
        self.__nSets__  = nSets
        self.__nGames__ = nGames
        self.__golden__ = golden
        self.__tieTarget__ = tieTarget

    #0-0 1-15 2-30 3-40 4-45/AD
    def playGame(self):
        while True:
            team=input()
            if not team.isnumeric():
                continue 
            pointWon = int(team)
            if pointWon > 2 or pointWon < 0:
                continue


            result=self.__score__.newPoint(pointWon)
            self.__displayFullScoreSheet__()
            if result:
                print("Finished")
    

    def __displayFullScoreSheet__(self):
        print("{team} {sets} {currGame}".format(
            team=self.__teamOne__.getDisplay(),
            sets=self.__score__.getFinishedSets(1),
            currGame=self.__score__.getCurrGame(1)
        ))
        print("{team} {sets} {currGame}".format(
            team=self.__teamTwo__.getDisplay(),
            sets=self.__score__.getFinishedSets(2),
            currGame=self.__score__.getCurrGame(2)
        ))

        

    def tiebreaker():
        pass
    

    

    

import Team
import Score
import GUI
class Game:
    def __init__(self, t1:Team, t2:Team, score:Score, nSets:int, nGames:int,tieTarget:int, golden:bool, gui):
        self.__score__  = score
        self.__teamOne__= t1
        self.__teamTwo__= t2
        self.__nSets__  = nSets
        self.__nGames__ = nGames
        self.__golden__ = golden
        self.__tieTarget__ = tieTarget

   
    

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
    

    

    

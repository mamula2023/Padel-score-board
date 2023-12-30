import Team
import Score
import Game
class Match:
    def __init__(self, t1: Team, t2: Team, setTarget:int, gameTarget:int, tieTarget:int,  golden:bool):
        self.__teamOne__ = t1
        self.__teamTwo__ = t2
        self.__nSets__   = setTarget
        self.__nGames__  = gameTarget
        self.__tieTarget__ = tieTarget     
        self.__golden__  = golden
        self.__score__   = Score.Score(setTarget, gameTarget, tieTarget, golden)   
        #print("Match class created for\n{t1}\n{t2}".format(t1=self.__teamOne__.getDisplay(), t2=self.__teamTwo__.getDisplay()))
    
    def startMatch(self):
        print("Match started between\n{t1}\n{t2}".format(t1=self.__teamOne__.getDisplay(), t2=self.__teamTwo__.getDisplay()))
        
        game=Game.Game(self.__teamOne__, self.__teamTwo__, self.__score__, self.__nSets__, self.__nGames__, self.__tieTarget__, self.__golden__)
        game.playGame()


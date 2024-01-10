import Team
import Score
import Game
import GUI
class Match:
    def __init__(self, t1: Team, t2: Team, nSets:int, gameTarget:int, tieTarget:int,  golden:bool):
        self.__teamOne__ = t1
        self.__teamTwo__ = t2
        self.__nSets__   = nSets
        self.__nGames__  = gameTarget
        self.__tieTarget__ = tieTarget     
        self.__golden__  = golden
        self.__score__   = Score.Score(nSets, gameTarget, tieTarget, golden)   
        self.__gui__ = GUI.gameDisplay(t1, t2, self.__score__)
        #print("Match class created for\n{t1}\n{t2}".format(t1=self.__teamOne__.getDisplay(), t2=self.__teamTwo__.getDisplay()))
    

     #0-0 1-15 2-30 3-40 4-45/AD
    def playMatch(self):
        while True:
            team=self.__gui__.getTeam()

            result=self.__score__.newPoint(team)
            self.gui.updateScore()
            if result:
                print("Finished")
                return

    def startMatch(self):
        print("Match started between\n{t1}\n{t2}".format(t1=self.__teamOne__.getDisplay(), t2=self.__teamTwo__.getDisplay()))
        
        game=Game.Game(self.__teamOne__, self.__teamTwo__, self.__score__, self.__nSets__, self.__nGames__, self.__tieTarget__, self.__golden__, self.__gui__)
        game.playGame()
        
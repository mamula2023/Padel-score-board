import Player
class Team:
    def __init__(self, p1, p2):
        self.__playerOne__ = p1
        self.__playerTwo__ = p2
    
    def __str__(self):
        return "{p1}\n{p2}".format(p1=self.__playerOne__.__str__() ,p2= self.__playerTwo__.__str__())
    
    def getDisplay(self):
        return "{p1}/{p2}".format(p1=self.__playerOne__.getAbbrev(), p2=self.__playerTwo__.getAbbrev())
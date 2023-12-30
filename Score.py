class Score:
    # args: nSets, golden
    def __init__(self, nSets,nGames,tieTarget, golden):
        self.__sets__=[[0,0]] # result something like - [[6,4], [5,7], [7,6]]
        self.__currentGame__=[0,0]
        self.__tiebreaker__=[0,0]
        self.__overall__=[0,0]
        self.__nSets__=nSets
        self.__nGames__=nGames
        self.__golden__ = golden
        self.__scores__={0:0, 1:15, 2:30, 3:40, 4:'AD'}
        self.__tiebreakerMode__= False
        self.__tieTarget = tieTarget

    def newPoint(self, team):
        scorer = team - 1
        other = int(not scorer)
        gameResult = self.__applyToGame__(scorer, other)

        if self.__tiebreakerMode__:
            if self.__currentGame__[scorer] >= self.__tieTarget and self.__currentGame__[scorer] - self.__currentGame__[other] >=2:
                self.__sets__[-1][scorer]+=1
                result = self.__setWon__(scorer)
                return result
            else:
                return 0

        if gameResult:
            self.__currentGame__ = [0,0]
            setResult = self.__gameWon__(scorer, other)
            if setResult:
                result = self.__setWon__(scorer)
                if result:
                    return 1
        return 0

    def __setWon__(self, scorer):
        self.__overall__[scorer]+=1
        if self.__overall__[scorer] == self.__nSets__ // 2 + 1:
            return 1
        self.__sets__.append([0,0])
        return 0
        
        
    def __gameWon__(self, scorer, other):
        if self.__sets__[-1][scorer] - self.__sets__[-1][other] >= 1 and self.__sets__[-1][scorer] >= self.__nGames__-1:
            self.__sets__[-1][scorer]+=1
            return 1

        if self.__sets__[-1][scorer] == self.__nGames__-1 and self.__sets__[-1][other] == self.__nGames__:
            self.__sets__[-1][scorer]+=1
            self.__tiebreakerMode__=True
            return 0
        
        self.__sets__[-1][scorer]+=1
        return 0
        

            

    def __applyToGame__(self, scorer, other):
        if self.__tiebreakerMode__:
            self.__currentGame__[scorer]+=1
            return 0
        if self.__currentGame__[scorer] == 3 and self.__golden__:
            self.__currentGame__[scorer] += 1
            return 1 ## won game
        if self.__currentGame__[scorer] == 3 and self.__currentGame__[other] == 4 and not self.__golden__:
            self.__currentGame__[other]-=1
            return 0 ## nothing happened
        if self.__currentGame__[scorer] == 3 and self.__currentGame__[other] < 3:
            return 1
        if self.__currentGame__[scorer] == 4 and self.__currentGame__[other] == 3:
            return 1 ## won game

        self.__currentGame__[scorer] += 1 
        return 0


    def getFinishedSets(self, team):
        team-=1
        result = []
        for i in range(len(self.__sets__)):
            result.append(self.__sets__[i][team])
        return result
    
    def getCurrGame(self, team):
        if self.__tiebreakerMode__:
            return self.__currentGame__[team-1]
        
        return self.__scores__[self.__currentGame__[team-1]]

class Player:
    def __init__(self, fname, lname):
        self.__first_name__ = fname
        self.__last_name__ = lname
        self.__abbrev__ = lname[0:3]
    
    def __str__(self):
        return "{name} {lastname} ({abbrev})".format(name=self.__first_name__,lastname= self.__last_name__,abbrev= self.__abbrev__) 
    
    def getAbbrev(self):
        return self.__abbrev__
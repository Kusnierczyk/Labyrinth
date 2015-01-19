from labyrinth.constants.Consts import Consts;

class ConstsValidator(object):
    
    minimalLabyrinthSize = 3;
    
    def __init__(self):
        pass;
    
    def checkLabyrinthSize(self):
        if (Consts.LABYRINTH_SIZE < self.minimalLabyrinthSize):
            raise BaseException("The labyrinth size must equal 3 or greater.");
            
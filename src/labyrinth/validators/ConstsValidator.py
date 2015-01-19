from labyrinth.constants.Consts import Consts;

class ConstsValidator(object):
    
    ## Defines minimum labyrinth size
    minimalLabyrinthSize = 3;
    
    ## ConstsValidator class constructor
    # @param self The object pointer  
    def __init__(self):
        pass;
    
    ## Checks if labyrinth size has correct value
    # @param self The object pointer  
    def checkLabyrinthSize(self):
        if (Consts.LABYRINTH_SIZE < self.minimalLabyrinthSize):
            raise BaseException("The labyrinth size must equal 3 or greater.");
            
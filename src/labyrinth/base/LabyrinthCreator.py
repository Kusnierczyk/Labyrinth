import random;
from labyrinth.constants.Consts import Consts;

class LabyrinthCreator(object):

    xEntrancePosition = 0;
    yEntrancePosition = 0;
    xExitPosition = 0;
    yExitPosition = 0;
    labyrinthArray = None;
    
    def __init__(self):
        self.labyrinthArray = [[0 for j in range (Consts.LABYRINTH_WIDTH)] 
                          for i in range (Consts.LABYRINTH_HEIGHT)];
    
    def initializeLabyrinth(self):
        for i in range(Consts.LABYRINTH_HEIGHT):
            for j in range(Consts.LABYRINTH_WIDTH):
                self.labyrinthArray[i][j] = Consts.LABYRINTH_WALL;
                
    def createLabyrinthEntrance(self):        
        self.xEntrancePosition = random.randrange(Consts.LABYRINTH_HEIGHT);
        if ((self.xEntrancePosition == 0) or (self.xEntrancePosition == Consts.LABYRINTH_HEIGHT - 1)):
            self.yEntrancePosition = random.randrange(Consts.LABYRINTH_WIDTH);
            self.labyrinthArray[self.xEntrancePosition][self.yEntrancePosition] = Consts.LABYRINTH_ENTRANCE;
        
        #Check if xEntrancePosition is between top and bottom labyrinth edge
        elif (self.xEntrancePosition in range(1, Consts.LABYRINTH_HEIGHT - 1)):
            if (random.random() < Consts.PROBABILITY):
                self.yEntrancePosition = 0;        
                self.labyrinthArray[self.xEntrancePosition][self.yEntrancePosition] = Consts.LABYRINTH_ENTRANCE;
            else:
                self.yEntrancePosition = Consts.LABYRINTH_WIDTH - 1;
                self.labyrinthArray[self.xEntrancePosition][self.yEntrancePosition] = Consts.LABYRINTH_ENTRANCE;
                
    def createLabyrinthExit(self):
        if (self.yEntrancePosition == 0):
            self.xExitPosition = random.randrange(Consts.LABYRINTH_HEIGHT);
            self.yExitPosition = Consts.LABYRINTH_WIDTH - 1;
            self.labyrinthArray[self.xExitPosition][self.yExitPosition] = Consts.LABYRINTH_EXIT;
        elif (self.yEntrancePosition == Consts.LABYRINTH_WIDTH - 1):
            self.xExitPosition = random.randrange(Consts.LABYRINTH_HEIGHT);
            self.yExitPosition = 0;
            self.labyrinthArray[self.xExitPosition][self.yExitPosition] = Consts.LABYRINTH_EXIT;
        elif (self.yEntrancePosition in range(1, self.LABYRINTH_WIDTH - 1)):
            self.xExitPosition = Consts.LABYRINTH_HEIGHT - 1;
            self.yExitPosition = random.randrange(Consts.LABYRINTH_WIDTH - 1);
            self.labyrinthArray[self.xExitPosition][self.yExitPosition] = Consts.LABYRINTH_EXIT;
    
    def show(self):
        print(self.labyrinthArray);

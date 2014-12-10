import random;

class LabyrinthCreator(object):

    LABYRINTH_HEIGHT = 20;
    LABYRINTH_WIDTH = 20;
    LABYRINTH_WALL = 0;
    LABYRINTH_ROAD = 1;
    LABYRINTH_ENTRANCE = 2;
    LABYRINTH_EXIT = 3;
    PROBABILITY = 0.5;
    xEntrancePosition = 0;
    yEntrancePosition = 0;
    xExitPosition = 0;
    yExitPosition = 0;
    labyrinthArray = None;
    
    
    def __init__(self):
        self.labyrinthArray = [[0 for j in range (self.LABYRINTH_WIDTH)] 
                          for i in range (self.LABYRINTH_HEIGHT)];
    
    def initializeLabyrinth(self):
        for i in range(self.LABYRINTH_HEIGHT):
            for j in range(self.LABYRINTH_WIDTH):
                self.labyrinthArray[i][j] = self.LABYRINTH_WALL;
                
    def createLabyrinthEntrance(self):        
        self.xEntrancePosition = random.randrange(self.LABYRINTH_HEIGHT);
        if ((self.xEntrancePosition == 0) or (self.xEntrancePosition == self.LABYRINTH_HEIGHT - 1)):
            self.yEntrancePosition = random.randrange(self.LABYRINTH_WIDTH);
            self.labyrinthArray[self.xEntrancePosition][self.yEntrancePosition] = self.LABYRINTH_ENTRANCE;
        elif (self.xEntrancePosition in range(1, self.LABYRINTH_HEIGHT - 1)):
            if (random.random() < self.PROBABILITY):
                self.yEntrancePosition = 0;        
                self.labyrinthArray[self.xEntrancePosition][self.yEntrancePosition] = self.LABYRINTH_ENTRANCE;
            else:
                self.yEntrancePosition = self.LABYRINTH_WIDTH - 1;
                self.labyrinthArray[self.xEntrancePosition][self.yEntrancePosition] = self.LABYRINTH_ENTRANCE;
                
    def createLabyrinthExit(self):
        if (self.yEntrancePosition == 0):
            self.xExitPosition = random.randrange(self.LABYRINTH_HEIGHT);
            self.yExitPosition = self.LABYRINTH_WIDTH - 1;
            self.labyrinthArray[self.xExitPosition][self.yExitPosition] = self.LABYRINTH_EXIT;
        elif (self.yEntrancePosition == self.LABYRINTH_WIDTH - 1):
            self.xExitPosition = random.randrange(self.LABYRINTH_HEIGHT);
            self.yExitPosition = 0;
            self.labyrinthArray[self.xExitPosition][self.yExitPosition] = self.LABYRINTH_EXIT;
        elif (self.yEntrancePosition in range(1, self.LABYRINTH_WIDTH - 1)):
            self.xExitPosition = self.LABYRINTH_HEIGHT - 1;
            self.yExitPosition = random.randrange(self.LABYRINTH_WIDTH - 1);
            self.labyrinthArray[self.xExitPosition][self.yExitPosition] = self.LABYRINTH_EXIT;
    
    def show(self):
        print(self.labyrinthArray);

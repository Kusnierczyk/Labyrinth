import numpy;
import random;
from labyrinth.constants.Consts import Consts;

class LabyrinthCreator(object):

    xEntrancePosition = 0;
    yEntrancePosition = 0;
    xExitPosition = 0;
    yExitPosition = 0;
    labyrinthArray = None;
    
    def __init__(self):
        pass;
    
    def initializeLabyrinth(self):
        self.labyrinthArray = numpy.zeros((Consts.LABYRINTH_WIDTH, Consts.LABYRINTH_HEIGHT), dtype=numpy.int);
                
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
        if ((self.xEntrancePosition == 0) and
                (self.yEntrancePosition in range(Consts.LABYRINTH_WIDTH))):
            self.xExitPosition = Consts.LABYRINTH_HEIGHT - 1; 
            self.yExitPosition = random.randrange(Consts.LABYRINTH_WIDTH);
            self.labyrinthArray[self.xExitPosition][self.yExitPosition] = Consts.LABYRINTH_EXIT;
        elif ((self.xEntrancePosition == Consts.LABYRINTH_HEIGHT - 1) and 
                (self.yEntrancePosition in range(Consts.LABYRINTH_WIDTH))):
            self.xExitPosition = 0;
            self.yExitPosition = random.randrange(Consts.LABYRINTH_WIDTH);
            self.labyrinthArray[self.xExitPosition][self.yExitPosition] = Consts.LABYRINTH_EXIT;
        elif ((self.xEntrancePosition in range(1, Consts.LABYRINTH_HEIGHT - 1)) and
                (self.yEntrancePosition == 0)):
            self.xExitPosition = random.randrange(Consts.LABYRINTH_HEIGHT);
            self.yExitPosition = Consts.LABYRINTH_WIDTH - 1;
            self.labyrinthArray[self.xExitPosition][self.yExitPosition] = Consts.LABYRINTH_EXIT;
        elif ((self.xEntrancePosition in range(1, Consts.LABYRINTH_HEIGHT - 1)) and
                (self.yEntrancePosition == Consts.LABYRINTH_WIDTH - 1)):
            self.xExitPosition = random.randrange(Consts.LABYRINTH_HEIGHT);
            self.yExitPosition = 0;
            self.labyrinthArray[self.xExitPosition][self.yExitPosition] = Consts.LABYRINTH_EXIT;
        else:
            raise BaseException("ERROR");
    
    def createRoadBetweenEntranceAndExit(self):
        numberOfRotations = self.checkIfLabyrinthArrayRotationIsRequired();
        self.rotateArray(self.labyrinthArray, numberOfRotations);
        self.updateEntranceExitPosition(self.findElementInLabyrinthArray(Consts.LABYRINTH_ENTRANCE),
                                        self.findElementInLabyrinthArray(Consts.LABYRINTH_EXIT));
        currentX = self.xEntrancePosition;
        currentY = self.yEntrancePosition;
        newX = currentX;
        newY = self.generateRandomValue(currentY);
        self.connectPoints(currentX, currentY, newX, newY);
        
        while (newX != self.xExitPosition - 1):
            currentX = newX;
            currentY = newY;
            newX += 1;
            self.connectPoints(currentX, currentY, newX, newY);
            currentX += 1;
            newY = self.generateRandomValue(newY);
            self.connectPoints(currentX, currentY, newX, newY);
        
        self.connectPoints(newX, newY, self.xExitPosition, newY);
        newX += 1;
        self.connectPoints(newX, newY, self.xExitPosition, self.yExitPosition);
        self.rotateArray(self.labyrinthArray, 4 - numberOfRotations);
        self.updateEntranceExitPosition(self.findElementInLabyrinthArray(Consts.LABYRINTH_ENTRANCE),
                                        self.findElementInLabyrinthArray(Consts.LABYRINTH_EXIT));
        
    def generateRandomValue(self, currentValue):
        newValue = random.randrange(0, Consts.LABYRINTH_WIDTH);
        while (newValue == currentValue):
            newValue = random.randrange(0, Consts.LABYRINTH_WIDTH);
        return newValue;
    
    def connectPoints(self, startX, startY, stopX, stopY):    
        while (startY != stopY):
            if (stopY > startY):            #We are going to the right
                startY += 1;
                self.labyrinthArray[startX][startY] = Consts.LABYRINTH_ROAD;
            elif (stopY < startY):          #We are going to the left
                startY -= 1;
                self.labyrinthArray[startX][startY] = Consts.LABYRINTH_ROAD;
        
        if ((stopX == self.xExitPosition) and (stopY == self.yExitPosition)):
            self.labyrinthArray[stopX][stopY] = Consts.LABYRINTH_EXIT;
        else:
            self.labyrinthArray[stopX][stopY] = Consts.LABYRINTH_ROAD;
    
    def checkIfLabyrinthArrayRotationIsRequired(self):
        ''' nie zadziala dobrze dla przypadku II '''
        numberOfRotations = 0;
        if ((self.yEntrancePosition == 0) and 
        (self.xEntrancePosition in range(1, Consts.LABYRINTH_HEIGHT - 1))): 
            ''' przypadek III --> obrot o 90 w prawo '''
            numberOfRotations = 3;
        elif (self.xEntrancePosition == Consts.LABYRINTH_WIDTH - 1):
            ''' przypadek IV --> obrot o 180 w prawo '''
            numberOfRotations = 2;
        elif (self.yEntrancePosition == Consts.LABYRINTH_WIDTH - 1):
            ''' przypadek V --> obrot o 270 w prawo '''
            numberOfRotations = 1;
        else:
            numberOfRotations = 0;
        return numberOfRotations;
    
    def rotateArray(self, labArray, numberOfRotations):
        self.labyrinthArray = numpy.rot90(labArray, numberOfRotations);
    
    def findElementInLabyrinthArray(self, value):
        for row in range(Consts.LABYRINTH_WIDTH):
            for column in range(Consts.LABYRINTH_HEIGHT):
                if (self.labyrinthArray[row][column] == value):
                    return row, column;
        return -1;
    
    def updateEntranceExitPosition(self, entrancePosition, exitPosition):
        self.xEntrancePosition = entrancePosition[0];
        self.yEntrancePosition = entrancePosition[1];
        self.xExitPosition = exitPosition[0];
        self.yExitPosition = exitPosition[1];
    
    def show(self):
        print(self.labyrinthArray);
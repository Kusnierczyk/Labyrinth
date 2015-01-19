import numpy;
import random;
from labyrinth.constants.Consts import Consts;

class LabyrinthCreator(object):
    
    ## Defines labyrinth entrance position on X axis
    xEntrancePosition = 0;
    
    ## Defines labyrinth entrance position on Y axis
    yEntrancePosition = 0;
    
    ## Defines labyrinth exit position on X axis
    xExitPosition = 0;
    
    ## Defines labyrinth exit position on Y axis
    yExitPosition = 0;
    
    ## Defines labyrinth array which represents labyrinth
    labyrinthArray = None;

    ## LabyrinthCreator class constructor
    # @param self The object pointer     
    def __init__(self):
        pass;
    
    ## Creates and initializes with 0 value labyrinth array
    # @param self The object pointer 
    def initializeLabyrinth(self):
        self.labyrinthArray = numpy.zeros((Consts.LABYRINTH_SIZE, Consts.LABYRINTH_SIZE), dtype=numpy.int);
                
    ## Creates labyrinth entrance
    # @param self The object pointer
    def createLabyrinthEntrance(self):        
        self.xEntrancePosition = random.randrange(Consts.LABYRINTH_SIZE);
        if ((self.xEntrancePosition == 0) or (self.xEntrancePosition == Consts.LABYRINTH_SIZE - 1)):
            self.yEntrancePosition = random.randrange(Consts.LABYRINTH_SIZE);
            self.labyrinthArray[self.xEntrancePosition][self.yEntrancePosition] = Consts.LABYRINTH_ENTRANCE;
        
        #Check if xEntrancePosition is between top and bottom labyrinth edge
        elif (self.xEntrancePosition in range(1, Consts.LABYRINTH_SIZE - 1)):
            if (random.random() < Consts.PROBABILITY):
                self.yEntrancePosition = 0;        
                self.labyrinthArray[self.xEntrancePosition][self.yEntrancePosition] = Consts.LABYRINTH_ENTRANCE;
            else:
                self.yEntrancePosition = Consts.LABYRINTH_SIZE - 1;
                self.labyrinthArray[self.xEntrancePosition][self.yEntrancePosition] = Consts.LABYRINTH_ENTRANCE;
                
    ## Creates labyrinth exit
    # @param self The object pointer
    def createLabyrinthExit(self):
        if ((self.xEntrancePosition == 0) and
                (self.yEntrancePosition in range(Consts.LABYRINTH_SIZE))):
            self.xExitPosition = Consts.LABYRINTH_SIZE - 1; 
            self.yExitPosition = random.randrange(Consts.LABYRINTH_SIZE);
            self.labyrinthArray[self.xExitPosition][self.yExitPosition] = Consts.LABYRINTH_EXIT;
        elif ((self.xEntrancePosition == Consts.LABYRINTH_SIZE - 1) and 
                (self.yEntrancePosition in range(Consts.LABYRINTH_SIZE))):
            self.xExitPosition = 0;
            self.yExitPosition = random.randrange(Consts.LABYRINTH_SIZE);
            self.labyrinthArray[self.xExitPosition][self.yExitPosition] = Consts.LABYRINTH_EXIT;
        elif ((self.xEntrancePosition in range(1, Consts.LABYRINTH_SIZE - 1)) and
                (self.yEntrancePosition == 0)):
            self.xExitPosition = random.randrange(Consts.LABYRINTH_SIZE);
            self.yExitPosition = Consts.LABYRINTH_SIZE - 1;
            self.labyrinthArray[self.xExitPosition][self.yExitPosition] = Consts.LABYRINTH_EXIT;
        elif ((self.xEntrancePosition in range(1, Consts.LABYRINTH_SIZE - 1)) and
                (self.yEntrancePosition == Consts.LABYRINTH_SIZE - 1)):
            self.xExitPosition = random.randrange(Consts.LABYRINTH_SIZE);
            self.yExitPosition = 0;
            self.labyrinthArray[self.xExitPosition][self.yExitPosition] = Consts.LABYRINTH_EXIT;
        else:
            raise BaseException("ERROR");
    
    ## Creates road between entrance and exit
    # @param self The object pointer
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
        
    ## Generate new value using random library
    # @param self The object pointer
    # @param currentValue Current value
    # @return newValue Value which not equals to currentValue
    def generateRandomValue(self, currentValue):
        newValue = random.randrange(0, Consts.LABYRINTH_SIZE);
        while (newValue == currentValue):
            newValue = random.randrange(0, Consts.LABYRINTH_SIZE);
        return newValue;
    
    ## Creates road between two points
    # @param self The object pointer
    # @param startX Start position on X axis
    # @param startY Start position on Y axis
    # @param stopX Stop position on X axis
    # @param stopY Stop position on Y axis
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
    
    ## Rotates labyrinth array using numpy.rot90 method
    # @param self The object pointer
    # @return numberOfRotations Number of rotations which should be made
    def checkIfLabyrinthArrayRotationIsRequired(self):
        numberOfRotations = 0;
        if ((self.yEntrancePosition == 0) and 
        (self.xEntrancePosition in range(1, Consts.LABYRINTH_SIZE - 1))): 
            'Rotation of 90 degrees in clockwise direction'
            numberOfRotations = 3;
        elif (self.xEntrancePosition == Consts.LABYRINTH_SIZE - 1):
            'Rotation of 180 degrees in clockwise direction'
            numberOfRotations = 2;
        elif (self.yEntrancePosition == Consts.LABYRINTH_SIZE - 1):
            'Rotation of 270 degrees in clockwise direction'
            numberOfRotations = 1;
        else:
            numberOfRotations = 0;
        return numberOfRotations;
    
    ## Rotates labyrinth array using numpy.rot90 method
    # @param self The object pointer
    # @param labArray Array which represents labyrinth
    # @param numberOfRotations Number of rotations which should be made
    def rotateArray(self, labArray, numberOfRotations):
        self.labyrinthArray = numpy.rot90(labArray, numberOfRotations);
    
    ## Rotates labyrinth array using numpy.rot90 method
    # @param self The object pointer
    # @param labArray Array which represents labyrinth
    # @return Tuple which contains (row, column) of searched element
    # If value has not been found method return -1
    def findElementInLabyrinthArray(self, value):
        for row in range(Consts.LABYRINTH_SIZE):
            for column in range(Consts.LABYRINTH_SIZE):
                if (self.labyrinthArray[row][column] == value):
                    return row, column;
        return -1;
    
    ## Updates entrance and exit position after labyrinth array rotation 
    # @param self The object pointer
    # @param entrancePosition Tuple which contains row and column of entrance 
    # @param exitPosition Tuple which contains row and column of exit 
    def updateEntranceExitPosition(self, entrancePosition, exitPosition):
        self.xEntrancePosition = entrancePosition[0];
        self.yEntrancePosition = entrancePosition[1];
        self.xExitPosition = exitPosition[0];
        self.yExitPosition = exitPosition[1];
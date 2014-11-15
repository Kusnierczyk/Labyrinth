import random;

LABYRINTH_HEIGHT = 5;
LABYRINTH_WIDTH = 3;
LABYRINTH_WALL = 0;
LABYRINTH_ROAD = 1;
LABYRINTH_ENTRANCE = 2;
LABYRINTH_EXIT = 3;
PROBABILITY = 0.5;
xEntrancePosition = 0;
yEntrancePosition = 0;
xExitPosition = 0;
yExitPosition = 0;

labyrinthArray = [[0 for j in range (LABYRINTH_WIDTH)] for i in range (LABYRINTH_HEIGHT)];

def initializeLabyrinth():
    global labyrinthArray;
    for i in range(LABYRINTH_HEIGHT):
        for j in range(LABYRINTH_WIDTH):
            labyrinthArray[i][j] = LABYRINTH_WALL;
            
def createLabyrinthEntrance():
    global labyrinthArray;
    global xEntrancePosition;
    global yEntrancePosition;
    
    xEntrancePosition = random.randrange(LABYRINTH_HEIGHT);
    if ((xEntrancePosition == 0) or (xEntrancePosition == LABYRINTH_HEIGHT - 1)):
        yEntrancePosition = random.randrange(LABYRINTH_WIDTH);
        labyrinthArray[xEntrancePosition][yEntrancePosition] = LABYRINTH_ENTRANCE;
    elif (xEntrancePosition in range(1, LABYRINTH_HEIGHT - 1)):
        if (random.random() < PROBABILITY):
            yEntrancePosition = 0;        
            labyrinthArray[xEntrancePosition][yEntrancePosition] = LABYRINTH_ENTRANCE;
        else:
            yEntrancePosition = LABYRINTH_WIDTH - 1;
            labyrinthArray[xEntrancePosition][yEntrancePosition] = LABYRINTH_ENTRANCE;

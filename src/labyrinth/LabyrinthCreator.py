LABYRINTH_HEIGHT = 5;
LABYRINTH_WIDTH = 3;
LABYRINTH_WALL = 0;
LABYRINTH_ROAD = 1;
LABYRINTH_ENTRANCE = 2;
LABYRINTH_EXIT = 3;
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
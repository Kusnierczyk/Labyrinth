from labyrinth.LabyrinthCreator import LabyrinthCreator;
from labyrinth.LabyrinthDisplayer import LabyrinthDisplayer

if __name__ == '__main__':
    labyrinthCreator = LabyrinthCreator();
    labyrinthDisplayer = LabyrinthDisplayer(labyrinthCreator.LABYRINTH_HEIGHT,
                                            labyrinthCreator.LABYRINTH_WIDTH);
    
    labyrinthCreator.initializeLabyrinth();
    labyrinthCreator.createLabyrinthEntrance();
    labyrinthCreator.createLabyrinthExit();
    labyrinthCreator.show();
    
    labyrinthDisplayer.showLabyrinth(labyrinthCreator.labyrinthArray, 
        labyrinthCreator.LABYRINTH_HEIGHT, labyrinthCreator.LABYRINTH_WIDTH, 
        labyrinthCreator.LABYRINTH_ENTRANCE, labyrinthCreator.LABYRINTH_EXIT,
        labyrinthCreator.LABYRINTH_ROAD, labyrinthCreator.LABYRINTH_WALL,
        labyrinthCreator.xEntrancePosition, labyrinthCreator.yEntrancePosition,
        labyrinthCreator.xExitPosition, labyrinthCreator.yExitPosition);
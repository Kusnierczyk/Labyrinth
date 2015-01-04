from labyrinth.base.LabyrinthCreator import LabyrinthCreator;
from labyrinth.constants.Consts import Consts;
from labyrinth.display.LabyrinthDisplayer import LabyrinthDisplayer

if __name__ == '__main__':
    labyrinthCreator = LabyrinthCreator();
    labyrinthDisplayer = LabyrinthDisplayer(Consts.LABYRINTH_HEIGHT,
                                            Consts.LABYRINTH_WIDTH);
    
    labyrinthCreator.initializeLabyrinth();
    labyrinthCreator.createLabyrinthEntrance();
    labyrinthCreator.createLabyrinthExit();
    labyrinthCreator.show();
    
    labyrinthDisplayer.showLabyrinth(Consts.LABYRINTH_HEIGHT, Consts.LABYRINTH_WIDTH, 
        Consts.LABYRINTH_ENTRANCE, Consts.LABYRINTH_EXIT, Consts.LABYRINTH_ROAD, 
        Consts.LABYRINTH_WALL, labyrinthCreator.labyrinthArray,
        labyrinthCreator.xEntrancePosition, labyrinthCreator.yEntrancePosition,
        labyrinthCreator.xExitPosition, labyrinthCreator.yExitPosition);
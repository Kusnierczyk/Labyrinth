from labyrinth.base.LabyrinthCreator import LabyrinthCreator;
from labyrinth.constants.Consts import Consts;
from labyrinth.display.LabyrinthDisplayer import LabyrinthDisplayer
from labyrinth.road.RoadFinder import RoadFinder;

if __name__ == '__main__':

    labyrinthCreator = LabyrinthCreator();
    roadFinder = RoadFinder();
    labyrinthDisplayer = LabyrinthDisplayer(Consts.LABYRINTH_HEIGHT, Consts.LABYRINTH_WIDTH);

    labyrinthCreator.initializeLabyrinth();
    labyrinthCreator.createLabyrinthEntrance();
    labyrinthCreator.createLabyrinthExit();
    labyrinthCreator.show();
    labyrinthCreator.createRoadBetweenEntranceAndExit();
    labyrinthCreator.show();
    
    roadFinder.searchRoad(labyrinthCreator.labyrinthArray,labyrinthCreator.xEntrancePosition,
                          labyrinthCreator.yEntrancePosition, labyrinthCreator.xExitPosition,
                          labyrinthCreator.yExitPosition);
    
    labyrinthCreator.show();    
    roadFinder.clearFlagsAfterRoadSearch(labyrinthCreator.labyrinthArray, 
                                         labyrinthCreator.xExitPosition, 
                                         labyrinthCreator.yExitPosition);
    labyrinthCreator.show();

    labyrinthDisplayer.showLabyrinth(labyrinthCreator.labyrinthArray,
        labyrinthCreator.xEntrancePosition, labyrinthCreator.yEntrancePosition,
        labyrinthCreator.xExitPosition, labyrinthCreator.yExitPosition);
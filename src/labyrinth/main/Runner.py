from labyrinth.base.LabyrinthCreator import LabyrinthCreator;
from labyrinth.constants.Consts import Consts;
from labyrinth.display.LabyrinthDisplayer import LabyrinthDisplayer
from labyrinth.road.RoadFinder import RoadFinder;

class Runner(object):

    def __init__(self):
        pass;
    
    def run(self):
        labyrinthCreator = LabyrinthCreator();
        roadFinder = RoadFinder();
        labyrinthDisplayer = LabyrinthDisplayer(Consts.LABYRINTH_HEIGHT, Consts.LABYRINTH_WIDTH);
    
        labyrinthCreator.initializeLabyrinth();
        labyrinthCreator.createLabyrinthEntrance();
        labyrinthCreator.createLabyrinthExit();
        labyrinthCreator.createRoadBetweenEntranceAndExit();
        
        roadFinder.searchRoad(labyrinthCreator.labyrinthArray,labyrinthCreator.xEntrancePosition,
                              labyrinthCreator.yEntrancePosition, labyrinthCreator.xExitPosition,
                              labyrinthCreator.yExitPosition);
            
        roadFinder.clearFlagsAfterRoadSearch(labyrinthCreator.labyrinthArray, 
                                             labyrinthCreator.xExitPosition, 
                                             labyrinthCreator.yExitPosition);
    
        labyrinthDisplayer.showLabyrinth(labyrinthCreator.labyrinthArray,
            labyrinthCreator.xEntrancePosition, labyrinthCreator.yEntrancePosition,
            labyrinthCreator.xExitPosition, labyrinthCreator.yExitPosition);
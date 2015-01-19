from labyrinth.base.LabyrinthCreator import LabyrinthCreator;
from labyrinth.display.LabyrinthDisplayer import LabyrinthDisplayer
from labyrinth.road.RoadFinder import RoadFinder;
from labyrinth.validators.ConstsValidator import ConstsValidator

class Runner(object):

    ## Runner class constructor
    # @param self The object pointer 
    def __init__(self):
        pass;
    
    ## Creates main objects and invokes methods
    # @param self The object pointer 
    def run(self):
        constsValidator = ConstsValidator();
        constsValidator.checkLabyrinthSize();
        
        labyrinthCreator = LabyrinthCreator();
        roadFinder = RoadFinder();
        labyrinthDisplayer = LabyrinthDisplayer();
    
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
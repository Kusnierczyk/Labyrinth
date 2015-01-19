class Consts(object):
    
    ''' 
    This const must be an integer
    Minimal value is 3
    '''
    ## Defines labyrinth width and height
    LABYRINTH_SIZE = 5;
    
    ''' 
    This const must be an integer
    Recommended value is 0 
    '''
    ## Defines labyrinth wall
    LABYRINTH_WALL = 0;
    
    ''' 
    This const must be an integer
    Recommended value is 1 
    '''
    ## Defines labyrinth road
    LABYRINTH_ROAD = 1;
    
    ''' 
    This const must be an integer
    Recommended value is 2 
    '''
    ## Defines labyrinth best road
    LABYRINTH_BEST_ROAD = 2
    
    ''' 
    This const must be an integer
    Recommended value is 3 
    '''
    ## Defines labyrinth entrance
    LABYRINTH_ENTRANCE = 3;
    
    ''' 
    This const must be an integer
    Recommended value is 4 
    '''
    ## Defines labyrinth exit
    LABYRINTH_EXIT = 4;
    
    ''' 
    This const must be an integer
    Recommended value is 5 
    '''
    ## Defines labyrinth road left direction
    LABYRINTH_ROAD_LEFT = 5;
    
    ''' 
    This const must be an integer
    Recommended value is 6 
    '''
    ## Defines labyrinth road right direction
    LABYRINTH_ROAD_RIGHT = 6;
    
    ''' 
    This const must be an integer
    Recommended value is 7 
    '''
    ## Defines labyrinth road up direction
    LABYRINTH_ROAD_UP = 7;
    
    ''' 
    This const must be an integer
    Recommended value is 8 
    '''
    ## Defines labyrinth road down direction
    LABYRINTH_ROAD_DOWN = 8;
    
    ''' 
    This const should be float or double
    Recommended value is 0.5 
    '''
    ## Defines probability of some events
    PROBABILITY = 0.5;
    
    ## Consts class constructor
    # @param self The object pointer 
    def __init__(self):
        pass;
        
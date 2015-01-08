import pygame;
import os;
from labyrinth.constants.Consts import Consts;

class LabyrinthDisplayer(object):
    
    ## Defines labyrinth wall image name
    LABYRINTH_WALL_IMAGE = "wall.png";

    ## Defines labyrinth road image name
    LABYRINTH_ROAD_IMAGE = "road.png";
    
    ## Defines labyrinth best road image name
    LABYRINTH_BEST_ROAD = "bestRoad.png"
    
    ## Defines labyrinth entrance image name
    LABYRINTH_ENTRANCE_IMAGE = "entrance.png";
    
    ## Defines labyrinth exit image name
    LABYRINTH_EXIT_IMAGE = "exit.png";
    
    ## Defines source project folder name
    SOURCE_FOLDER_NAME = "src";
    
    ## Defines images folder name
    IMAGES_FOLDER_NAME = "images";
    
    ## Defines images height
    IMAGE_HEIGHT = 20;
    
    ## Defines images width
    IMAGE_WIDTH = 20;
    
    ## Defines labyrinth wall image
    wallImage = None;
    
    ## Defines labyrinth road image
    roadImage = None;
    
    ## Defines labyrinth best road image
    bestRoadImage = None;
    
    ## Defines labyrinth entrance image
    entranceImage = None;
    
    ## Defines labyrinth exit image
    exitImage = None;
    
    ## Defines window size
    screenSize = None;
    
    ## Defines window background
    screenBackgroundColour = (255,255,255);
    
    ## Defines flag if program is running
    running = False;

    ## LabyrinthDisplayer class constructor
    # @param self The object pointer
    # @param labyrinthHeight Labyrinth height
    # @param labyrinthWidth Labyrinth width
    def __init__(self, labyrinthHeight, labyrinthWidth):
        self.screenSize = (labyrinthHeight * self.IMAGE_HEIGHT, 
                           labyrinthWidth * self.IMAGE_WIDTH);
        pygame.init();
        self.surface = pygame.display.set_mode(self.screenSize, pygame.DOUBLEBUF);
        pygame.display.set_caption("Labyrinth");
        self.surface.fill(self.screenBackgroundColour);
        self.entranceImage = self.loadImage(self.prepareImagePath(self.LABYRINTH_ENTRANCE_IMAGE));
        self.exitImage = self.loadImage(self.prepareImagePath(self.LABYRINTH_EXIT_IMAGE));
        self.bestRoadImage = self.loadImage(self.prepareImagePath(self.LABYRINTH_BEST_ROAD));
        self.roadImage = self.loadImage(self.prepareImagePath(self.LABYRINTH_ROAD_IMAGE));
        self.wallImage = self.loadImage(self.prepareImagePath(self.LABYRINTH_WALL_IMAGE));
        
    ## Waits for quit event and then closes it
    # @param self The object pointer 
    def displayLoop(self):
        while not self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = True
        pygame.quit();        
         
    ## Loads image from disk
    # @param self The object pointer
    # @param path Path to image
    # @return Loaded image        
    def loadImage(self, path):
        image = pygame.image.load(path).convert_alpha();
        return image;
    
    ## Prepares image path
    # @param self The object pointer
    # @param imageName Image name
    # @return Prepared path       
    def prepareImagePath(self, imageName):
        path = os.getcwd();
        index = path.rfind(self.SOURCE_FOLDER_NAME);
        path = path[0 : index] + self.IMAGES_FOLDER_NAME + "\\" + imageName;
        return path;
    
    ## Displays labyrinth using pygame library
    # @param self The object pointer
    # @param labyrinthArray Array which represents labyrinth
    # @param xEntrancePosition Entrance position on X axis
    # @param yEntrancePosition Entrance position on Y axis
    # @param xExitPosition Exit position on X axis
    # @param yExitPosition Exit position on Y axis
    def showLabyrinth(self, labyrinthArray, xEntrancePosition, yEntrancePosition, 
                    xExitPosition, yExitPosition):
        
        pygame.display.flip();
        
        for i in range(Consts.LABYRINTH_HEIGHT):
            for j in range(Consts.LABYRINTH_WIDTH):
                if (labyrinthArray[i][j] == Consts.LABYRINTH_ROAD):
                    self.surface.blit(self.roadImage, (j * self.IMAGE_WIDTH, 
                                                   i * self.IMAGE_HEIGHT));
                                                   
                elif (labyrinthArray[i][j] == Consts.LABYRINTH_BEST_ROAD):
                    self.surface.blit(self.bestRoadImage, (j * self.IMAGE_WIDTH,
                                                           i * self.IMAGE_HEIGHT));
                                                           
                else:
                    self.surface.blit(self.wallImage, (j * self.IMAGE_WIDTH, 
                                                   i * self.IMAGE_HEIGHT));
                
        self.surface.blit(self.entranceImage, (yEntrancePosition * self.IMAGE_WIDTH, 
        xEntrancePosition * self.IMAGE_HEIGHT));
        self.surface.blit(self.exitImage, (yExitPosition * self.IMAGE_WIDTH, 
        xExitPosition * self.IMAGE_HEIGHT));
        pygame.display.flip();
        self.displayLoop();
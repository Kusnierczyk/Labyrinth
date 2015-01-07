import pygame;
import os;
from labyrinth.constants.Consts import Consts;

class LabyrinthDisplayer(object):
    LABYRINTH_ENTRANCE_IMAGE = "entrance.png";
    LABYRINTH_EXIT_IMAGE = "exit.png";
    LABYRINTH_BEST_ROAD = "bestRoad.png"
    LABYRINTH_ROAD_IMAGE = "road.png";
    LABYRINTH_WALL_IMAGE = "wall.png";
    SOURCE_FOLDER_NAME = "src";
    IMAGES_FOLDER_NAME = "images";
    IMAGE_HEIGHT = 20;
    IMAGE_WIDTH = 20;
    entranceImage = None;
    exitImage = None;
    bestRoadImage = None;
    roadImage = None;
    wallImage = None;
    screenSize = None;
    screenBackgroundColour = (255,255,255);
    running = False;

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
        
    def displayLoop(self):
        while not self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = True
        pygame.quit();        
         
    def loadImage(self, path):
        image = pygame.image.load(path).convert_alpha();
        return image;
    
    def prepareImagePath(self, imageName):
        path = os.getcwd();
        index = path.rfind(self.SOURCE_FOLDER_NAME);
        path = path[0 : index] + self.IMAGES_FOLDER_NAME + "\\" + imageName;
        return path;
    
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
import pygame;

class LabyrinthDisplayer(object):
    LABYRINTH_ENTRANCE_IMAGE = "entrance.png";
    LABYRINTH_EXIT_IMAGE = "exit.png";
    LABYRINTH_BEST_ROAD = "bestRoad.png"
    LABYRINTH_ROAD_IMAGE = "road.png";
    LABYRINTH_WALL_IMAGE = "wall.png";
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
        
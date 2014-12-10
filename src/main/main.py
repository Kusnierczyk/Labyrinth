from labyrinth import LabyrinthCreator

if __name__ == '__main__':
    labyrinthCreator = LabyrinthCreator();
    labyrinthCreator.initializeLabyrinth();
    labyrinthCreator.createLabyrinthEntrance();
    labyrinthCreator.createLabyrinthExit();
    labyrinthCreator.showLabyrinth();    
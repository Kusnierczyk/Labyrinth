from labyrinth.constants.Consts import Consts;
from collections import deque;

class RoadFinder(object):

    def __init__(self):
        pass;
    
    def searchRoad(self, labyrinthArray, xEntrancePosition, yEntrancePosition, 
               xExitPosition, yExitPosition):
    
        vertexQueue = deque();
        ' Set labyrinth exit as road '
        labyrinthArray[xExitPosition][yExitPosition] = Consts.LABYRINTH_ROAD;
        
        'Oznaczamy wierzcholek wejscia jako odwiedzony i wrzucamy do kolejki'
        vertexQueue.append(xEntrancePosition);
        vertexQueue.append(yEntrancePosition);
        
        '__len__() zwraca dlugosc'
        while (vertexQueue.__len__() != 0):
            tmpX = vertexQueue.popleft();
            tmpY = vertexQueue.popleft();
            
            'Sprawdzamy czy x i y pobranego punktu rowna sie x i y wyjscia'
            if ((tmpX == xExitPosition) and (tmpY == yExitPosition)):
                
                while ((labyrinthArray[tmpX][tmpY] != Consts.LABYRINTH_BEST_ROAD)
                       and (labyrinthArray[tmpX][tmpY] != Consts.LABYRINTH_ENTRANCE)):
                    
                    if (labyrinthArray[tmpX][tmpY] == Consts.LABYRINTH_ROAD_UP):
                        labyrinthArray[tmpX][tmpY] = Consts.LABYRINTH_BEST_ROAD;
                        tmpX += 1;
                    
                    elif (labyrinthArray[tmpX][tmpY] == Consts.LABYRINTH_ROAD_DOWN):
                        labyrinthArray[tmpX][tmpY] = Consts.LABYRINTH_BEST_ROAD;
                        tmpX -= 1;
                    
                    elif (labyrinthArray[tmpX][tmpY] == Consts.LABYRINTH_ROAD_LEFT):
                        labyrinthArray[tmpX][tmpY] = Consts.LABYRINTH_BEST_ROAD;
                        tmpY += 1;
                        
                    elif (labyrinthArray[tmpX][tmpY] == Consts.LABYRINTH_ROAD_RIGHT):
                        labyrinthArray[tmpX][tmpY] = Consts.LABYRINTH_BEST_ROAD;
                        tmpY -= 1;
            
            if ((tmpX - 1 >= 0) and
                (labyrinthArray[tmpX - 1][tmpY] == Consts.LABYRINTH_ROAD)):
                
                labyrinthArray[tmpX - 1][tmpY] = Consts.LABYRINTH_ROAD_UP;
                vertexQueue.append(tmpX - 1);
                vertexQueue.append(tmpY);
            
            if ((tmpX + 1 <= Consts.LABYRINTH_HEIGHT - 1) and
                (labyrinthArray[tmpX + 1][tmpY] == Consts.LABYRINTH_ROAD)):
                
                labyrinthArray[tmpX + 1][tmpY] = Consts.LABYRINTH_ROAD_DOWN;
                vertexQueue.append(tmpX + 1);
                vertexQueue.append(tmpY);
            
            if ((tmpY - 1 >= 0) and
                (labyrinthArray[tmpX][tmpY - 1] == Consts.LABYRINTH_ROAD)):
                
                labyrinthArray[tmpX][tmpY - 1] = Consts.LABYRINTH_ROAD_LEFT;
                vertexQueue.append(tmpX);
                vertexQueue.append(tmpY - 1);
            
            if ((tmpY + 1 <= Consts.LABYRINTH_WIDTH - 1) and
                (labyrinthArray[tmpX][tmpY + 1] == Consts.LABYRINTH_ROAD)):
                
                labyrinthArray[tmpX][tmpY + 1] = Consts.LABYRINTH_ROAD_RIGHT;
                vertexQueue.append(tmpX);
                vertexQueue.append(tmpY + 1);

    def clearFlagsAfterRoadSearch(self, labyrinthArray, xExitPosition, yExitPosition):
        for i in range(Consts.LABYRINTH_HEIGHT):
            for j in range(Consts.LABYRINTH_WIDTH):
                if (labyrinthArray[i][j] in range (Consts.LABYRINTH_ROAD_LEFT, Consts.LABYRINTH_ROAD_DOWN + 1)):
                    labyrinthArray[i][j] = Consts.LABYRINTH_ROAD;
        labyrinthArray[xExitPosition][yExitPosition] = Consts.LABYRINTH_EXIT;
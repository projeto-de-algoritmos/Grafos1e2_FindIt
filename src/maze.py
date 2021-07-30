from cell import Cell
import random
import pygame

WIDTH = 1000
HEIGHT = 1000
screen = pygame.display.set_mode((WIDTH, HEIGHT))


class Maze:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.path = []
        self.graph = self.__initGraph()

    def __initGraph(self):
        graph = []

        for i in range(self.rows):
            graph.append([])
            for j in range(self.columns):
                graph[i].append(Cell(i, j))
                self.__initGame(i, j)
        return graph

    def __initGame(self, x, y):
        
      

        WHITE = (255, 255, 255)
        GREEN = (0, 255, 0,)
        BLUE = (0, 0, 255)
        YELLOW = (255 ,255 ,0)
        w = 10
        x = x*w
        y = y*w
        
        pygame.draw.line(screen, YELLOW, [x, y], [x+w,y]) #up
        pygame.draw.line(screen, YELLOW, [x + w, y], [x+w, y+w]) #right
        pygame.draw.line(screen, YELLOW, [x + w, y+w], [x, y+w]) #down
        pygame.draw.line(screen, YELLOW, [x, y + w], [x, y]) #left
        pygame.display.update()

    def __checkNeighbour(self, neighbours, x, y):
        if x >= 0 and x < self.rows and y >= 0 and y < self.columns:
            neighbours.append((x, y))

    def findNeighbours(self, x, y):
        neighbours = []
        self.__checkNeighbour(neighbours, x + 1, y)
        self.__checkNeighbour(neighbours, x - 1, y)
        self.__checkNeighbour(neighbours, x, y + 1)
        self.__checkNeighbour(neighbours, x, y - 1)
        random.shuffle(neighbours)
        return neighbours

    def nodeVisited(self, node):
        return self.graph[node[0]][node[1]].visited

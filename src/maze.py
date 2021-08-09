from cell import Cell
import random

class Maze:
    def __init__(self, size):
        self.rows, self.columns = size
        self.graph = self.__initGraph()

    def __initGraph(self):
        graph = []

        for i in range(self.rows):
            graph.append([])
            for j in range(self.columns):
                graph[i].append(Cell(i, j))
        return graph

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

    def findPossiblePath(self, x, y):
        possiblePath = []
        if not self.graph[x][y].walls['up']:
            possiblePath.append((x - 1, y))
        if not self.graph[x][y].walls['down']:
            possiblePath.append((x + 1, y))
        if not self.graph[x][y].walls['right']:
            possiblePath.append((x, y + 1))
        if not self.graph[x][y].walls['left']:
            possiblePath.append((x, y - 1))
        return possiblePath

    def nodeVisited(self, node):
        return self.graph[node[0]][node[1]].visited

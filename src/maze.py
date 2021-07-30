from cell import Cell
import random

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

    def nodeVisited(self, node):
        return self.graph[node[0]][node[1]].visited

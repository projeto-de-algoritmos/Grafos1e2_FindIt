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

    def nodeVisited(self, node):
        return self.graph[node[0]][node[1]].visited

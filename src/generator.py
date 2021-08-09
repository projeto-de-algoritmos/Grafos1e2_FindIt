from graphics import *
import random

def mazeGenerator(maze, startPoint, RANDOM_STACK):
    x_c, y_c = startPoint
    stack = []
    maze.graph[x_c][y_c].visited = True

    stack.append((x_c, y_c))
    RGB = changeColor([60, 0, 255, '+', 0, 1])
    gameDrawMaze(maze.graph[x_c][y_c], [255, 255, 255])
    while stack:
        if RANDOM_STACK:
            random.shuffle(stack)
        x_c, y_c = stack.pop()
        neighbours = maze.findNeighbours(x_c, y_c)

        if neighbours is not None:
            RGB = changeColor(RGB)
            for n in neighbours:
                if not maze.nodeVisited(n):
                    x_n, y_n = n
                    maze.graph[x_c][y_c].breackWalls(x_n, y_n)
                    maze.graph[x_n][y_n].breackWalls(x_c, y_c)
                    maze.graph[n[0]][n[1]].visited = True
                    gameDrawMaze(maze.graph[x_n][y_n], RGB[0:3])
                    stack.append(n)

from maze import Maze
from graphics import *
from constants import FPS, RANDOM_STACK
import pygame , time, random

def DFSmaze(maze, startPoint):
    x_c, y_c = startPoint
    path = []
    stack = []
    maze.graph[x_c][y_c].visited = True

    stack.append((x_c, y_c))
    path.append((x_c, y_c))
    RGB = changeColor([60, 0, 255, '+', 0, 1])
    gameCurrentNode(maze.graph[x_c][y_c], RGB[0:3])
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
                    gameCurrentNode(maze.graph[x_n][y_n], RGB[0:3])
                    path.append(n)
                    stack.append(n)

    return path

clock = initGame()
maze = Maze(60, 60)
path = DFSmaze(maze, (0, 0))

running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

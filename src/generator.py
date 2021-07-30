from maze import Maze
from graphics import *
import pygame , time, random

FPS = 30

randomizeStack = True

def DFSmaze(maze, startPoint):
    x_c, y_c = startPoint
    path = []
    stack = []
    maze.graph[x_c][y_c].visited = True

    stack.append((x_c, y_c))
    path.append((x_c, y_c))
    while stack:
        if randomizeStack:
            random.shuffle(stack)
        x_c, y_c = stack.pop()
        neighbours = maze.findNeighbours(x_c, y_c)

        if neighbours is not None:
            for n in neighbours:
                if not maze.nodeVisited(n):
                    x_n, y_n = n
                    maze.graph[x_c][y_c].breackWalls(x_n, y_n)
                    maze.graph[x_n][y_n].breackWalls(x_c, y_c)
                    maze.graph[n[0]][n[1]].visited = True
                    path.append(n)
                    stack.append(n)
    return path

clock = initGame()
maze = Maze(50, 30)
path = DFSmaze(maze, (0, 0))

for node in path:
    gameCurrentNode(maze.graph[node[0]][node[1]])
    
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

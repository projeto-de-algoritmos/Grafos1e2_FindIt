from maze import Maze
from solver import mazeSolver
from graphics import *
from constants import FPS, RANDOM_STACK, SIZE, START
import pygame , time, random, threading




def mazeGenerator(maze, startPoint):
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

pygame.init()
pygame.mixer.init()
pygame.font.init()
return_Menu = menu()

if return_Menu[0] and not return_Menu[1]:
    RANDOM_STACK = False
elif not return_Menu[0] and return_Menu[1]:
    RANDOM_STACK = True

maze = Maze(SIZE)
mazeGenerator(maze, START)
path = mazeSolver(maze, (0, 0), (49, 49))

node = path[0]
while node[1] != (0, 0):
    gameDrawSolve(node[0], node[1], [255, 0, 0])
    node = [item for item in path if item[1] == node[0]][0]


#for node in range(1, len(path), 2):
#    gameDrawSolve(path[node-1], path[node], [255, 0, 0])


    
    
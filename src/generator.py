from maze import Maze
from solver import mazeSolver
from graphics import *
from constants import FPS, SIZE, START
import pygame , time, random, threading




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

clock = initGame()

return_Menu = menu()

RANDOM_STACK = return_Menu[0]
BFS_SEARCH = return_Menu[1]


pygame.display.set_mode((WIDTH, HEIGHT))

maze = Maze(SIZE)
mazeGenerator(maze, START, RANDOM_STACK)
path = mazeSolver(maze, (0, 0), (79, 39), BFS_SEARCH)

node = path[0]
while node[1] != (0, 0):
    gameDrawSolve(node[0], node[1], [255, 0, 0])
    node = [item for item in path if item[1] == node[0]][0]


running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    
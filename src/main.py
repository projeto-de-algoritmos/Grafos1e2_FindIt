from maze import Maze
from solver import *
from constants import SIZE, START, WIDTH, HEIGHT, FINAL
from graphics import *
from generator import *
import pygame
from time import sleep
import os

# def main():
#     initGame()
#     pygame.display.set_mode((WIDTH, HEIGHT))
#     maze = Maze(SIZE)
#     #  mazeGenerator(maze, START, False)
#     #primGenerator(maze, START)
#     kruskalGenerator(maze)
#     path = mazeSolver(maze, START, FINAL , True)
#     path = aStarSolver(maze, START, FINAL)

#     node = path[0]
#     while node[1] != START:
#         gameDrawSolve(node[0], node[1], [255, 0, 0])
#         node = [item for item in path if item[1] == node[0]][0]

#     while True:
#         sleep(1)

def main():
    initGame()
    exit = False
    while not exit:
        return_Menu = menu()
        
        maze = Maze(SIZE)

        if not return_Menu:
            break

        if return_Menu[0] == 0:
            primGenerator(maze, START)
        elif return_Menu[0] == 1:
            kruskalGenerator(maze)
        elif return_Menu[0] == 2:
            mazeGenerator(maze, START, False)
        elif return_Menu[0] == 3:
            mazeGenerator(maze, START, True)
        

        if return_Menu[1] == 0:
            path = aStarSolver(maze, START, FINAL)
        elif return_Menu[1] == 1:
            path = path = mazeSolver(maze, START, FINAL , False)
        elif return_Menu[1] == 2:
            path = path = mazeSolver(maze, START, FINAL , True)

        
        pygame.display.set_mode((WIDTH, HEIGHT + 100))

        node = path[0]
        while node[1] != START:
            gameDrawSolve(node[0], node[1], [255, 0, 0])
            node = [item for item in path if item[1] == node[0]][0]
    
        exit = restart()

        if exit:
            break

if __name__ == '__main__':
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    main()

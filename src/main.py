from maze import Maze
from solver import mazeSolver
from graphics import *
from constants import FPS, SIZE, START
import pygame , time, random, threading
from generator import *

def main():
    
    clock = initGame()
    
    exit = False
    while not exit:
        return_Menu = menu()
        if not return_Menu:
            break


        RANDOM_STACK = return_Menu[0]
        BFS_SEARCH = return_Menu[1]
        
        pygame.display.set_mode((WIDTH, HEIGHT + 100))

        maze = Maze(SIZE)
        mazeGenerator(maze, START, RANDOM_STACK)
        path = mazeSolver(maze, START, (49, 79), BFS_SEARCH)

        node = path[0]
        while node[1] != START:
            gameDrawSolve(node[0], node[1], [255, 0, 0])
            node = [item for item in path if item[1] == node[0]][0]

        
        exit = restart()

        if not exit:
            break
    


if __name__ == '__main__':
    main()


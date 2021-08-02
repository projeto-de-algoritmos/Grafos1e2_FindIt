from graphics import *
from constants import *

def mazeSolver(maze, startPoint, finishPoint):
    x_c, y_c = startPoint
    path = []
    stack = []
    maze.graph[x_c][y_c].player = True

    stack.append((x_c, y_c))
    while stack:
        if False:
            random.shuffle(stack)

        x_c, y_c = stack.pop()
        path.append((x_c, y_c))
        if (x_c, y_c) == finishPoint:
            #  print(path)
            return path

        possiblePath = maze.findPossiblePath(x_c, y_c)
        if possiblePath is not None:
            for n in possiblePath:
                if not maze.graph[n[0]][n[1]].player:
                    x_n, y_n = n
                    maze.graph[x_n][y_n].player = True
                    gameDrawSolve((x_c, y_c), (x_n, y_n), [255, 255, 255])
                    stack.append(n)

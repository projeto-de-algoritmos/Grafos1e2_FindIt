from graphics import *

def mazeSolver(maze, startPoint, finishPoint, BFS_SEARCH):
    x_c, y_c = startPoint
    path = []
    stack = []
    maze.graph[x_c][y_c].player = True

    stack.append(((x_c, y_c), (x_c, y_c)))
    path.append(((x_c, y_c), (x_c, y_c)))
    while stack:
        a, c = stack.pop(0 if BFS_SEARCH else -1)
        x_c, y_c = c
        if not maze.graph[x_c][y_c].player:
            maze.graph[x_c][y_c].player = True
            path.insert(0, (a, c))

        if (x_c, y_c) == finishPoint:
            return path

        possiblePath = maze.findPossiblePath(x_c, y_c)
        if possiblePath is not None:
            for n in possiblePath:
                if not maze.graph[n[0]][n[1]].player:
                    x_n, y_n = n
                    gameDrawSolve((x_c, y_c), (x_n, y_n), [255, 255, 255])
                    stack.append([(x_c, y_c), n])

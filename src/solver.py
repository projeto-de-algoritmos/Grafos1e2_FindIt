from graphics import *
import heapq as hp

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

def calculateDistance(start_x, start_y, finish_x, finish_y):
    return (finish_x - start_x) ** 2 + (finish_y - start_y) ** 2

def aStarSolver(maze, startPoint, finishPoint):
    openList = []
    path = []
    # (F, (G, H), (start_x, start_y), (pai_x, pai_y))
    hp.heappush(openList, (0, (0, 0), startPoint, startPoint))

    while openList:
        _, _, (x_c, y_c), (x_n, y_n) = hp.heappop(openList)
        path.append(((x_c, y_c), (x_n, y_n)))
        gameDrawSolve((x_c, y_c), (x_n, y_n), [255, 255, 255])

        if (x_c, y_c) == finishPoint:
            return path

        possiblePath = maze.findPossiblePath(x_c, y_c)
        for n in possiblePath:
            if not maze.graph[x_c][y_c].player:
                output = [i for i, v in enumerate(openList) if v[2] == n]
                G = calculateDistance(n[0], n[1], finishPoint[0], finishPoint[1])
                F = calculateDistance(n[0], n[1], startPoint[0], startPoint[1])
                if not output:
                    hp.heappush(openList, (F, (G, F+G), n, (x_c, y_c)))
                else:
                    node = openList[output[0]]
                    if node[1][0] > G:
                       node[1][0] = G
                       node[0] = F
                       node[1][1] = node[0] + G
                       node[3] = (x_c, y_c)
                       hp.heapify(openList)
        maze.graph[x_c][y_c].player = True

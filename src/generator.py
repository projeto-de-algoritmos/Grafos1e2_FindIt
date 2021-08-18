from graphics import *
import random
import heapq as hp

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

def primGenerator(maze, startPoint):
    heap = []
    x_c, y_c = startPoint
    hp.heappush(heap, (0, startPoint, startPoint))

    RGB = changeColor([60, 0, 255, '+', 0, 1])
    gameDrawMaze(maze.graph[x_c][y_c], [255, 255, 255])
    while heap:
        _, (x_c, y_c), (x_n, y_n) = hp.heappop(heap)
        if not maze.graph[x_c][y_c].visited:
            maze.graph[x_c][y_c].visited = True
            neighbours = maze.findNeighboursHeap(x_c, y_c)
            for n in neighbours:
                if not maze.graph[n[0][0]][n[0][1]].visited:
                    hp.heappush(heap, (maze.graph[n[0][0]][n[0][1]].weight[n[1]], n[0], (x_c, y_c)))

            maze.graph[x_c][y_c].breackWalls(x_n, y_n)
            maze.graph[x_n][y_n].breackWalls(x_c, y_c)
            gameDrawMaze(maze.graph[x_c][y_c], RGB[0:3])
            RGB = changeColor(RGB)

def find(matrizUnionFind, node):
    while (node != matrizUnionFind[node[0]][node[1]][0]):
        node = matrizUnionFind[node[0]][node[1]][0]
    return node

def union(matrizUnionFind, nodeA, nodeB):
    if matrizUnionFind[nodeA[0]][nodeA[1]][1] < matrizUnionFind[nodeB[0]][nodeB[1]][1]:
        matrizUnionFind[nodeA[0]][nodeA[1]] = (nodeB, matrizUnionFind[nodeA[0]][nodeA[1]][1])
        matrizUnionFind[nodeB[0]][nodeB[1]] = (nodeB, 1 + matrizUnionFind[nodeA[0]][nodeA[1]][1])
    else:
        matrizUnionFind[nodeB[0]][nodeB[1]] = (nodeA, matrizUnionFind[nodeB[0]][nodeB[1]][1])
        matrizUnionFind[nodeA[0]][nodeA[1]] = (nodeA, 1 + matrizUnionFind[nodeB[0]][nodeB[1]][1])
    #print(matrizUnionFind[nodeA[0]][nodeA[1]][0], matrizUnionFind[nodeB[0]][nodeB[1]][0])

def kruskalGenerator(maze):
    heap = []
    matrizUnionFind = []
    RGB = changeColor([60, 0, 255, '+', 0, 1])

    for i in range(maze.rows):
        matrizUnionFind.append([])
        for j in range(maze.columns):
            matrizUnionFind[i].append(((i,j), 1))
            neighbours = maze.findNeighboursHeap(i,j)
            for n in neighbours:
                hp.heappush(heap, (maze.graph[n[0][0]][n[0][1]].weight[n[1]], (i,j), n[0]))
    

    while heap:
        _, (x_c, y_c), (x_n, y_n) = hp.heappop(heap)
        print("A = {}, B = {}".format((x_c, y_c), (x_n,y_n)))

        a = find(matrizUnionFind, (x_c, y_c))
        b = find(matrizUnionFind, (x_n, y_n))
        
        if a != b:
            maze.graph[x_c][y_c].breackWalls(x_n, y_n)
            maze.graph[x_n][y_n].breackWalls(x_c, y_c)
            
            union(matrizUnionFind, a, b)
            if maze.graph[x_n][y_n].visited:
                gameDrawMaze(maze.graph[x_n][y_n], RGB[0:3])

            gameDrawMaze(maze.graph[x_c][y_c], RGB[0:3])
            

            maze.graph[x_n][y_n].visited = True
            RGB = changeColor(RGB)
    
    
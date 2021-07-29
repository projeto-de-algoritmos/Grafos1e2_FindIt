from maze import Maze

def DFSmaze(maze, startPoint):
    x_c, y_c = startPoint
    path = []
    maze.graph[x_c][y_c].visited = True

    stack = [(x_c, y_c)]
    path.append((x_c, y_c))
    while stack:
        x_c, y_c = stack.pop()
        neighbours = maze.findNeighbours(x_c, y_c)

        if neighbours is not None:
            for n in neighbours:
                if not maze.nodeVisited(n):
                    x_n, y_n = n
                    maze.graph[x_c][x_c].breackWalls(x_n, y_n)
                    maze.graph[x_n][x_n].breackWalls(x_c, y_c)
                    maze.graph[n[0]][n[1]].visited = True
                    path.append(n)
                    stack.append(n)

    return path

qtd = 10
maze = Maze(qtd, qtd)
path = DFSmaze(maze, (0, 0))
print(path)
#  for i in range(qtd):
    #  for j in range(qtd):
  #        print(f'Node ({i}, {j}): {maze.graph[i][j].walls}')

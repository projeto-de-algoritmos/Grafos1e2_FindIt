from maze import Maze
import pygame , time, random

WIDTH = 1000
HEIGHT = 1000
FPS = 30

w = 40
w2 = 10

WHITE = (255, 255, 255)
GREEN = (0, 255, 0,)
BLUE = (0, 0, 255)
YELLOW = (255 ,255 ,0)
screen = pygame.display.set_mode((WIDTH, HEIGHT))

def DFSmaze(maze, startPoint):
    x_c, y_c = startPoint
    path = []

    stack = []

    maze.graph[x_c][y_c].visited = True

    stack.append((x_c, y_c))
    path.append((x_c, y_c))


    while stack:

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


def gameUp(x, y):
    x = x*w

    y = y*w
    pygame.draw.rect(screen, BLUE, (x+1, y, w-1, w-1), 0)
  
def gameDown(x, y):
    x = x*w
    y = y*w

    pygame.draw.rect(screen, BLUE, (x+1, y+1, w-1, w), 0)


def gameLeft(x, y):
    x = x*w
    y = y*w
    pygame.draw.rect(screen, BLUE, (x, y+1, w-1, w-1), 0)
 

def gameRight(x, y):
    x = x*w
    y = y*w
    
    pygame.draw.rect(screen, BLUE, (x+1, y+1, w, w-1), 0)
   
    
def gameCurrentNode(node):
    walls = node.walls

    if not walls["down"]:
        gameDown(node.x,node.y)
    if not walls["up"]:
        gameUp(node.x,node.y)
    if not walls["left"]:
        gameLeft(node.x,node.y)
    if not walls["right"]:
        gameRight(node.x,node.y)

    pygame.display.update()
    time.sleep(.05)

pygame.init()
pygame.mixer.init()
pygame.display.set_caption("Finder")
clock = pygame.time.Clock()



maze = Maze(w2, w2)
path = DFSmaze(maze, (0, 0))


for node in path:
    gameCurrentNode(maze.graph[node[0]][node[1]])
    
#for i in range(w2):
#    for j in range(w2):
#        print(f'Node ({i}, {j}): {maze.graph[i][j].walls}')

running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False




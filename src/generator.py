from maze import Maze
import pygame , time, random

WIDTH = 500
HEIGHT = 500
FPS = 30

x = 0
y = 0
w = 10

WHITE = (255, 255, 255)
GREEN = (0, 255, 0,)
BLUE = (0, 0, 255)
YELLOW = (255 ,255 ,0)
screen = pygame.display.set_mode((WIDTH, HEIGHT))

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
                    a = maze.graph[x_c][x_c].breackWalls(x_n, y_n)
                    if a == "down":
                        gameDown(x_c,y_c)
                    elif a == "up":
                        gameUp(x_c,y_c)
                    elif a == "left":
                        gameLeft(x_c,y_c)
                    elif a == "right":
                        gameRight(x_c, y_c)
                    maze.graph[x_n][x_n].breackWalls(x_c, y_c)
                    maze.graph[n[0]][n[1]].visited = True
                    path.append(n)
                    stack.append(n)

    return path


def gameUp(x, y):
    x = x*w
    y = y*w
    pygame.draw.rect(screen, BLUE, (x, y-w+1, 9, 9), 0)
    pygame.display.update()
    time.sleep(.05)

def gameDown(x, y):
    x = x*w
    y = y*w
    pygame.draw.rect(screen, BLUE, (x+1, y + 1, 9, 9), 0)
    pygame.display.update()
    time.sleep(.05)

def gameLeft(x, y):
    x = x*w
    y = y*w
    pygame.draw.rect(screen, BLUE, (x+1, y +1, 9, 9), 0)
    pygame.display.update()
    time.sleep(.05)

def gameRight(x, y):
    x = x*w
    y = y*w
    pygame.draw.rect(screen, BLUE, (x + 1, y + 1, 10, 10), 0)
    pygame.display.update()
    time.sleep(.05)
    
def gameCurrentNode(x, y):
    x = x*w
    y = y*w
    pygame.draw.rect(screen, GREEN, (x, y, w, w),0)
    pygame.display.update()
    time.sleep(.05)


pygame.init()
pygame.mixer.init()
pygame.display.set_caption("Finder")
clock = pygame.time.Clock()



maze = Maze(w, w)
path = DFSmaze(maze, (x, y))

running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


#for i in range(w):
#  for j in range(w):
#        print(f'Node ({i}, {j}): {maze.graph[i][j].walls}')

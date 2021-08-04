from pygame.constants import MOUSEBUTTONDOWN
from constants import CELL_SIZE, COLOR_CHANGE, WIDTH, HEIGHT
import pygame, time, random, sys

screen = pygame.display.set_mode((WIDTH, HEIGHT))
screenMenu = pygame.display.set_mode((800, 600))
click = False

def changeColor(color):
    if color[0:3] == [255, 255, 0] or color[0:3] == [255, 0, 255] or color[0:3] == [0, 255, 255]:
        color[3] = '-'
    elif color[0:3] == [255, 0, 0] or color[0:3] == [0, 0, 255] or color[0:3] == [0, 255, 0]:
        color[3] = '+'

    if color[0:3] == [0, 0, 255] or color[0:3] == [255, 255, 0]:
        color[4] = 0
    elif color[0:3] == [255, 0, 0] or color[0:3] == [0, 255, 255]:
        color[4] = 1
    if color[0:3] == [0, 255, 0] or color[0:3] == [255, 0, 255]:
        color[4] = 2

    if color[5] == COLOR_CHANGE:
        color[color[4]] += 1 if color[3] == '+' else -1
        color[5] = 1
    else:
        color[5] += 1
    return color

def drawCell(color, rectTuple):
    pygame.draw.rect(screen, color, rectTuple, 0)

def gameDrawMaze(node, color):
    y = (node.x * 2 + 1) * CELL_SIZE
    x = (node.y * 2 + 1) * CELL_SIZE
    walls = node.walls

    drawCell(color, (x, y, CELL_SIZE, CELL_SIZE))
    if not walls["down"]:
        drawCell(color, (x, y+CELL_SIZE, CELL_SIZE, CELL_SIZE))
    if not walls["up"]:
        drawCell(color, (x, y-CELL_SIZE, CELL_SIZE, CELL_SIZE))
    if not walls["left"]:
        drawCell(color, (x-CELL_SIZE, y, CELL_SIZE, CELL_SIZE))
    if not walls["right"]:
        drawCell(color, (x+CELL_SIZE, y, CELL_SIZE, CELL_SIZE))

    pygame.display.update()
    time.sleep(.001)

def gameDrawSolve(node_i, node_f, color):
    y_i = (node_i[0] * 2 + 1) * CELL_SIZE
    x_i = (node_i[1] * 2 + 1) * CELL_SIZE
    y_f = (node_f[0] * 2 + 1) * CELL_SIZE
    x_f = (node_f[1] * 2 + 1) * CELL_SIZE
    drawCell(color, (x_i, y_i, CELL_SIZE, CELL_SIZE))
    drawCell(color, (x_f, y_f, CELL_SIZE, CELL_SIZE))
    if x_f < x_i:
        drawCell(color, (x_f+CELL_SIZE, y_f, CELL_SIZE, CELL_SIZE))
    elif y_f < y_i:
        drawCell(color, (x_f, y_f+CELL_SIZE, CELL_SIZE, CELL_SIZE))
    elif x_f > x_i:
        drawCell(color, (x_i+CELL_SIZE, y_f, CELL_SIZE, CELL_SIZE))
    elif y_f > y_i:
        drawCell(color, (x_f, y_i+CELL_SIZE, CELL_SIZE, CELL_SIZE))

    pygame.display.update()
    time.sleep(.001)

def initGame():
    
    pygame.display.set_caption("Finder")
    return pygame.time.Clock()

def draw_Text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x,y)
    surface.blit(textobj, textrect)


def menu():
    click = False
    green_DFS = False
    green_BFS = False
    running = True
    font = pygame.font.SysFont(0, 60)
    button_dfs = pygame.Rect(50, 100, 50, 50)
    button_bfs = pygame.Rect(50, 200, 50, 50)
    pygame.draw.rect(screenMenu, (255, 255, 255), button_dfs)
    pygame.draw.rect(screenMenu, (255, 255, 255), button_bfs)

    button_dfs = pygame.Rect(55, 105, 40, 40)
    button_bfs = pygame.Rect(55, 205, 40, 40)
    pygame.draw.rect(screenMenu, (0, 0, 0), button_dfs)
    pygame.draw.rect(screenMenu, (0, 0, 0), button_bfs)

    button_Start = pygame.Rect(400, 450, 50, 50)
    pygame.draw.rect(screenMenu, (255, 0, 0), button_Start)
    draw_Text('Começar', font, (255, 255, 255), screenMenu, 470, 450)

    draw_Text('DFS', font, (255, 255, 255), screenMenu, 105, 105)
    draw_Text('BFS', font, (255, 255, 255), screenMenu, 105, 205)

    while running:
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if button_dfs.collidepoint((mouse_x,mouse_y)):
                        if click:
                            click = False
                            if not green_DFS:
                                pygame.draw.rect(screenMenu, (0, 255, 0), button_dfs)
                                pygame.display.update()
                                green_DFS = True
                            else:
                                pygame.draw.rect(screenMenu, (0, 0, 0), button_dfs)
                                pygame.display.update()
                                green_DFS = False
                    if button_bfs.collidepoint((mouse_x,mouse_y)):
                        if click:
                            click = False
                            if not green_BFS:
                                pygame.draw.rect(screenMenu, (0, 255, 0), button_bfs)
                                pygame.display.update()
                                green_BFS = True
                            else:
                                pygame.draw.rect(screenMenu, (0, 0, 0), button_bfs)
                                pygame.display.update()
                                green_BFS = False
                    if green_BFS or green_DFS:
                        pygame.draw.rect(screenMenu, (0, 255, 0), button_Start)
                        pygame.display.update()
                        
                        if button_Start.collidepoint((mouse_x,mouse_y)):
                            if click:
                                screen.fill((0,0,0))
                                return green_DFS, green_BFS
                    else:
                        pygame.draw.rect(screenMenu, (255, 0, 0), button_Start)
                        pygame.display.update()
                                    
    
        
from constants import CELL_SIZE, COLOR_CHANGE, WIDTH, HEIGHT
import pygame, time, random

screen = pygame.display.set_mode((WIDTH, HEIGHT))

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

def gameCurrentNode(node, color):
    y = (node.x * 2 + 1) * CELL_SIZE
    x = (node.y * 2 + 1) * CELL_SIZE
    walls = node.walls
    def drawCell(color, rectTuple):
        pygame.draw.rect(screen, color, rectTuple, 0)

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

def initGame():
    pygame.init()
    pygame.mixer.init()
    pygame.display.set_caption("Finder")
    return pygame.time.Clock()

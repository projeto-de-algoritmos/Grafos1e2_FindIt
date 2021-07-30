import pygame, time, random

w = 10
WIDTH = 1000
HEIGHT = 1000
screen = pygame.display.set_mode((WIDTH, HEIGHT))
WHITE = (255, 255, 255)

def drawCell(rectTuple):
    pygame.draw.rect(screen, WHITE, rectTuple, 0)

def gameCurrentNode(node):
    y = (node.x * 2 + 1) * w
    x = (node.y * 2 + 1) * w
    walls = node.walls

    if not walls["down"]:
        drawCell((x, y, w, w*2))
    if not walls["up"]:
        drawCell((x, y-w, w, w*2))
    if not walls["left"]:
        drawCell((x-w, y, w*2, w))
    if not walls["right"]:
        drawCell((x, y, w*2, w))

    pygame.display.update()
    time.sleep(.005)

def initGame():
    pygame.init()
    pygame.mixer.init()
    pygame.display.set_caption("Finder")
    return pygame.time.Clock()

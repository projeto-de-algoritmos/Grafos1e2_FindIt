from pygame.constants import MOUSEBUTTONDOWN
from constants import CELL_SIZE, COLOR_CHANGE, HEIGHT
import pygame, time

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
    pygame.draw.rect(screenMenu, color, rectTuple, 0)

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
    pygame.init()
    pygame.mixer.init()
    pygame.font.init()
    pygame.display.set_caption("Finder")
    return pygame.time.Clock()

def draw_Text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def menu():
    pygame.display.set_mode((800, 600))
    click = False
    maze_DFS = maze_BFS = solver_DFS = solver_BFS = maze_prim = maze_kruskal = solver_aStar = False
    running = True
    font = pygame.font.SysFont(0, 60)
    draw_Text('Gerador de labirinto', font, (255, 255, 255), screenMenu, 185, 5)

    button_dfs = pygame.Rect(50, 70, 50, 50)
    button_bfs = pygame.Rect(50, 140, 50, 50)
    pygame.draw.rect(screenMenu, (255, 255, 255), button_dfs)
    pygame.draw.rect(screenMenu, (255, 255, 255), button_bfs)

    button_dfs = pygame.Rect(55, 75, 40, 40)
    button_bfs = pygame.Rect(55, 145, 40, 40)
    pygame.draw.rect(screenMenu, (0, 0, 0), button_dfs)
    pygame.draw.rect(screenMenu, (0, 0, 0), button_bfs)

    button_prim = pygame.Rect(400, 70, 50, 50)
    button_kruskal = pygame.Rect(400, 140, 50, 50)
    pygame.draw.rect(screenMenu, (255, 255, 255), button_prim)
    pygame.draw.rect(screenMenu, (255, 255, 255), button_kruskal)

    button_prim = pygame.Rect(405, 75, 40, 40)
    button_kruskal = pygame.Rect(405, 145, 40, 40)
    pygame.draw.rect(screenMenu, (0, 0, 0), button_prim)
    pygame.draw.rect(screenMenu, (0, 0, 0), button_kruskal)

    button_Start = pygame.Rect(400, 450, 50, 50)
    pygame.draw.rect(screenMenu, (255, 0, 0), button_Start)
    draw_Text('Começar', font, (255, 255, 255), screenMenu, 470, 450)

    draw_Text('DFS', font, (255, 255, 255), screenMenu, 105, 75)
    draw_Text('BFS', font, (255, 255, 255), screenMenu, 105, 145)
    draw_Text('Prim', font, (255, 255, 255), screenMenu, 455, 75)
    draw_Text('Kruskal', font, (255, 255, 255), screenMenu, 455, 145)
    
    draw_Text('Solucionador de labirinto', font, (255, 255, 255), screenMenu, 145, 250)

    button_dfs_solver = pygame.Rect(50, 320, 50, 50)
    button_bfs_solver = pygame.Rect(50, 390, 50, 50)
    pygame.draw.rect(screenMenu, (255, 255, 255), button_dfs_solver)
    pygame.draw.rect(screenMenu, (255, 255, 255), button_bfs_solver)

    button_dfs_solver = pygame.Rect(55, 325, 40, 40)
    button_bfs_solver = pygame.Rect(55, 395, 40, 40)
    pygame.draw.rect(screenMenu, (0, 0, 0), button_dfs_solver)
    pygame.draw.rect(screenMenu, (0, 0, 0), button_bfs_solver)

    button_aStar_solver = pygame.Rect(400, 320, 50, 50)
    pygame.draw.rect(screenMenu, (255, 255, 255), button_aStar_solver)

    button_aStar_solver = pygame.Rect(405, 325, 40, 40)
    pygame.draw.rect(screenMenu, (0, 0, 0), button_aStar_solver)

    draw_Text('DFS', font, (255, 255, 255), screenMenu, 105, 325)
    draw_Text('BFS', font, (255, 255, 255), screenMenu, 105, 395)
    draw_Text('A*', font, (255, 255, 255), screenMenu, 455, 325)

    while running:
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
                    mouse_x, mouse_y = pygame.mouse.get_pos()

                    if button_prim.collidepoint((mouse_x, mouse_y)):
                        if click:
                            click = False
                            if not maze_prim:
                                pygame.draw.rect(screenMenu, (0, 255, 0), button_prim)
                                pygame.draw.rect(screenMenu, (0, 0, 0), button_bfs)
                                pygame.draw.rect(screenMenu, (0, 0, 0), button_kruskal)
                                pygame.draw.rect(screenMenu, (0, 0, 0), button_dfs)
                                pygame.display.update()
                                maze_prim = True
                                maze_kruskal = False
                                maze_DFS = False
                                maze_BFS = False
                                maze = 0
                            else:
                                pygame.draw.rect(screenMenu, (0, 0, 0), button_prim)
                                pygame.display.update()
                                maze_prim = False
                    if button_kruskal.collidepoint((mouse_x, mouse_y)):
                        if click:
                            click = False
                            if not maze_kruskal:
                                pygame.draw.rect(screenMenu, (0, 0, 0), button_prim)
                                pygame.draw.rect(screenMenu, (0, 0, 0), button_bfs)
                                pygame.draw.rect(screenMenu, (0, 255, 0), button_kruskal)
                                pygame.draw.rect(screenMenu, (0, 0, 0), button_dfs)
                                pygame.display.update()
                                maze_prim = False
                                maze_kruskal = True
                                maze_DFS = False
                                maze_BFS = False
                                maze = 1
                            else:
                                pygame.draw.rect(screenMenu, (0, 0, 0), button_kruskal)
                                pygame.display.update()
                                maze_kruskal = False
                    if button_dfs.collidepoint((mouse_x, mouse_y)):
                        if click:
                            click = False
                            if not maze_DFS:
                                pygame.draw.rect(screenMenu, (0, 0, 0), button_prim)
                                pygame.draw.rect(screenMenu, (0, 0, 0), button_bfs)
                                pygame.draw.rect(screenMenu, (0, 0, 0), button_kruskal)
                                pygame.draw.rect(screenMenu, (0, 255, 0), button_dfs)
                                pygame.display.update()
                                maze_prim = False
                                maze_kruskal = False
                                maze_DFS = True
                                maze_BFS = False
                                maze = 2
                            else:
                                pygame.draw.rect(screenMenu, (0, 0, 0), button_dfs)
                                pygame.display.update()
                                maze_DFS = False
                    if button_bfs.collidepoint((mouse_x, mouse_y)):
                        if click:
                            click = False
                            if not maze_BFS:
                                pygame.draw.rect(screenMenu, (0, 0, 0), button_prim)
                                pygame.draw.rect(screenMenu, (0, 255, 0), button_bfs)
                                pygame.draw.rect(screenMenu, (0, 0, 0), button_kruskal)
                                pygame.draw.rect(screenMenu, (0, 0, 0), button_dfs)
                                pygame.display.update()
                                maze_prim = False
                                maze_kruskal = False
                                maze_DFS = False
                                maze_BFS = True
                                maze = 3
                            else:
                                pygame.draw.rect(screenMenu, (0, 0, 0), button_bfs)
                                pygame.display.update()
                                maze_BFS = False
                    if button_aStar_solver.collidepoint((mouse_x, mouse_y)):
                        if click:
                            click = False
                            if not solver_aStar:
                                pygame.draw.rect(screenMenu, (0, 0, 0), button_dfs_solver)
                                pygame.draw.rect(screenMenu, (0, 0, 0), button_bfs_solver)
                                pygame.draw.rect(screenMenu, (0, 255, 0), button_aStar_solver)
                                pygame.display.update()
                                solver_DFS = False
                                solver_BFS = False
                                solver_aStar = True
                                solver = 0
                            else:
                                pygame.draw.rect(screenMenu, (0, 0, 0), button_aStar_solver)
                                pygame.display.update()
                                solver_aStar = False
                    if button_dfs_solver.collidepoint((mouse_x, mouse_y)):
                        if click:
                            click = False
                            if not solver_DFS:
                                pygame.draw.rect(screenMenu, (0, 255, 0), button_dfs_solver)
                                pygame.draw.rect(screenMenu, (0, 0, 0), button_bfs_solver)
                                pygame.draw.rect(screenMenu, (0, 0, 0), button_aStar_solver)
                                pygame.display.update()
                                solver_DFS = True
                                solver_BFS = False
                                solver_aStar = False
                                solver = 1
                            else:
                                pygame.draw.rect(screenMenu, (0, 0, 0), button_dfs_solver)
                                pygame.display.update()
                                solver_DFS = False
                    if button_bfs_solver.collidepoint((mouse_x, mouse_y)):
                        if click:
                            click = False
                            if not solver_BFS:
                                pygame.draw.rect(screenMenu, (0, 255, 0), button_bfs_solver)
                                pygame.draw.rect(screenMenu, (0, 0, 0), button_dfs_solver)
                                pygame.draw.rect(screenMenu, (0, 0, 0), button_aStar_solver)
                                pygame.display.update()
                                solver_BFS = True
                                solver_DFS = False
                                solver_aStar = False
                                solver = 2
                            else:
                                pygame.draw.rect(screenMenu, (0, 0, 0), button_bfs_solver)
                                pygame.display.update()
                                solver_BFS = False
                    if (solver_BFS or solver_DFS or solver_aStar) and (maze_BFS or maze_DFS or maze_kruskal or maze_prim):
                        pygame.draw.rect(screenMenu, (0, 255, 0), button_Start)
                        pygame.display.update()
                        
                        if button_Start.collidepoint((mouse_x, mouse_y)):
                            if click:
                                screenMenu.fill((0, 0, 0))
                                
                                return maze, solver
                    else:
                        pygame.draw.rect(screenMenu, (255, 0, 0), button_Start)
                        pygame.display.update()

def restart():
    restart_button = pygame.Rect(50, HEIGHT + 20, 135, 55)
    pygame.draw.rect(screenMenu, (255, 255, 255), restart_button)
    restart_button = pygame.Rect(55, HEIGHT + 25, 125, 45)
    pygame.draw.rect(screenMenu, (0, 0, 0), restart_button)

    font = pygame.font.SysFont(0, 60)
    draw_Text('Menu', font, (255, 255, 255), screenMenu, 60, HEIGHT + 30)

    pygame.display.update()

    running = True
    while running:
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if restart_button.collidepoint((mouse_x, mouse_y)):
                        return False
    return True

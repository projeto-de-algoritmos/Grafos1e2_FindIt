class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.visited = False
        self.walls = {"up": True, "down": True, "right": True, "left": True}

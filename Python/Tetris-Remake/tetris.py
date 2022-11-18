import pygame

pygame.init()

window = pygame.display.set_mode((1000, 1000))

class L_Left(object):
    def __init__(self, x, y):
        self.width = 40
        self.x = x
        self.y = y
        self.cubes = [Cube(self.width, self.x, self.y), Cube(self.width, self.x, self.y + 40), Cube(self.width, self.x - 40, self.y - 40), Cube(self.width, self.x, self.y)]

    def draw(self):
        for c in self.cubes:
            c.draw()

    def move(self, direction):
        if direction == 1:
            for c in self.cubes:
                c.x -= 40
        if direction == 2:
            for c in self.cubes:
                c.y += 40
        if direction == 3:
            for c in self.cubes:
                c.x += 40

    def turn(self):
        pass

class T(object):
    def __init__(self, x, y):
        self.width = 40
        self.x = x
        self.y = y
        self.cubes = [Cube(self.width, self.x, self.y), Cube(self.width, self.x + 40, self.y), Cube(self.width, self.x - 40, self.y), Cube(self.width, self.x, self.y - 40)]

    def draw(self):
        for c in self.cubes:
            c.draw()

    def move(self, direction):
        if direction == 1:
            for c in self.cubes:
                c.x -= 40
        if direction == 2:
            for c in self.cubes:
                c.y += 40
        if direction == 3:
            for c in self.cubes:
                c.x += 40

    def turn(self):
        pass

class Cube(object):
    def __init__(self, width, x, y):
        self.width = width
        self.x = x
        self.y = y
        self.innerrect = pygame.Rect(self.x, self.y, self.width - 5, self.width - 5)
        self.outerrect = pygame.Rect(self.x, self.y, self.width, self.width)

    def draw(self):
        self.innerrect.center = (self.x, self.y)
        self.outerrect.center = (self.x, self.y)
        pygame.draw.rect(window, (0, 0, 0), self.outerrect)
        pygame.draw.rect(window, (255, 255, 0), self.innerrect)

class Background(object):
    def __init__(self):
        self.outercolor = (0, 0, 0)
        self.innercolor = (50, 50, 50)
        self.gamewindow = pygame.Rect(300, 100, 400, 800)

    def draw(self):
        window.fill(self.outercolor)
        pygame.draw.rect(window, self.innercolor, self.gamewindow)

lleft = L_Left(480, 840)
tpiece = T(480, 880)
background = Background()

def render_frame():

    background.draw()

    lleft.draw()

def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    tpiece.turn()
                if event.key == pygame.K_LEFT:
                    tpiece.move(1)
                if event.key == pygame.K_DOWN:
                    tpiece.move(2)
                if event.key == pygame.K_RIGHT:
                    tpiece.move(3)

        render_frame()
        pygame.display.flip()

if __name__ == "__main__":
    main()

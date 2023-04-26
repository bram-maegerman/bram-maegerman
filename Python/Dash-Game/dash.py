import pygame
from math import radians, sin, cos

pygame.init()

window = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Dash Game")
clock = pygame.time.Clock()

class Player(object):
    def __init__(self):
        self.x = 400
        self.y = 400
        self.size = 10
        self.speed = 7

    def draw(self):
        self.update_movement()
        pygame.draw.circle(window, (255, 255, 255), (self.x, self.y), self.size)
    
    def update_movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_z]:
            if self.y > 60:
                self.y -= self.speed
        if keys[pygame.K_s]:
            if self.y < 740:
                self.y += self.speed
        if keys[pygame.K_q]:
            if self.x > 60:
                self.x -= self.speed
        if keys[pygame.K_d]:
            if self.x < 740:
                self.x += self.speed

    def dash(self):
        mouse_pos = pygame.mouse.get_pos()

class Map(object):
    def __init__(self):
        self.width = 800
        self.height = 800
        self.floor = pygame.Rect(50, 50, self.width - 100, self.height - 100)

    def draw(self):
        window.fill((50, 50, 50))
        pygame.draw.polygon(window, (75, 75, 75), ((0, 0), (800, 0), (0, 800)))
        pygame.draw.rect(window, (100, 100, 100), self.floor)

player = Player()
map = Map()

def render_frame():
    map.draw()
    player.draw()

def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                player.dash()

        render_frame()
        clock.tick(60)
        pygame.display.flip()

if __name__ == "__main__":
    main()

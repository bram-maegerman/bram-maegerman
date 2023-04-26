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
        self.size = 12
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

        # ENEMY SPAWN ANIMATION
        self.spawning_enemy = False
        self.spawn_animation_length = 120 # length in frames 
        self.spawn_animation_current_frame = 0
        self.spawn_animation_current_position = (0, 0)
        self.spawn_animation_rect = pygame.Rect(0, 0, 25, 25)

    def draw(self):
        window.fill((50, 50, 50))
        pygame.draw.polygon(window, (75, 75, 75), ((0, 0), (800, 0), (0, 800)))
        pygame.draw.rect(window, (100, 100, 100), self.floor)
        if self.spawning_enemy is True:
            self.run_spawn_animation()

    def start_spawn_animation(self, spawn_position):
        self.spawn_animation_current_position = spawn_position
        self.spawning_enemy = True

    def run_spawn_animation(self):
        if self.spawn_animation_current_frame < self.spawn_animation_length:
            self.spawn_animation_rect.center = self.spawn_animation_current_position
            if self.spawn_animation_current_frame > 10 and self.spawn_animation_current_frame < 50:
                self.spawn_animation_current_position = (self.spawn_animation_current_position[0], self.spawn_animation_current_position[1] - 1)
            elif self.spawn_animation_current_frame > 70 and self.spawn_animation_current_frame < 110:
                self.spawn_animation_current_position = (self.spawn_animation_current_position[0], self.spawn_animation_current_position[1] + 1)

            pygame.draw.rect(window, (50, 50, 50), self.spawn_animation_rect)
            self.spawn_animation_current_frame += 1
        else: 
            self.spawn_animation_current_frame = 0
            self.spawning_enemy = False

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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    map.start_spawn_animation((400, 37))

        render_frame()
        clock.tick(60)
        pygame.display.flip()

if __name__ == "__main__":
    main()
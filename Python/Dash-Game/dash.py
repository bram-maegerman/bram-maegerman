import pygame, math

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

        #DASH ABILITY
        self.dashing = False
        self.dash_time = 7
        self.dash_speed = 25
        self.dash_time_current = 0

        # HITBOX
        self.hitbox = pygame.Rect(self.x, self.y, self.size + 2, self.size + 2)

    def draw(self):
        self.update_movement()
        pygame.draw.circle(window, (255, 255, 255), (self.x, self.y), self.size)
    
    def update_movement(self):
        keys = pygame.key.get_pressed()
        if self.dashing:
            self.run_dash()
        else:
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

    def start_dash(self):
        mouse_pos = pygame.mouse.get_pos()
        self.dash_direction = math.radians(math.degrees(math.atan2(mouse_pos[1] - self.y, mouse_pos[0] - self.x)))
        self.dashing = True

    def run_dash(self):
        if self.dash_time_current < self.dash_time:
            newx = self.x + math.cos(self.dash_direction) * self.dash_speed
            newy = self.y + math.sin(self.dash_direction) * self.dash_speed
            if map.check_map_bounds(newx, newy):
                self.x = newx
                self.y = newy
                self.dash_time_current += 1
                self.hitbox.center = (self.x, self.y)
                self.check_enemy_collisions()
            else:
                self.dashing = False
                self.dash_time_current = 0
        else:
            self.dashing = False
            self.dash_time_current = 0

    def check_enemy_collisions(self):
        for index, e in enumerate(enemies):
            if e.hitbox.colliderect(self.hitbox):
                enemies.pop(index)

class Enemy(object):
    def __init__(self, spawn_pos):
        self.x = 0
        self.y = 0
        self.size = 10
        self.speed = 2

        # ENEMY SPAWN ANIMATION
        self.spawning_enemy = False
        self.spawn_animation_length = 240 # length in frames 
        self.spawn_animation_current_frame = 0
        self.spawn_animation_current_position = (0, 0)
        self.spawn_animation_moving_doorparts = [pygame.Rect(0, 0, 30, 30), pygame.Rect(0, 0, 30, 30)]
        self.spawn_animation_static_doorparts = pygame.Rect(0, 0, 30, 30)
        self.start_spawn_animation(spawn_pos)

        # HITBOX
        self.hitbox = pygame.Rect(self.x, self.y, self.size + 2, self.size + 2)

    def draw(self):
        if self.spawning_enemy is True:
            self.run_spawn_animation()
        else:
            self.move()
            pygame.draw.circle(window, (255, 0, 0), (self.x, self.y), self.size)
        
    def move(self):
        if abs(player.x - self.x) > 30 or abs(player.y - self.y) > 30:
            player_pos = (player.x, player.y)
            self.dash_direction = math.radians(math.degrees(math.atan2(player_pos[1] - self.y, player_pos[0] - self.x)))
            self.x += math.cos(self.dash_direction) * self.speed
            self.y += math.sin(self.dash_direction) * self.speed
            self.hitbox.center = (self.x, self.y)

    def start_spawn_animation(self, spawn_position):
        self.spawn_animation_current_position = spawn_position
        self.spawn_animation_static_doorparts.center = spawn_position
        self.x, self.y = spawn_position[0], spawn_position[1]
        self.spawning_enemy = True

    def run_spawn_animation(self):
        if self.spawn_animation_current_frame < self.spawn_animation_length:
            for x in self.spawn_animation_moving_doorparts:
                x.center = self.spawn_animation_current_position
            if self.spawn_animation_current_frame > 20 and self.spawn_animation_current_frame < 50:
                self.spawn_animation_current_position = (self.spawn_animation_current_position[0], self.spawn_animation_current_position[1] - 1)
                self.x, self.y = self.spawn_animation_current_position[0], self.spawn_animation_current_position[1] - 1
            elif self.spawn_animation_current_frame > 90 and self.spawn_animation_current_frame < 150:
                self.x, self.y = self.x, self.y + 1
            elif self.spawn_animation_current_frame > 190 and self.spawn_animation_current_frame < 220:
                self.spawn_animation_current_position = (self.spawn_animation_current_position[0], self.spawn_animation_current_position[1] + 1)
            pygame.draw.rect(window, (50, 50, 50), self.spawn_animation_static_doorparts)
            pygame.draw.circle(window, (255, 0, 0), (self.x, self.y), self.size)
            pygame.draw.rect(window, (100, 100, 100), self.spawn_animation_moving_doorparts[0])
            pygame.draw.rect(window, (50, 50, 50), self.spawn_animation_moving_doorparts[1], 1)
            self.spawn_animation_current_frame += 1
        else: 
            self.spawn_animation_current_frame = 0
            self.spawning_enemy = False

class Map(object):
    def __init__(self):
        self.width = 800
        self.height = 800
        self.floor = pygame.Rect(50, 50, self.width - 100, self.height - 100)

    def draw(self):
        window.fill((50, 50, 50))
        pygame.draw.polygon(window, (75, 75, 75), ((0, 0), (800, 0), (0, 800)))
        pygame.draw.rect(window, (100, 100, 100), self.floor)

    def check_map_bounds(self, x, y):
        if y > 60 and y < 740 and x > 60 and x < 740:
            return True
        return False

player = Player()
map = Map()
enemies: list[Enemy] = []

def render_frame():
    map.draw()
    for x in enemies:
        x.draw()
    player.draw()

def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                player.start_dash()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    enemies.append(Enemy((400, 35)))

        render_frame()
        clock.tick(60)
        pygame.display.flip()

if __name__ == "__main__":
    main()
import pygame, math
from random import *

pygame.init()
clock = pygame.time.Clock()

#WINDOW
window = pygame.display.set_mode((1500, 1000))
width, height = window.get_width(), window.get_height()
centerx, centery = width // 2, height // 2

#ENTITIES
enemies = []

#EVENTS
SPAWN_ENEMY = pygame.USEREVENT
spawn_enemy_event = pygame.event.Event(SPAWN_ENEMY)

class Player:
    def __init__(self):
        #POSITION
        self.x = centerx
        self.y = centery

        #MOVEMENT VALUES
        self.xvel = 4
        self.yvel = 3

        #MOUSEPOS
        self.mpos = (0, 0)

        #IMAGE (set colorkey very important when rotating surfaces)
        self.color = (255, 255, 255)
        self.playersurface = pygame.Surface((30, 30))
        self.playersurface.fill(self.color)  
        self.playersurface.set_colorkey((0, 0, 0))
        self.hitbox = self.playersurface.get_rect()

        #SWORD
        self.swingtime = 0
        self.timeperswing = 30
        self.swingspeed = 6
        self.swordlength = (30, 170)

    def draw(self):
        #SETTING PLAYERPOS
        self.rotatePlayerToMousePos()
        self.adjust_hitboxes()

        #SWORD HANDLING
        if self.swingtime > 0:
            self.swingtime -= 1
            self.current_startpoint, self.current_endpoint = self.rect.center + self.startpoint.rotate(self.angle), self.rect.center + self.endpoint.rotate(self.angle)

            #ADDING POINTS TO SWORDPOINTS
            self.swordpoints = []
            for i in range(self.swordlength[1] - self.swordlength[0] - 2):
                if i % 2 == 0:
                    currentpoint = self.startpoint + pygame.Vector2(0, i + 1)
                    new_currentpoint = self.rect.center + currentpoint.rotate(self.angle)
                    self.swordpoints.append(new_currentpoint)

            #DRAWING SWORD
            pygame.draw.line(window, (255, 255, 255), self.current_startpoint, self.current_endpoint, 4)

            #ADDING ANGLE
            self.angle = (self.angle - self.swingspeed) % 360
        else:
            self.swordpoints = []

        window.blit(self.rotated_playersurface, self.hitbox)

    def swing_sword(self):
        self.swingtime = self.timeperswing
        self.startpoint, self.endpoint = pygame.math.Vector2(0, self.swordlength[0]), pygame.math.Vector2(0, self.swordlength[1])
        self.angle = math.degrees(math.atan2(-(self.mpos[0] - self.x), self.mpos[1] - self.y) % (2*math.pi))
        for i in range(self.swingtime // 2):
            self.angle = (self.angle + self.swingspeed) % 360
        self.swordpoints = []

    def adjust_hitboxes(self):
        self.rect = self.playersurface.get_rect()
        self.rect.center = (self.x, self.y)

    def rotatePlayerToMousePos(self):
        angle = math.degrees(math.atan2(self.mpos[0] - self.x, self.mpos[1] - self.y) % (2*math.pi))
        self.rotated_playersurface = pygame.transform.rotate(self.playersurface, angle)
        self.hitbox = self.rotated_playersurface.get_rect()
        self.hitbox.center = (self.x, self.y)

class Enemy:
    def __init__(self):
        #POSITION
        self.spawnpos = self.spawn()
        self.x = self.spawnpos[0]
        self.y = self.spawnpos[1]

        #IMAGE & HITBOX
        self.radius = 10
        self.color = (255, 0, 0)
        self.hitbox = pygame.Rect(0, 0, self.radius * 1.5, self.radius * 1.5)

        #VALUES
        self.speed = 1

    def draw(self):
        #UPDATE HITBOX
        self.hitbox = pygame.Rect(0, 0, self.radius * 1.5, self.radius * 1.5)
        self.hitbox.center = (self.x, self.y)

        #DRAWING
        pygame.draw.circle(window, self.color, (self.x, self.y), self.radius)

    def spawn(self):
        spawnpos = (randint(100, width - 100), randint(100, height - 100))
        playerrect = pygame.Rect(0, 0, 100, 100)
        playerrect.center = (player.x, player.y)
        if playerrect.collidepoint(spawnpos):
            return self.spawn()
        else:
            return spawnpos
        
    def move(self):
        dx, dy = player.rect.x - self.x, player.rect.y - self.y
        dist = math.hypot(dx, dy)
        dx, dy = dx / dist, dy / dist
        self.x += dx * self.speed
        self.y += dy * self.speed

player = Player()

def input(events):
    mpos = pygame.mouse.get_pos()
    for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if player.swingtime == 0:
                    player.swing_sword()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                exit()

    #MOVEMENT
    keys = pygame.key.get_pressed()
    player.x += (keys[pygame.K_d] - keys[pygame.K_q]) * player.xvel
    player.y += (keys[pygame.K_s] - keys[pygame.K_z]) * player.yvel

def update_game():
    player.mpos = pygame.mouse.get_pos()

    for e in enemies:
        if type(e) is Enemy:
            e.move()
            if player.swingtime > 0:
                for point in player.swordpoints:
                    if e.hitbox.collidepoint(point):
                        enemies.pop(enemies.index(e))
                        break

def render_frame():
    window.fill((0, 0, 0))
    
    for e in enemies:
        e.draw()

    player.draw()

def game():
    #TIMERS
    pygame.time.set_timer(SPAWN_ENEMY, 1000)
    
    running = True          
    while running:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == SPAWN_ENEMY:
                enemies.append(Enemy())

        input(events)
        update_game()
        render_frame()

        pygame.display.flip()
        clock.tick(120)
    
    exit()

if __name__ == "__main__":
    game()
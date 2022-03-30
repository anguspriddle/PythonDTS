import pygame
from random import randint
from pygame import time
from time import sleep
pygame.init()
window = pygame.display.set_mode((1100, 650))
x = 500
y = 100
width = 64
height = 64
enemyY = 600
enemyx = 500
rise_velocity = 5
#-- Variables and lists --
bg = pygame.image.load('bg.png')
char = pygame.image.load('racer.png')
bad = pygame.image.load('rock.png')
clock = pygame.time.Clock()
badhitbox = bad.get_rect(topleft = (enemyx, enemyY))


class AbstractGroup:
    pass


class player(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, *groups: AbstractGroup):
        super().__init__(*groups)
        pygame.sprite.Sprite.__init__(self)
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.velocity = 6
        self.run = True
        self.left = False
        self.right = False
        self.walkCount = 0
        self.hitbox = (self.x + 27, self.y + 40, 39, 50)
        self.rect = pygame.draw.rect(window, (255, 0, 0), self.hitbox, 2)
    def draw(self, window):
        window.blit(char, (self.x, self.y))
        pygame.sprite.Sprite.__init__(self)
        self.hitbox = (self.x + 27, self.y + 40, 39, 50)
        self.rect = pygame.draw.rect(window, (255, 0, 0), self.hitbox, 2)
    def collision(self):
        print("Collision")


class enemy(object):
    def __init__(self, enemyx, enemyY, width, height):
        self.x=enemyx
        self.y=enemyY
        self.width=width
        self.height=height
        self.rise=rise_velocity
        self.hitbox = (self.x + 30, self.y + 50, 48, 35)
        self.rect = pygame.draw.rect(window, (255, 0, 0), self.hitbox, 2)
    def draw(self, window):
        window.blit(bad, (self.x, self.y))
        self.hitbox = (self.x + 28, self.y + 50, 48, 35)
        self.rect = pygame.draw.rect(window, (255, 0, 0), self.hitbox, 2)
def redraw_GameWindow():
    window.blit(bg, (0, 0))
    player_character.draw(window)
    enemy_object.draw(window)
    pygame.display.update()


score = 0
run = True
alive = True
player_character=player(500, 100, 64, 64)
enemy_object=enemy(500, 600, 64, 64)
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_character.x > 230 - player_character.velocity - player_character.width:
       player_character.x -= player_character.velocity
    elif keys[pygame.K_RIGHT] and player_character.x < 930 - player_character.velocity - player_character.width:
        player_character.x += player_character.velocity
    enemy_object.y -= enemy_object.rise
    if player_character.rect.colliderect(enemy_object.rect):
        print("Collision")
        player_character.kill()
    if enemy_object.y == 0:
        print("Game over")
        enemy_object.y = 600
        enemy_object.x = randint(330, 930)
        run = False
    redraw_GameWindow()

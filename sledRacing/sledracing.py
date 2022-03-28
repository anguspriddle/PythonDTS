import pygame
from random import randint

import pygame as pygame
from pygame import time
from time import sleep
pygame.init()
window = pygame.display.set_mode((1100, 650))
x = 500
y = 100
width = 64
height = 64
enemyY = 600
enemyx = randint(330, 930)
rise_velocity = 5
#-- Variables and lists --
bg = pygame.image.load('bg.png')
char = pygame.image.load('racer.png')
bad = pygame.image.load('rock.png')
clock = pygame.time.Clock()
badhitbox = bad.get_rect(topleft = (enemyx, enemyY))
class player(object):
    def __init__(self, x, y, width, height):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.velocity = 6
        self.run = True
        self.left = False
        self.right = False
        self.walkCount = 0
        self.charhitbox = char.get_rect(topleft = (x, y))
    def draw(self, window):
            window.blit(char, (self.x, self.y))


def redraw_GameWindow():
    window.blit(bg, (0, 0))
    player_character.draw(window)
    badhitbox = bad.get_rect(topleft=(10, 10))
    window.blit(bad, (enemyx, enemyY))
    pygame.display.update()


score = 0
run = True

player_character=player(500, 100, 64, 64)
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
    enemyY -= rise_velocity
    if enemyY == 0:
        print("Game over")
        enemyY = 600
        enemyx = randint(330, 930)
    if player_character.charhitbox.colliderect(badhitbox):
        print("Grah")
    redraw_GameWindow()

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

#-- Variables and lists --
bg = pygame.image.load('bg.png')
char = pygame.image.load('racer.png')
bad = pygame.image.load('rock.png')
clock = pygame.time.Clock()

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

    def draw(self, window):
            window.blit(char, (self.x, self.y))

class enemy(object):
    def __init__(self):
        self.enemyx= 1000
        self.enemyy= 10

    def enemydraw(self, window):
        window.blit(bad, (self.x, self.y))

def redraw_GameWindow():
    window.blit(bg, (0, 0))
    player_character.draw(window)
    pygame.display.update()

score = 0
run = True

player_character=player(500, 100, 64, 64)
enemy_object=enemy
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

    redraw_GameWindow()

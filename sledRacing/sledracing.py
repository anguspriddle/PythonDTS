import pygame
from pygame import time
pygame.init()
window = pygame.display.set_mode((1100, 650))
x = 1100
y = 650
width = 64
height = 64

#-- Variables and lists --
bg = pygame.image.load('bg.png')
char = pygame.image.load('racer.png')
clock = pygame.time.Clock()

class player(object):
    def __init__(self, x, y, width, height):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.velocity = 5
        self.run = True
        self.left = False
        self.right = False
        self.walkCount = 0

    def draw(self, window):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if self.left:
            self.walkCount += 1
        elif self.right:
            self.walkCount += 1
        else:
            window.blit(char, (self.x, self.y))

def redraw_GameWindow():
    window.blit(bg, (0, 0))
    player_character.draw(window)
    pygame.display.update()

run = True

player_character=player(300, 410, 64, 64)
while run:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and player_character.x > player_character.velocity:
       player_character.x -= player_character.velocity
       player_character.left = True
       player_character.right = False
    elif keys[pygame.K_RIGHT] and player_character.x < 500 - player_character.velocity - player_character.width:
        player_character.x += player_character.velocity
        player_character.left = False
        player_character.right = True

    redraw_GameWindow()

import pygame
import random
from random import randint
import time

pygame.init()

window = pygame.display.set_mode((1900,1000))
pygame.display.set_caption("Angus's Balloon Pop Game")
x = 1900
y = 1040
width = 64
height = 64
clock = pygame.time.Clock()
# Game Scenario: Balloon Pop Game

balloon = pygame.image.load('balloon.png')

class balloon(object):
    def __init__(self, x, y, width, height):
        self.x=x
        self.y=y
        window.blit(balloon,(self.x,self.y))


run = True
player_character=balloon(64,64)
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
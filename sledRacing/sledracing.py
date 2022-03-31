# Imports and setups
import pygame
from random import randint
from pygame import time
from time import sleep
pygame.init()
window = pygame.display.set_mode((1100, 650)) # Sets window size to 1100 x 650
pygame.display.set_caption("Danger Sledding") # Sets window name
# Variables And Lists
Points = 0
x = 500
y = 100
width = 64
height = 64
enemyY = 600
enemyx = 500
rise_velocity = 5
bg = pygame.image.load('bg.png')
char = pygame.image.load('racer.png')
bad = pygame.image.load('rock.png')
title = pygame.image.load('title.png')
clock = pygame.time.Clock()

#Classes
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
        self.hitbox = (self.x + 27, self.y + 40, 39, 50)
        self.rect = pygame.draw.rect(window, (255, 255, 255), self.hitbox, 2)
    def draw(self, window):
        window.blit(char, (self.x, self.y))
        self.hitbox = (self.x + 27, self.y + 40, 39, 50)
        self.rect = pygame.draw.rect(window, (255, 255, 255), self.hitbox, 2)


class enemy(object):
    def __init__(self, enemyx, enemyY, width, height):
        self.x=enemyx
        self.y=enemyY
        self.width=width
        self.height=height
        self.rise=rise_velocity
        self.hitbox = (self.x + 30, self.y + 50, 48, 35)
        self.rect = pygame.draw.rect(window, (255, 255, 255), self.hitbox, 2)
    def draw(self, window):
        window.blit(bad, (self.x, self.y))
        self.hitbox = (self.x + 28, self.y + 50, 48, 35)
        self.rect = pygame.draw.rect(window, (255, 255, 255), self.hitbox, 2)
def redraw_GameWindow():
    window.blit(bg, (0, 0))
    player_character.draw(window)
    enemy_object.draw(window)
    text=font.render("Score: " +str(Points), 1,(0, 0, 0))
    window.blit(text, (50, 10))
    pygame.display.update()

def redrawEndgame_window():
    window.blit(title, (0, 0))
    text = font.render("You scored " + str(Points) + " Points!", 1, (0, 0, 0))
    text2 = font2.render("You Died!", 1, (0, 0, 0))
    window.blit(text, (400, 350))
    window.blit(text2, (400, 200))
    pygame.display.update()

# Main game
score = 0
run = True
alive = True
font=pygame.font.SysFont("comicsansms", 30, True, True) # Setsup fonts for the score and end game screen.
font2=pygame.font.SysFont("comicsansms", 60, True, True)
player_character=player(500, 100, 64, 64) # Setting passthrough variables for the player and the enemies
enemy_object=enemy(500, 600, 64, 64)
while run: # This is the game loop
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            run = False
    while alive:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                alive = False
                run = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_character.x > 230 - player_character.velocity - player_character.width:
           player_character.x -= player_character.velocity
        elif keys[pygame.K_RIGHT] and player_character.x < 930 - player_character.velocity - player_character.width:
            player_character.x += player_character.velocity
        enemy_object.y -= enemy_object.rise
        if keys[pygame.K_ESCAPE]: # Closes the game on Escape Button Press
            run = False
            alive = False
        if player_character.rect.colliderect(enemy_object.rect): # Upon collision, goes to end game screen and stops
                                                                 # The main game loop of 'alive'
            alive = False
        if enemy_object.y == 0: # Resets the Y value of the enemy and places it at a random x value
                                # To have a constant flow of enemies one after the other
            Points += 1   # This adds a point every time the enemy is successfully avoided by the player
            enemy_object.y = 600
            enemy_object.x = randint(330, 930)
        redraw_GameWindow()
    redrawEndgame_window()
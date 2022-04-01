# Imports and setups
import pygame
from random import randint
from pygame import time
from time import sleep
pygame.init()
window = pygame.display.set_mode((1100, 645)) # Sets window size to 1100 x 645
pygame.display.set_caption("Danger Sledding") # Sets window name
# Variables And Lists
Points = 0
x = 500
y = 100
width = 64
height = 64
enemyY = 600
enemyx = 500
enemy2x = 400
enemy3x = 400
rise_velocity = 5
riseVelocity2 = 5
score = 0
run = True
endgame = False
alive = False
mainMenu = True
font=pygame.font.SysFont("cambri", 30, True, True) # Setsup fonts for the score and end game screen.
font2=pygame.font.SysFont("cambri", 60, True, True)
bg = pygame.image.load('bg.png')
char = pygame.image.load('racer.png')
bad = pygame.image.load('rock.png')
title = pygame.image.load('title.png')
bad2 = pygame.image.load('rock2.png')
bad3 = pygame.image.load('rock3.png')
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
        self.hitbox = (self.x + 27, self.y + 40, 42, 50)
        self.rect = pygame.draw.rect(window, (0, 255, 255), self.hitbox, 2)
    def draw(self, window):
        window.blit(char, (self.x, self.y))
        self.hitbox = (self.x + 27, self.y + 40, 42, 50)
        self.rect = pygame.draw.rect(window, (0, 255, 255), self.hitbox, 2)


class enemy(object):
    def __init__(self, enemyx, enemyY, width, height):
        self.x=enemyx
        self.y=enemyY
        self.width=width
        self.height=height
        self.rise=rise_velocity
        self.hitbox = (self.x + 30, self.y + 50, 48, 35)
        self.rect = pygame.draw.rect(window, (255, 0, 255), self.hitbox, 2)
    def draw(self, window):
        window.blit(bad, (self.x, self.y))
        self.hitbox = (self.x + 28, self.y + 50, 48, 35)
        self.rect = pygame.draw.rect(window, (255, 0, 255), self.hitbox, 2)

class enemy2(object):
    def __init__(self, enemy2x, enemyY, width, height):
        self.x=enemy2x
        self.y=enemyY
        self.width=width
        self.height=height
        self.rise=rise_velocity
        self.hitbox = (self.x+30, self.y+50, 48, 35)
        self.rect = pygame.draw.rect(window, (255, 0, 255), self.hitbox, 2)
    def draw(self, window):
        window.blit(bad2, (self.x, self.y)) # add image for second obstacle here
        self.hitbox = (self.x + 30, self.y + 50, 48, 35)
        self.rect = pygame.draw.rect(window, (255, 0, 255), self.hitbox, 2)

class enemy3(object):
    def __init__(self, enemy3x, enemyY, width, height):
        self.x=enemy3x
        self.y=enemyY
        self.width=width
        self.height=height
        self.rise=rise_velocity
        self.hitbox = (self.x+30, self.y+50, 48, 35)
        self.rect = pygame.draw.rect(window, (255, 0, 255), self.hitbox, 2)
    def draw(self, window):
        window.blit(bad3, (self.x, self.y)) # add image for second obstacle here
        self.hitbox = (self.x + 30, self.y + 50, 48, 35)
        self.rect = pygame.draw.rect(window, (255, 0, 255), self.hitbox, 2)



def redraw_GameWindow():
    window.blit(bg, (0, 0))
    player_character.draw(window)
    enemy_object.draw(window)
    enemyObject2.draw(window)
    text=font.render("Score: " +str(Points), 1,(0, 0, 0))
    window.blit(text, (50, 10))
    pygame.display.update()

def endGame_window():
    window.blit(title, (0, 0))
    text = font.render("You scored " + str(Points) + " Points!", 1, (0, 0, 0))
    text2 = font2.render("You Died!", 1, (0, 0, 0))
    window.blit(text, (400, 350))
    window.blit(text2, (400, 200))
    pygame.display.update()

def mainMenu_window():
    window.blit(title, (0, 0))
    titleText = font.render("Danger Sledding", 1, (0, 0, 0))
    pressPlay_Text = font2.render("Press Space To Start", 1, (0, 0, 0))
    window.blit(titleText, (500, 100))
    window.blit(pressPlay_Text, (325, 550))
    pygame.display.update()

# Main game
player_character=player(500, 100, 64, 64) # Setting passthrough variables for the player and the enemies
enemy_object=enemy(500, 600, 64, 64)
enemyObject2 = enemy2(500, 650, 64, 64)
enemyObject3 = enemy3(500, 600, 64, 64)
while run: # This is the game loop
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    while mainMenu: # Runs Main Menu On Start of game.
        clock.tick(60)
        keys = pygame.key.get_pressed()
        mainMenu_window()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                mainMenu = False
        if keys[pygame.K_ESCAPE]:
            run = False
            mainMenu = False
        if keys[pygame.K_SPACE]: # Switches to main game on press of spacebar
            enemy_object.y = 500
            alive = True
            mainMenu = False
            endgame = False

    while alive:
        clock.tick(60)
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                alive = False
                run = False
        # for obstacle in obstacles:
             # if enemy_object.x < 855 and enemy_object.x > 150:
                # enemy_object.y -= enemy_object.rise
        if keys[pygame.K_LEFT] and player_character.x > 250 - player_character.velocity - player_character.width:
           player_character.x -= player_character.velocity
        elif keys[pygame.K_RIGHT] and player_character.x < 930 - player_character.velocity - player_character.width:
            player_character.x += player_character.velocity
        enemy_object.y -= enemy_object.rise
        if Points >= 5:
            enemyObject2.y -= enemyObject2.rise
        if Points >= 10:
            enemyObject3.y -= enemyObject3.rise
        if keys[pygame.K_ESCAPE]: # Closes the game on Escape Button Press
            run = False
            alive = False
        if player_character.rect.colliderect(enemy_object.rect): # Upon collision, goes to end game screen and stops
                                                                 # The main game loop of 'alive'
            alive = False
            endgame = True
        if enemy_object.y == -100: # Resets the Y value of the enemy and places it at a random x value
                                # To have a constant flow of enemies one after the other
            Points += 1   # This adds a point every time the enemy is successfully avoided by the player
            enemy_object.y = 600
            enemy_object.x = randint(150, 855)
            if enemy_object.x == enemyObject2.x:
                enemy_object.x = randint(150, 855)
        if enemyObject2.y <= -100:
            enemyObject2.y = 600
            enemyObject2.x = randint(180, 840)
            if enemyObject2.x == enemy_object.x:
                enemyObject2.x = randint(180, 840)
        redraw_GameWindow()
    while endgame:
        clock.tick(60)
        endGame_window()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                endgame = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            run = False
            endgame = False
        if keys[pygame.K_b]:
            endgame = False
            mainMenu = True
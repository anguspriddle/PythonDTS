# Imports and setups
import pygame
from random import randint
from pygame import mixer
pygame.mixer.pre_init(44100, -16, 2, 6000)
pygame.init()
window = pygame.display.set_mode((1100, 645)) # Sets window size to 1100 x 645
pygame.display.set_caption("Danger Sledding") # Sets window name
icon = pygame.image.load('icon.png') # This line of code loads in an image to a variable name, for this it loads the
                                      # Image used for the window icon
pygame.display.set_icon(icon) # Sets window icon
# Variables And Lists.
Points = 0
width = 64
height = 64
lives = 3
rise_velocity = [5, 7, 3, 8]
ranVel = randint(0, 3)
riseVelocity = rise_velocity[ranVel]
bg = pygame.image.load('bg.png')
char = pygame.image.load('racer.png')
bad = pygame.image.load('rock.png')
title = pygame.image.load('title.png')
bad2 = pygame.image.load('rock2.png')
log = pygame.image.load('log.png')
boulder = pygame.image.load('rock3.png')

clock = pygame.time.Clock() # Makes the pygame clock function simply run under 'clock'
font=pygame.freetype.Font("Penguin.ttf", 50) # This loads a font to a variable, name for this it uses the Penguin.ttf font, and loads
                                             # it to the size 50 pixels under the variable name 'font'
font2=pygame.freetype.Font("Penguin.ttf", 40)
font3=pygame.freetype.Font("Icecold.ttf", 20)
Gameover = mixer.Sound('GameOver.wav') # This loads audio to a variable name , for this one it loads the game over noise to
                                       # The variable name Gameover
music = mixer.music.load('SledRacing.mp3') # This loads music to the game, and allows it to play continuously no matter what loop, unless
                                           # Changed by command, for this it loads SledRacing.mp3 to the variable 'music'
pygame.mixer.music.play(-1) # This makes the music variable play on an infinite loop unless stopped by a later command
#Classes
class player(object): # This is a class, a class holds information under one name or  'class', in order to store and call individual variables.
# This class will be the class that will store all the information for the player character itself.
    def __init__(self, width, height):
        self.x=500
        self.y=100
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
    def __init__(self, width, height):
        self.x=400
        self.y=600
        self.width=width
        self.height=height
        self.rise=rise_velocity
        self.hitbox = (self.x + 30, self.y + 50, 48, 35)
        self.rect = pygame.draw.rect(window, (255, 255, 255), self.hitbox, 2)
    def draw(self, window):
        window.blit(bad, (self.x, self.y))
        self.hitbox = (self.x + 28, self.y + 50, 48, 35)
        self.rect = pygame.draw.rect(window, (255, 255, 255), self.hitbox, 2)

class enemy2(object):
    def __init__(self, width, height):
        self.x=400
        self.y=600
        self.width=width
        self.height=height
        self.rise=riseVelocity
        self.hitbox = (self.x+30, self.y+50, 48, 35)
        self.rect = pygame.draw.rect(window, (255, 255, 255), self.hitbox, 2)
    def draw(self, window):
        window.blit(bad2, (self.x, self.y)) # add image for second obstacle here
        self.hitbox = (self.x + 30, self.y + 50, 48, 35)
        self.rect = pygame.draw.rect(window, (255, 255, 255), self.hitbox, 2)

class logEnemy(object):
    def __init__(self, width, height):
        self.x=660
        self.y=700
        self.width=width
        self.height=height
        self.hitbox = (self.x + 40, self.y+50, 100, 29)
        self.rect = pygame.draw.rect(window, (225, 255, 255), self.hitbox, 2)
    def draw(self, window):
        window.blit(log, (self.x, self.y))
        self.hitbox = (self.x + 40, self.y + 50, 100, 29)
        self.rect = pygame.draw.rect(window, (225, 255, 255), self.hitbox, 2)

class boulderEnemy(object):
     def __init__(self, width, height):
         self.x=800
         self.y=700
         self.width=width
         self.height=height
         self.hitbox= (self.x + 8, self.y+39, 70, 30)
         self.rect = pygame.draw.rect(window, (255, 255, 255), self.hitbox, 2)
     def draw(self, window):
            window.blit(boulder, (self.x, self.y))
            self.hitbox = (self.x + 8, self.y + 39, 70, 30)
            self.rect = pygame.draw.rect(window, (225, 255, 255), self.hitbox, 2)


def redraw_GameWindow(): # These are functions, they are defined functions that do certain things and can be called later on
                         # This function draws the main game window
    window.blit(bg, (0, 0))
    clock.tick(60)
    player_character.draw(window)  # Calls the draw functions of all players and enemies
    enemy_object.draw(window)
    enemyObject2.draw(window)
    logEnemy.draw(window)
    boulderEnemy.draw(window)
    font3.render_to(window, (30, 10), "Score:{}" .format(Points)) # Displays score in the top right
    pygame.display.update() # This updates the display in a loop, otherwise it would flash for 1 frame and stop.

def endGame_window(): # This is a function that will draw the end game window
    window.blit(title, (0, 0))
    clock.tick(60)
    font.render_to(window, (300, 350), "You scored {} Points!" .format(Points))
    font2.render_to(window, (400, 150), "You Died!")
    pygame.display.update()

def mainMenu_window(): # This is the function that will display the main menu
    window.blit(title, (0, 0))
    clock.tick(60)
    font.render_to(window, (300, 170), "Danger Sledding +")
    font2.render_to(window, (300, 500), "Press Space To Play")
    pygame.display.update()

# Main game
run = True # Turns on run loop on open
endgame = False
alive = False
mainMenu = True
font=pygame.freetype.Font("Penguin.ttf", 50) # Sets up fonts for the score and end game screen.
font2=pygame.freetype.Font("Penguin.ttf", 40)
font3=pygame.freetype.Font("Icecold.ttf", 20)
player_character=player(64, 64) # Setting passthrough variables for the player and the enemies
enemy_object=enemy(64, 64)
enemyObject2 = enemy2(64, 64)
logEnemy = logEnemy(64 ,64)
boulderEnemy = boulderEnemy(64, 64)
while run: # This is the game loop, the while statement means that while a variable is set to True, the code will loop
           # Until the variable is set to False.
    while mainMenu: # Runs Main Menu On Start of game.
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
            logEnemy.y = 660
            alive = True
            mainMenu = False
            endgame = False

    while alive: # This is the loop for the main gameplay segment
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                alive = False
                run = False
        if lives == 0:
            alive = False
            playGameOver = True
            endgame = True
        if keys[pygame.K_LEFT] and player_character.x > 195 - player_character.velocity - player_character.width:
            # This is an if statement that runs when the user presses the left arrow key, moving the character to the left
           player_character.x -= player_character.velocity
        elif keys[pygame.K_RIGHT] and player_character.x < 920 - player_character.velocity - player_character.width:
            # This is an elif statement, meaning that if the first thing doesnt happen, this would happen instead but only if it's own requirements are met.
            # For example, if the other if statement for the left arrow key isn't happening, but the right arrow is being pressed, this loop will run.
            player_character.x += player_character.velocity
        enemy_object.y -= riseVelocity
        if Points >= 5:
            enemyObject2.y -= riseVelocity
            logEnemy.y -= riseVelocity
        if Points >= 10:
            boulderEnemy.y -= riseVelocity
        if keys[pygame.K_ESCAPE]: # Closes the game on Escape Button Press
            run = False
            alive = False
        if player_character.rect.colliderect(enemy_object.rect) or player_character.rect.colliderect(enemyObject2.rect)\
            or player_character.rect.colliderect(logEnemy.rect) or player_character.rect.colliderect(boulderEnemy.rect)\
                                                                : # Upon collision, goes to end game screen and stops
            lives -= 1
            print(lives)
        if enemy_object.y < 0: # Resets the Y value of the enemy and places it at a random x value
                                        # To have a constant flow of enemies one after the other
            Points += 1         # This adds a point every time the enemy is successfully avoided by the player
            enemy_object.y = 600
            enemy_object.x = randint(170, 800)
            if enemy_object.rect.colliderect(enemyObject2.rect):
                 enemy_object.x = randint(170, 300)
            ranVel = randint(0, 3)
            riseVelocity = rise_velocity[ranVel]
        if enemyObject2.y < 0:
            enemyObject2.y = 600
            enemyObject2.x = randint(200, 855)
        if logEnemy.y < 0:
            logEnemy.y = 600
            logEnemy.x = randint(200, 750)
            if logEnemy.x == enemyObject2.x:
                logEnemy.x = randint(200, 750)
            elif logEnemy.x == enemy_object.x:
                logEnemy.x = randint(200, 750)
        if boulderEnemy.y < 0:
            boulderEnemy.y = 600
            boulderEnemy.x = randint(200, 780)
            if boulderEnemy.x == logEnemy.x:
                boulderEnemy.x = randint(200, 780)
            elif boulderEnemy.x == enemyObject2.x:
                boulderEnemy.x = randint(200, 780)
            elif boulderEnemy.x == enemy_object.x:
                boulderEnemy.x = randint(200, 780)
        redraw_GameWindow()
    while endgame: # This is the loop for the endgame screen
        pygame.mixer.music.stop()
        if playGameOver:
            Gameover.play()
            playGameOver = False
        endGame_window()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            run = False
            endgame = False
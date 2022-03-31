import pygame
from pygame import time
pygame.init()
window = pygame.display.set_mode((500, 500))
pygame.display.set_caption("UARGHHHHH")
x = 500
y = 400
width = 64
height = 64

#---------------------------- Variables and lists ----------------------------
walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'),
             pygame.image.load('R3.png'), pygame.image.load('R4.png'),
             pygame.image.load('R5.png'), pygame.image.load('R6.png'),
             pygame.image.load('R7.png'), pygame.image.load('R8.png'),
             pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'),
            pygame.image.load('L3.png'), pygame.image.load('L4.png'),
            pygame.image.load('L5.png'), pygame.image.load('L6.png'),
            pygame.image.load('L7.png'), pygame.image.load('L8.png'),
            pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')
clock = pygame.time.Clock()

class player(object):
    def __init__(self, x, y, width, height): # Pass through Variables
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.velocity = 5    # These are no longer global variable, they are now class variables.
        self.run = True      # This is better because they can only be accessed by the player class
        self.is_jump = False # and not other parts of the program.
        self.jump_count = 10
        self.left = False
        self.right = False
        self.walkCount = 0
    def draw(self, window):
        # We have 9 images for our walking animation, I want to show the same image for 3 frames
        # so i use the number 27 as an upper bound for walkCount because 27 / 3 = 9. So 9 images shown
        # 3 times each animation
        if self.walkCount + 1 >= 27: # Because each direction is made up of 9 images shown 3 times this will
                                    # stop a index out of range error with our list as it only has 9 values.
            self.walkCount = 0
        if self.left:
            window.blit(walkLeft[self.walkCount//3], (self.x,self.y)) # We integer divide (Rounding down to a even
                                                                      # number) WalkCount by 3 to ensure each image
                                                                      # is shown 3 times every animation. (x,y)will
                                                                      # keep track of the curent position of the
                                                                      # character based on the user input .
            self.walkCount += 1
        elif self.right:
            window.blit(walkRight[self.walkCount//3], (self.x,self.y))
            self.walkCount += 1
        else:
            window.blit(char, (self.x, self.y)) # If the character is standing still.

#---------------------------- Methods ----------------------------
def redraw_GameWindow():
    window.blit(bg, (0,0)) # This will draw our background image at (0,0) .blit is short for block
    # transfer and allows us to add images to a surface, in this case the main window.
    player_character.draw(window)
    pygame.display.update()

#---------------------------- Main Routine ----------------------------
run=True

player_character=player(300,410,64,64) # Object created from the class which sends information to the pass through variables
while run:
    clock.tick(27)
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
    else:
        player_character.left = False
        player_character.right = False
    if not (player_character.is_jump):
        if keys[pygame.K_SPACE]: # Jumping
            player_character.is_jump = True
            player_character.right = False # Stops animation while jumping
            player_character.left = False # Stops animation while jumping
            player_character.walkCount = 0 # Stops animation while jumping
    else:
        if player_character.jump_count >= -10:
            negitive = 1 # New Code
            if player_character.jump_count < 0: # New Code
                negitive = -1 # code
            player_character.y -= (player_character.jump_count ** 2) * 0.5 * negitive # New Code
            player_character.jump_count -= 1
        else:
            player_character.is_jump = False
            player_character.jump_count = 10

    redraw_GameWindow()
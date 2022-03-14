import pygame
from pygame import time
pygame.init()
window = pygame.display.set_mode((500, 500))
pygame.display.set_caption("UARGHHHHH")
x = 500
y = 400
width = 64
height = 64


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
    def __init__(self, x, y, width, height):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.velocity = 5
        self.run = True
        self.is_jump = False
        self.jump_count = 10
        self.left = False
        self.right = False
        self.walkCount = 0
    def draw(self, window):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        if self.left:
            window.blit(walkLeft[self.walkCount//3], (self.x,self.y))



            self.walkCount += 1
        elif self.right:
            window.blit(walkRight[self.walkCount//3], (self.x,self.y))
            self.walkCount += 1
        else:
            window.blit(char, (self.x, self.y))
def redraw_GameWindow():
    window.blit(bg, (0,0))
    player_character.draw(window)
    pygame.display.update()

run=True
player_character=player(300,410,64,64)
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
        if keys[pygame.K_SPACE]:
            player_character.is_jump = True
            player_character.right = False
            player_character.left = False
            player_character.walkCount = 0
    else:
        if player_character.jump_count >= -10:
            negitive = 1
            if player_character.jump_count < 0:
                negitive = -1
            player_character.y -= (player_character.jump_count ** 2) * 0.5 * negitive
            player_character.jump_count -= 1
        else:
            player_character.is_jump = False
            player_character.jump_count = 10

    redraw_GameWindow()
import pygame
from pygame import time
pygame.init()
window = pygame.display.set_mode((500, 500))
pygame.display.set_caption("UARGHHHHH")
x = 500
y = 400
width = 64
height = 64
velocity = 5
run = True
is_jump = False
jump_count = 10
left = False
right = False
walkCount = 0


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

def redraw_GameWindow():
    global walkCount
    global left
    global right
    window.blit(bg, (0,0))

    if walkCount + 1 >- 27:
        walkCount = 0

    if left:
        window.blit(walkLeft[walkCount//3], (x,y))

        walkCount += 1
    elif right:
        window.blit(walkRight[walkCount//3], (x,y))
        walkCount += 1
    else:
        window.blit(char, (x,y))
        walkCount = 0
    pygame.display.update()

while run:
    clock = pygame.time.Clock()
    clock.tick(27)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > velocity:
        x -= velocity
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x < 500 - velocity - width:
        x += velocity
        left = False
        right = True
    else:
        left = False
        right = False
    if not (is_jump):
        if keys[pygame.K_UP] and y > velocity:
            y -= velocity
        if keys[pygame.K_DOWN] and y < 500 - velocity - height:
            y += velocity
        if keys[pygame.K_SPACE]:
            is_jump = True
    else:
        jump_count = 10
        is_jump = False

redraw_GameWindow()
import pygame

pygame.init()

window = pygame.display.set_mode((1100,650))
pygame.display.set_caption("Angus's Balloon Pop Game")
x = 1900
y = 1040
width = 40
height = 60
balloonvelocity = 6
clock = pygame.time.Clock()
# Game Scenario: Balloon Pop Game

bg = pygame.image.load('bg.png')
score = 0

def redraw_GameWindow():
    window.blit(bg, (0,0))
    window.fill(0 , 0)
    pygame.display.update()


run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.draw.rect(window, (225, 0, 0), (x, y, width, height))
    redraw_GameWindow()
import pygame
import math
#import numpy 


color1 = (22,22,22)
color2 = (222,222,222)
resolution_x = 1280
resolution_y = 720
black = (0,0,0)
#nb_cases_sqrt
#linecoord_x = [resolution(0)/10]
#linecoord_y = [resolution(0)/10]


pygame.init()
screen = pygame.display.set_mode((resolution_x, resolution_y))
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(color2)
    pygame.display.flip()

    for x in range (math.trunc(resolution_x/10), resolution_x, math.trunc(resolution_x/10)) :
        pygame.draw.line(screen, (black), [x, 0], [x, 720], 1)
        
    for y in range (math.trunc(resolution_y/10), resolution_y, math.trunc(resolution_y/10)) :
        pygame.draw.line(screen, (black), [0, y], [1280, y], 1)
    
    pygame.display.flip()

    clock.tick(60)

pygame.quit()

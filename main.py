import pygame
from screen import Screen
from vampire import Vampire

pygame.init()

run = True

while run:
    Screen.load()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                Vampire.change_pos('right')
            elif event.key == pygame.K_LEFT:
                Vampire.change_pos('left')
        elif event.type == pygame.KEYUP:
            if (event.key == pygame.K_RIGHT or
            event.key == pygame.K_LEFT):
                Vampire.change_pos('stop')
    
    Vampire.display()
    pygame.display.update()

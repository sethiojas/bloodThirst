import pygame
from screen import Screen
from vampire import Vampire
from pedestrian import Pedestrian

pygame.init()

run = True

ai = [Pedestrian()]

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
            elif event.key == pygame.K_SPACE:
                for i in range(len(ai)):
                    if ai[i].is_close_to_vampire():
                        ai.pop(i)

        elif event.type == pygame.KEYUP:
            if (event.key == pygame.K_RIGHT or
            event.key == pygame.K_LEFT):
                Vampire.change_pos('stop')

    for bot in ai:
        bot.move()
    
    Vampire.display()
    pygame.display.update()

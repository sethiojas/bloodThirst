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
                    if Vampire.is_close_to_vampire(ai[i]):
                        ai.pop(i)

        elif event.type == pygame.KEYUP:
            if (event.key == pygame.K_RIGHT or
            event.key == pygame.K_LEFT):
                Vampire.change_pos('stop')

    for i in range(len(ai)):
        out_of_window = ai[i].move()
        if out_of_window:
            ai.pop(i)

    Vampire.display()
    pygame.display.update()

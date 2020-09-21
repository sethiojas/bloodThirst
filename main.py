import pygame
from time import time
from random import randint
from screen import Screen
from vampire import Vampire
from pedestrian import Pedestrian
from hunter import Hunter

pygame.init()

run = True

ai = [Pedestrian()]
vampire_hunter = Hunter()
while run:
    
    if int(time()) % 5 == 0 and len(ai) < 3:
        ai.append(Pedestrian())

    Screen.load()
    
    deletion_list = []

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                Vampire.change_pos('right')
            elif event.key == pygame.K_LEFT:
                Vampire.change_pos('left')
            elif event.key == pygame.K_SPACE:
                for bot in ai:
                    if Vampire.is_close_to_vampire(bot):
                        deletion_list.append(bot)
            elif event.key == pygame.K_LALT:
                Vampire.hide_if_near_dumpster()
                        

        elif event.type == pygame.KEYUP:
            if (event.key == pygame.K_RIGHT or
            event.key == pygame.K_LEFT):
                Vampire.change_pos('stop')

    for bot in ai:
        out_of_window = bot.move()
        if out_of_window:
            deletion_list.append(bot)
   
    Vampire.display()
    vampire_hunter.move()
    pygame.display.update()

    if deletion_list:
        for item in deletion_list:
            ai.remove(item)

import pygame
from screen import Screen
from random import randint

class Pedestrian:

    def __init__(self):
        rand_number = randint(0, 1)
        x_pos = [-64, Screen.window_x()]
        pos_change = [0.2, -0.2]
        self._PEDESTRIAN_IMAGE = pygame.image.load('images/woman.png')
        self._pedestrian_position_x = x_pos[rand_number]
        self._pedestrian_position_y = 490
        self._position_change = pos_change[rand_number]

    def move(self):
        self._pedestrian_position_x += self._position_change
        Screen.screen.blit(self._PEDESTRIAN_IMAGE, (self._pedestrian_position_x, self._pedestrian_position_y))

        if (self._pedestrian_position_x < -64 or
            self._pedestrian_position_x > 800):
            return True
        return False


    def get_x(self):
        return self._pedestrian_position_x

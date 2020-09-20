import pygame
from screen import Screen
from vampire import Vampire

class Pedestrian:
    def __init__(self):
        self._PEDESTRIAN_IMAGE = pygame.image.load('images/woman.png')
        self._pedestrian_position_x = 0
        self._pedestrian_position_y = 490
        self._position_change = 0.2

    def move(self):
        self._pedestrian_position_x += self._position_change
        Screen.screen.blit(self._PEDESTRIAN_IMAGE, (self._pedestrian_position_x, self._pedestrian_position_y))

        if (self._pedestrian_position_x < 0 or
            self._pedestrian_position_x > 800):
            return True
        return False


    def get_x(self):
        return self._pedestrian_position_x

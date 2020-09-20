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

    def is_close_to_vampire(self):
        if self._pedestrian_position_x - Vampire.get_x() < 40:
            return True
        return False

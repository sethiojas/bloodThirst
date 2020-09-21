import pygame
from screen import Screen
from random import randint


class Hunter:
    rand_number = randint(0, 1)
    x_pos = [-64, Screen.window_x()]
    pos_change = [0.2, -0.2]
    hunter_images = ['hunter_right', 'hunter_left']
    range_images = ['range_right', 'range_left']
    range_offsets = [63, -200]

    def __init__(self):
        self._range_y_coordinate = 490
        self._turn_around()

    def move(self):
        self._hunter_position_x += self._position_change
        Screen.screen.blit(
            self._HUNTER_IMAGE, (self._hunter_position_x, self._hunter_position_y))
        
        Screen.screen.blit(
            self._RANGE_IMAGE,
            (self._hunter_position_x + self._range_offset,
            self._range_y_coordinate)
        )

        if (self._hunter_position_x < -64 or
                self._hunter_position_x > 800):
            self._turn_around()

    def _turn_around(self):
        self.rand_number = 0 if self.rand_number == 1 else 1

        self._HUNTER_IMAGE = pygame.image.load(
            'images/' +
            self.hunter_images[self.rand_number] +
            '.png')
       
        self._RANGE_IMAGE = pygame.image.load(
            'images/' +
            self.range_images[self.rand_number] +
            '.png')

        self._range_offset = self.range_offsets[self.rand_number]
        self._hunter_position_x = self.x_pos[self.rand_number]
        self._hunter_position_y = 500
        self._position_change = self.pos_change[self.rand_number]


import pygame
from screen import Screen
from vampire import Vampire
from random import randint


class Hunter:
    rand_number = randint(0, 1)
    moving_dir = 'right' if rand_number == 0 else 'left'
    x_pos = [-64, Screen.window_x()]
    pos_change = [0.3, -0.3]
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
        return self.check_if_caught()

    def _turn_around(self):
        self.rand_number = 0 if self.rand_number == 1 else 1
        self.moving_dir = 'right' if self.rand_number == 0 else 'left'
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

    def check_if_caught(self):
        position_difference = self._hunter_position_x - Vampire.get_x()

        if (
                (
                    (self.moving_dir == 'right' and
                    position_difference >= -240 and
                    position_difference <= 0
                    )
                    or
                    (self.moving_dir == 'left' and
                    position_difference <= 240 and
                    position_difference >= 0
                    )
                ) and
                not Vampire.hidden_status()
            ):
            pygame.quit()
       


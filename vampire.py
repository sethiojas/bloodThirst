import pygame
from screen import Screen

class Vampire:
    _VAMPIRE_IMAGE = pygame.image.load('images/vampire.png')
    _VAMPIRE_SPEED = 0.4
    _vampire_position_x = 10
    _vampire_position_y = 490
    _position_change = 0

    @classmethod
    def display(cls):
        cls._vampire_position_x = cls._vampire_position_x + cls._position_change

        if cls._vampire_position_x < 0:
            cls._vampire_position_x = 0
        elif cls._vampire_position_x > Screen.window_x() - 64:
            cls._vampire_position_x = Screen.window_x() - 64

        Screen.screen.blit(cls._VAMPIRE_IMAGE, (cls._vampire_position_x, cls._vampire_position_y))

    @classmethod
    def change_pos(cls, moving):
        if moving == 'left':
            cls._position_change = -cls._VAMPIRE_SPEED
        elif moving == 'right':
            cls._position_change = cls._VAMPIRE_SPEED
        elif moving == 'stop':
            cls._position_change = 0

    @classmethod
    def get_x(cls):
        return cls._vampire_position_x


import pygame
from screen import Screen

class Vampire:
    _VAMPIRE_IMAGE = pygame.image.load('images/vampire.png')
    _VAMPIRE_SPEED = 0.4
    _vampire_position_x = 364
    _vampire_position_y = 490
    _position_change = 0
    isHidden = False
    dumpster_hiding_ranges = [(106, 298), (506, 698)]

    @classmethod
    def display(cls):
        if cls.isHidden:
            return

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
    def is_close_to_vampire(cls, object):
        if abs(object.get_x() - cls._vampire_position_x) <= 40:
            return True
        return False

    @classmethod
    def hide_if_near_dumpster(cls):
        if cls.isHidden:
            cls.isHidden = False
            return

        for interval in cls.dumpster_hiding_ranges:
            if (cls._vampire_position_x >= interval[0] and
                cls._vampire_position_x <= interval[1]):
                cls.isHidden = True
                cls._position_change = 0


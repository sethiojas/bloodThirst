import pygame

class Screen:
    _WINDOW = (800, 600)
    _NIGHT_SKY_COLOR = (11, 16, 38)
    _MOON_IMAGE = pygame.image.load('images/moon.png')
    _MOON_POSITION = (720, 10)

    _ROAD_IMAGE = pygame.image.load('images/road.png')

    screen = pygame.display.set_mode(_WINDOW)

    @classmethod
    def load(cls):
        cls.screen.fill(cls._NIGHT_SKY_COLOR)
        cls.screen.blit(cls._MOON_IMAGE, cls._MOON_POSITION)
        for x in range(0, 800, 64):
            cls.screen.blit(cls._ROAD_IMAGE, (x, 536))

    @classmethod
    def window_x(cls):
        return cls._WINDOW[0]
        

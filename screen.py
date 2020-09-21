import pygame

class Screen:
    _WINDOW = (800, 600)
    _NIGHT_SKY_COLOR = (11, 16, 38)
    _MOON_IMAGE = pygame.image.load('images/moon.png')
    _MOON_POSITION = (720, 10)

    _ROAD_IMAGE = pygame.image.load('images/road.png')
    _ROAD_Y_COORDINATE = _WINDOW[1] -64
    
    _DUMPSTER_IMAGE = pygame.image.load('images/dumpster.png')
    _DUMPSTER_Y_COORDINATE = _ROAD_Y_COORDINATE - 64

    screen = pygame.display.set_mode(_WINDOW)

    @classmethod
    def load(cls):
        cls.screen.fill(cls._NIGHT_SKY_COLOR)
        cls.screen.blit(cls._MOON_IMAGE, cls._MOON_POSITION)
        for x in range(0, 800, 64):
            cls.screen.blit(cls._ROAD_IMAGE, (x, cls._ROAD_Y_COORDINATE))
        cls.screen.blit(cls._DUMPSTER_IMAGE, (170, cls._DUMPSTER_Y_COORDINATE))
        cls.screen.blit(cls._DUMPSTER_IMAGE, (570, cls._DUMPSTER_Y_COORDINATE))


    @classmethod
    def window_x(cls):
        return cls._WINDOW[0]
        

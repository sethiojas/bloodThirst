import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Blood Thirst')

night_sky_color_rgb = (11, 16, 38)

moon_image = pygame.image.load('images/moon.png')
moon_coordinates = (720, 10)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
    screen.fill(night_sky_color_rgb)
    screen.blit(moon_image, moon_coordinates)
    pygame.display.update()

    

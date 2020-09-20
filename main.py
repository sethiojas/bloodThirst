import pygame

pygame.init()
window = (800, 600)
screen = pygame.display.set_mode(window)
pygame.display.set_caption('Blood Thirst')

night_sky_color_rgb = (11, 16, 38)

moon_image = pygame.image.load('images/moon.png')
moon_coordinates = (720, 10)

vampire_image = pygame.image.load('images/vampire.png')
vampire_x_coordinate = 10
vampire_speed = 0.4

def move_vampire(x):
    # 520 is the y coordinate of vampire which is constant
    x = 0 if x < 0 else x
    x = window[0] - 64 if x > window[0] - 64 else x
    screen.blit(vampire_image, (x, 520))

vampire_x_change = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                vampire_x_change = -vampire_speed
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                vampire_x_change = vampire_speed
        elif event.type == pygame.KEYUP:
            if (event.key == pygame.K_LEFT or
                event.key == pygame.K_a or
                event.key == pygame.K_RIGHT or
                event.key == pygame.K_d):
                vampire_x_change = 0
                

    screen.fill(night_sky_color_rgb)
    screen.blit(moon_image, moon_coordinates)
    vampire_x_coordinate += vampire_x_change
    move_vampire(round(vampire_x_coordinate))
    pygame.display.update()

    

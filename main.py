import pygame
pygame.init()

from screeninfo import get_monitors

monitor = get_monitors()[0]

resolution_height = monitor.height
scrolling = False

if resolution_height < 1024:
    side_size = resolution_height - 72
    scrolling = True
    scrolling_height = side_size - 1024
    scrolling_width = side_size - 1024

screen = pygame.display.set_mode((side_size, side_size))
base_img = pygame.image.load("mapa_z_miejscami_na_pionki.png")

pygame.mixer.music.load("music1.mp3")
pygame.mixer.music.play()

done = False

while not done:

    mouse_x, mouse_y = pygame.mouse.get_pos()

    if not pygame.mixer.music.get_busy():
        print('restart')
        pygame.mixer.music.play()

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_SPACE:
                done = True

    if scrolling:
        if mouse_x > side_size - 80:
            scrolling_width -= 5
        if mouse_x > side_size - 40:
            scrolling_width -= 15

        if mouse_x < 80:
            scrolling_width += 5
        if mouse_x < 40:
            scrolling_width += 15

        if mouse_y > side_size - 80:
            scrolling_height -= 5
        if mouse_y > side_size - 40:
            scrolling_height -= 15

        if mouse_y < 80:
            scrolling_height += 5
        if mouse_y < 40:
            scrolling_height += 15

    if scrolling_height < side_size - 1024:
        scrolling_height = side_size - 1024
    if scrolling_height > 0:
        scrolling_height = 0

    if scrolling_width < side_size - 1024:
        scrolling_width = side_size - 1024
    if scrolling_width > 0:
        scrolling_width = 0


    screen.fill((0,0,0))
    screen.blit(base_img,(scrolling_width,scrolling_height))
    pygame.display.flip()
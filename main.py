import pygame

pygame.init()

screen = pygame.display.set_mode((720, 720))
base_img = pygame.image.load("mapa.png")

pygame.mixer.music.load("music1.mp3")
pygame.mixer.music.play()

done = False

while not done:

    if not pygame.mixer.music.get_busy():
        print('restart')
        pygame.mixer.music.play()

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_SPACE:
                done = True


    screen.blit(base_img,(0,0))
    pygame.display.flip()
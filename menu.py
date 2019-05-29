
from pygame.locals import *
from random import randrange
import os
import time
from random import randint

from tkinter import *

import pygame
from player import *
from button import *
pygame.init()
from screeninfo import get_monitors
import pygameMenu
from pygameMenu.locals import *


COLOR_BACKGROUND = (128, 0, 128)
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
FPS = 60.0
MENU_BACKGROUND_COLOR = (228, 55, 36)
WINDOW_SIZE = (1024, 1024)

pygame.init()
os.environ['SDL_VIDEO_CENTERED'] = '1'

surface = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('Menu')
clock = pygame.time.Clock()
dt = 1 / FPS


DIFFICULTY = ['2']



def change_difficulty(d):
    print ('Wybrany poziom: {0}'.format(d))
    DIFFICULTY[0] = d


def random_color():
    return randrange(0, 255), randrange(0, 255), randrange(0, 255)


def play_function(difficulty, font):
    difficulty = difficulty[0]
    assert isinstance(difficulty, str)

    gra(difficulty)


    bg_color = random_color()
    f_width = f.get_size()[0]

    main_menu.disable()
    main_menu.reset(1)

    while True:

        clock.tick(60)

        playevents = pygame.event.get()
        for e in playevents:
            if e.type == QUIT:
                exit()
            elif e.type == KEYDOWN: ######### Wylaczanie gry
                if e.key == K_ESCAPE and main_menu.is_disabled():
                    main_menu.enable()


                    return

        main_menu.mainloop(playevents)

        surface.fill(bg_color)
        surface.blit(f, ((WINDOW_SIZE[0] - f_width) / 2, WINDOW_SIZE[1] / 2))
        pygame.display.flip()



def gra(difficulty):
    monitor = get_monitors()[0]
    okno = Tk()
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
    pygame.mixer.music.set_volume(0.2)


    if difficulty == '2':
            players = [PlayerOne(screen), PlayerTwo(screen)]
    elif difficulty == '3':
        players = [PlayerOne(screen), PlayerTwo(screen), PlayerThree(screen)]
    elif difficulty == '4':
        players = [PlayerOne(screen), PlayerTwo(screen), PlayerThree(screen), PlayerFour(screen)]
    elif difficulty == '5':
        players = [PlayerOne(screen), PlayerTwo(screen), PlayerThree(screen), PlayerFour(screen), PlayerFive(screen)]
    elif difficulty == '6':
        players = [PlayerOne(screen), PlayerTwo(screen), PlayerThree(screen), PlayerFour(screen), PlayerFive(screen),PlayerSix(screen)]
    elif difficulty == '7':
        players = [PlayerOne(screen), PlayerTwo(screen), PlayerThree(screen), PlayerFour(screen),PlayerFive(screen), PlayerSix(screen), PlayerSeven(screen)]
    elif difficulty == '8':
        players = [PlayerOne(screen), PlayerTwo(screen), PlayerThree(screen), PlayerFour(screen),
                   PlayerFive(screen), PlayerSix(screen), PlayerSeven(screen), PlayerEight(screen)]

    go = Button(0, 0, 50, 50, 'hello', screen)

    done = False
    while not done:

        go.x = scrolling_width + 512
        go.y = scrolling_height + 512

        mouse_x, mouse_y = pygame.mouse.get_pos()

        if not pygame.mixer.music.get_busy():
            print('restart')
            pygame.mixer.music.play()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    done = True
                for player in players:

                    print(str(player))
                    ix=  randint(1, 6)
                    iy= randint(1, 6)
                    event.key = pygame.K_9
                    print(ix,iy)
                    for i in range(1,ix+iy+1):
                        print("ruch gracza " + str(player))
                        player.position.get_next()
                        time.sleep(0.05)

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

        screen.fill((0, 0, 0))
        screen.blit(base_img, (scrolling_width, scrolling_height))

        for i in players:
            i.show(scrolling_width, scrolling_height)

        go.show_and_update(mouse_x, mouse_y, pygame.mouse.get_pressed())

        if go.pressed:
            done = True

        pygame.display.flip()



def main_background():
    surface.fill(COLOR_BACKGROUND)


play_menu = pygameMenu.Menu(surface,
                            bgfun=main_background,
                            color_selected=COLOR_WHITE,
                            font=pygameMenu.fonts.FONT_BEBAS,
                            font_color=COLOR_BLACK,
                            font_size=30,
                            menu_alpha=100,
                            menu_color=MENU_BACKGROUND_COLOR,
                            menu_height=int(WINDOW_SIZE[1] * 0.6),
                            menu_width=int(WINDOW_SIZE[0] * 0.6),
                            onclose=PYGAME_MENU_DISABLE_CLOSE,
                            option_shadow=False,
                            title='Menu gry',
                            window_height=WINDOW_SIZE[1],
                            window_width=WINDOW_SIZE[0]
                            )
play_menu.add_option('Start', play_function, DIFFICULTY,
                     pygame.font.Font(pygameMenu.fonts.FONT_FRANCHISE, 30))
play_menu.add_selector('Ilu graczy', [('2', '2'),
                                             ('3', '3'),
                                             ('4', '4'),
                                             ('5', '5'),
                                             ('6', '6'),
                                             ('7', '7'),
                                             ('8', '8')],
                       onreturn=None,
                       onchange=change_difficulty)
play_menu.add_option('Powrot', PYGAME_MENU_BACK)



main_menu = pygameMenu.Menu(surface,
                            bgfun=main_background,
                            color_selected=COLOR_WHITE,
                            font=pygameMenu.fonts.FONT_BEBAS,
                            font_color=COLOR_BLACK,
                            font_size=30,
                            menu_alpha=100,
                            menu_color=MENU_BACKGROUND_COLOR,
                            menu_height=int(WINDOW_SIZE[1] * 0.6),
                            menu_width=int(WINDOW_SIZE[0] * 0.6),
                            onclose=PYGAME_MENU_DISABLE_CLOSE,
                            option_shadow=False,
                            title='Menu glowne',
                            window_height=WINDOW_SIZE[1],
                            window_width=WINDOW_SIZE[0]
                            )
main_menu.add_option('Graj', play_menu)
main_menu.add_option('Wyjscie', PYGAME_MENU_EXIT)

while True:

    clock.tick(60)

    events = pygame.event.get()
    for event in events:
        if event.type == QUIT:
            exit()

    main_menu.mainloop(events)

    pygame.display.flip()

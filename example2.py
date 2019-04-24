
# Import pygame and libraries
from pygame.locals import *
from random import randrange
import os
import pygame

# Import pygameMenu
import pygameMenu
from pygameMenu.locals import *

ABOUT = [
         'Author: {0}'.format(pygameMenu.__author__)]
COLOR_BACKGROUND = (128, 0, 128)
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
FPS = 60.0
MENU_BACKGROUND_COLOR = (228, 55, 36)
WINDOW_SIZE = (1024, 1024)

# -----------------------------------------------------------------------------
# Init pygame
pygame.init()
os.environ['SDL_VIDEO_CENTERED'] = '1'

# Create pygame screen and objects
surface = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('Menu')
clock = pygame.time.Clock()
dt = 1 / FPS

# Global variables
DIFFICULTY = ['2']


# -----------------------------------------------------------------------------

def change_difficulty(d):
    """
    Change difficulty of the game.
    
    :return: 
    """
    print ('Wybrany poziom: {0}'.format(d))
    DIFFICULTY[0] = d


def random_color():
    """
    Return random color.
    
    :return: Color tuple
    """
    return randrange(0, 255), randrange(0, 255), randrange(0, 255)


def play_function(difficulty, font):
    """
    Main game function
    
    :param difficulty: Difficulty of the game
    :param font: Pygame font
    :return: None
    """
    difficulty = difficulty[0]
    assert isinstance(difficulty, str)


    if difficulty == '2':
        f = font.render(' 2', 1, COLOR_WHITE)
    elif difficulty == '3':
        f = font.render('3', 1, COLOR_WHITE)
    elif difficulty == '4':
        f = font.render('4', 1, COLOR_WHITE)
    elif difficulty == '5':
        f = font.render('5', 1, COLOR_WHITE)
    elif difficulty == '6':
        f = font.render('6', 1, COLOR_WHITE)
    elif difficulty == '7':
        f = font.render('7', 1, COLOR_WHITE)
    elif difficulty == '8':
        f = font.render('8', 1, COLOR_WHITE)
    else:
        raise Exception('Nieznany {0}'.format(difficulty))

    # Draw random color and text
    bg_color = random_color()
    f_width = f.get_size()[0]

    # Reset main menu and disable
    # You also can set another menu, like a 'pause menu', or just use the same
    # main_menu as the menu that will check all your input.
    main_menu.disable()
    main_menu.reset(1)

    while True:

        # Clock tick
        clock.tick(60)

        # Application events
        playevents = pygame.event.get()
        for e in playevents:
            if e.type == QUIT:
                exit()
            elif e.type == KEYDOWN:
                if e.key == K_ESCAPE and main_menu.is_disabled():
                    main_menu.enable()

                    # Quit this function, then skip to loop of main-menu on line 217
                    return

        # Pass events to main_menu
        main_menu.mainloop(playevents)

        # Continue playing
        surface.fill(bg_color)
        surface.blit(f, ((WINDOW_SIZE[0] - f_width) / 2, WINDOW_SIZE[1] / 2))
        pygame.display.flip()


def main_background():
    """
    Function used by menus, draw on background while menu is active.
    
    :return: None
    """
    surface.fill(COLOR_BACKGROUND)


# -----------------------------------------------------------------------------
# PLAY MENU
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
# When pressing return -> play(DIFFICULTY[0], font)
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

# ABOUT MENU
about_menu = pygameMenu.TextMenu(surface,
                                 bgfun=main_background,
                                 color_selected=COLOR_WHITE,
                                 font=pygameMenu.fonts.FONT_BEBAS,
                                 font_color=COLOR_BLACK,
                                 font_size_title=30,
                                 font_title=pygameMenu.fonts.FONT_8BIT,
                                 menu_color=MENU_BACKGROUND_COLOR,
                                 menu_color_title=COLOR_WHITE,
                                 menu_height=int(WINDOW_SIZE[1] * 0.6),
                                 menu_width=int(WINDOW_SIZE[0] * 0.6),
                                 onclose=PYGAME_MENU_DISABLE_CLOSE,
                                 option_shadow=False,
                                 text_color=COLOR_BLACK,
                                 text_fontsize=20,
                                 title='O nas',
                                 window_height=WINDOW_SIZE[1],
                                 window_width=WINDOW_SIZE[0]
                                 )
for m in ABOUT:
    about_menu.add_line(m)
about_menu.add_line(PYGAMEMENU_TEXT_NEWLINE)
about_menu.add_option('Powrot', PYGAME_MENU_BACK)

# MAIN MENU
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
main_menu.add_option('O nas', about_menu)
main_menu.add_option('Wyjscie', PYGAME_MENU_EXIT)

# -----------------------------------------------------------------------------
# Main loop
while True:

    # Tick
    clock.tick(60)

    # Application events
    events = pygame.event.get()
    for event in events:
        if event.type == QUIT:
            exit()

    # Main menu
    main_menu.mainloop(events)

    # Flip surface
    pygame.display.flip()

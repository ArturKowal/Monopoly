from pygame import draw
from cyclic_list import *

class Player:

    def __init__(self, color, position_list, name, screen):
        self.color = color
        self.position_list = position_list
        self.position = cyclic_list(40)
        for x in range(40):
            self.position.add(x)
        self.in_prison = False
        self.possesions = []
        self.balance = 2000
        self.name = name
        self.screen = screen

    def show(self, offset_x, offset_y):
        rect_pos_and_size = (self.position_list[self.position.get_current()][0]+offset_x, self.position_list[self.position.get_current()][1]+offset_y,19,19)
        draw.rect(self.screen, self.color, rect_pos_and_size, 0)

playerOnePaths = [(896, 999),(808,999), (724, 999), (640, 999), (556, 999), (472, 999), (388, 999), (304, 999), (220, 999), (136, 999), (5, 896), (5, 808), (5, 724), (5, 640), (5,556), (5, 472), (5, 388), (5, 304), (5, 220), (5,136), (108, 5), (196, 5), (280, 5), (364, 5), (448, 5), (532, 5), (616, 5), (700, 5), (784, 5), (868, 5), (999, 108), (999, 196), (999, 280), (999, 364), (999, 448), (999, 532), (999, 616), (999, 700), (999, 784), (999, 868), (999, 952)]

playerTwoPaths = [(917,999),(828, 999),(744, 999),(660, 999),(576, 999),(492, 999),(408, 999),(324, 999),(240, 999),(156, 999),(5,917),(5, 828), (5, 744), (5, 660), (5, 576), (5, 492), (5, 408), (5, 324), (5, 240), (5, 156),(87,5),(176, 5), (260, 5), (344, 5), (428, 5), (512, 5), (596, 5), (680, 5), (764, 5), (848, 5),(999,87),(999, 176), (999, 260), (999, 344), (999, 428), (999, 512), (999, 596), (999, 680), (999, 764), (999, 848)]

playerThreePaths = [(938,999),(848, 999), (764, 999), (680, 999), (596, 999), (512, 999), (428, 999), (344, 999), (260, 999), (176, 999),(5,938),(5, 848), (5, 764), (5, 680), (5, 596), (5, 512), (5, 428), (5, 344), (5, 260), (5, 176),(66,5),(156, 5), (240, 5), (324, 5), (408, 5), (492, 5), (576, 5), (660, 5), (744, 5), (828, 5),(999,66),(999, 156), (999, 240), (999, 324), (999, 408), (999, 492), (999, 576), (999, 660), (999, 744), (999, 828)]

playerFourPaths = [(959,999),(868, 999), (784, 999), (700, 999), (616, 999), (532, 999), (448, 999), (364, 999), (280, 999), (196, 999),(5,959),(5, 868), (5, 784), (5, 700), (5, 616), (5, 532), (5, 448), (5, 364), (5, 280), (5, 196), (45,5),(136, 5), (220, 5), (304, 5), (388, 5), (472, 5), (556, 5), (640, 5), (724, 5), (808, 5),(999,45), (999, 136), (999, 220), (999, 304), (999, 388), (999, 472), (999, 556), (999, 640), (999, 724), (999, 808)]

playerFivePaths = [(999,959),(808, 979), (724, 979), (640, 979), (556, 979), (472, 979), (388, 979), (304, 979), (220, 979), (136, 979),(45,999),(25, 808), (25, 724), (25, 640), (25, 556), (25, 472), (25, 388), (25, 304), (25, 220), (25, 136),(5,45),(196, 25), (280, 25), (364, 25), (448, 25), (532, 25), (616, 25), (700, 25), (784, 25), (868, 25),(959,5),(979, 196), (979, 280), (979, 364), (979, 448), (979, 532), (979, 616), (979, 700), (979, 784), (979, 868)]

playerSixPaths = [(999,938),(828, 979), (744, 979), (660, 979), (576, 979), (492, 979), (408, 979), (324, 979), (240, 979), (156, 979),(66,999),(25, 828), (25, 744), (25, 660), (25, 576), (25, 492), (25, 408), (25, 324), (25, 240), (25, 156), (5,66), (176, 25), (260, 25), (344, 25), (428, 25), (512, 25), (596, 25), (680, 25), (764, 25), (848, 25), (938,5), (979, 176), (979, 260), (979, 344), (979, 428), (979, 512), (979, 596), (979, 680), (979, 764), (979, 848)]

playerSevenPaths = [(999,917),(848, 979), (764, 979), (680, 979), (596, 979), (512, 979), (428, 979), (344, 979), (260, 979), (176, 979), (87,999), (25, 848), (25, 764), (25, 680), (25, 596), (25, 512), (25, 428), (25, 344), (25, 260), (25, 176), (5,87), (156, 25), (240, 25), (324, 25), (408, 25), (492, 25), (576, 25), (660, 25), (744, 25), (828, 25), (917,5), (979, 156), (979, 240), (979, 324), (979, 408), (979, 492), (979, 576), (979, 660), (979, 744), (979, 828)]

playerEightPaths = [(999,896), (868, 979), (784, 979), (700, 979), (616, 979), (532, 979), (448, 979), (364, 979), (280, 979), (196, 979), (108,999),(25, 868), (25, 784), (25, 700), (25, 616), (25, 532), (25, 448), (25, 364), (25, 280), (25, 196), (5,108), (136, 25), (220, 25), (304, 25), (388, 25), (472, 25), (556, 25), (640, 25), (724, 25), (808, 25),(986,5), (979, 136), (979, 220), (979, 304), (979, 388), (979, 472), (979, 556), (979, 640), (979, 724), (979, 808)]



class PlayerOne(Player):
    def __init__(self, screen):
        super().__init__((255,0,0), playerOnePaths, "test", screen)

class PlayerTwo(Player):
    def __init__(self, screen):
        super().__init__((255,215,0), playerTwoPaths, "test", screen)

class PlayerThree(Player):
    def __init__(self, screen):
        super().__init__((138,43,226), playerThreePaths, "test", screen)

class PlayerFour(Player):
    def __init__(self, screen):
        super().__init__((50,205,50), playerFourPaths, "test", screen)

######################upper row#######################
class PlayerFive(Player):
    def __init__(self, screen):
        super().__init__((70,130,180), playerFivePaths, "test", screen)

class PlayerSix(Player):
    def __init__(self, screen):
        super().__init__((112,128,144), playerSixPaths, "test", screen)

class PlayerSeven(Player):
    def __init__(self, screen):
        super().__init__((139,69,19), playerSevenPaths, "test", screen)
    
class PlayerEight(Player):
    def __init__(self, screen):
        super().__init__((255,0,255), playerEightPaths, "test", screen)


'''cheat: 
def ReturnList(x,y):
         return [(x, y+84*i) for i in range(10)]

         
         
         '''
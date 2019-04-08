from pygame import draw

class Player:

    def __init__(self, color, position_list, name, screen):
        self.color = color
        self.position_list = position_list
        self.position = 0
        self.in_prison = False
        self.possesions = []
        self.balance = 2000
        self.name = name
        self.screen = screen
    
    def show(self):
        rect_pos_and_size = (self.position_list[self.position][0],self.position_list[self.position][1],19,19)
        draw.rect(self.screen, self.color, rect_pos_and_size, 0)



class PlayerOne(Player):
    def __init__(self, screen):
        super().__init__((255,0,0), [(0,0)], "test", screen)
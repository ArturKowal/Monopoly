from pygame import draw

class Button:
    def __init__(self, x, y, width, height, text, screen):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.fill = (150,150,150)
        self.text = text
        self.screen = screen
        self.pressed = False

    def show_and_update(self, mouseX, mouseY, mouseClicked):
        draw.rect(self.screen, self.fill, (self.x, self.y, self.width, self.height), 0)
        draw.rect(self.screen, (0,0,0), (self.x, self.y, self.width, self.height), 1)
        
        if (mouseX > self.x) and (mouseY > self.y) and (mouseX < self.x + self.width) and (mouseY < self.y + self.height) and mouseClicked:
            self.pressed = True
        else:
            self.pressed = False
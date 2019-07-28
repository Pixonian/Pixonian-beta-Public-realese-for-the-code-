import pygame

#UI Elements File
#Text, Buttons, and more soon.

font = pygame.font.Font("./resources/font/belligerent.ttf", 60)

class button(pygame.sprite.Sprite):
    def __init__(self, text, pos, color, centered=False):
        global font
        pygame.sprite.Sprite.__init__(self)
        self.image = font.render(str(text), 1, list(color))
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = list(pos)
        if centered:
            self.rect.left = self.rect.left - self.rect.width/2
    def click(self, pos):
        clicked = False
        if self.rect.collidepoint(pos[0], pos[1]):
            clicked = True
        return clicked
    def update(self, window):
        window.blit(self.image, [self.rect.left, self.rect.top])

class rectbutton(pygame.sprite.Sprite):
    def __init__(self, rect, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.surface.Surface([rect[0], rect[1]])
        self.image.fill([255, 255, 255])
        self.image.set_alpha(100)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = pos
    def click(self, pos):
        clicked = False
        if self.rect.collidepoint(pos[0], pos[1]):
            clicked = True
        return clicked
    def update(self, window):
        window.blit(self.image, [self.rect.left, self.rect.top])

def text(textstr, color, pos, window):
    global font
    render = font.render(str(textstr), 1, list(color))
    window.blit(render, list(pos))

def centeredText(textstr, color, pos, window):
    global font
    render = font.render(str(textstr), 1, list(color))
    rect = render.get_rect()
    window.blit(render, [pos[0]-(rect.width/2), pos[1]])

def changeFontSize(size):
    global font
    font = pygame.font.Font("./resources/font/belligerent.ttf", size)
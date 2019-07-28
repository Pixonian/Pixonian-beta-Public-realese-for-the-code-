import pygame, random

pygame.init()

#Game Engine File

class backdrop(pygame.sprite.Sprite):
    def __init__(self, pos):

        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("./resources/images/backdrop.png")
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = list(pos)
        self.newimagerequest = None
        self.imagename = "backdrop"

    def scroll(self, speed, window, returnparameters):
        global backdrop1, backdrop2

        if self.rect.left <= -800:
            self.rect.left = -800
            self.rect.left += 1600 #Reset to other off-screen edge
            if not self.newimagerequest == None:
                if self.newimagerequest == "endgame":
                    self.image = pygame.image.load("./resources/images/"+self.newimagerequest+".png")
                    self.imagename = self.newimagerequest
                    if self == backdrop1:
                        backdrop2.newimagerequest = None
                    elif self == backdrop2:
                        backdrop1.newimagerequest = None
                else:
                    self.image = pygame.image.load("./resources/images/"+self.newimagerequest+".png")
                    self.imagename = self.newimagerequest
        elif self.imagename == "endgame" and self.rect.left > 0 and self.rect.left < speed:
            returnparameters.returnbkg = True
            self.rect.left = 0

        else:
            self.rect.left -= speed #Move left by speed pixels

        window.blit(self.image, [self.rect.left, self.rect.top])

class Player(pygame.sprite.Sprite):
    def __init__(self, lane):
        pygame.sprite.Sprite.__init__(self)
        self.images = [pygame.image.load("./resources/images/player/player.png"), pygame.image.load("./resources/images/player/player-2.png")]
        self.image = self.images[0]
        self.imageindex = 0
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = 50, 50 + (int(lane)*200)
        self.lane = int(lane)
        self.moving = False
    def draw(self, window):
        window.blit(self.image, [self.rect.left, self.rect.top])
    def animate(self):
        if self.imageindex == 0:
            self.imageindex += 1
        else:
            self.imageindex = 0
        self.image = self.images[self.imageindex]
    def move(self):
        if self.rect.top < (50 + (self.lane * 200)):
            self.rect.top += 10
            self.moving = True
        elif self.rect.top > (50 + (self.lane * 200)):
            self.rect.top -= 10
            self.moving = True
        elif self.rect.top == (50 + (self.lane * 200)):
            self.moving = False

backdrop1 = backdrop([0, 0])
backdrop2 = backdrop([800, 0])
def scrolling(speed, window, returnparameters):
    global backdrop1, backdrop2
    backdrop1.scroll(speed, window, returnparameters)
    backdrop2.scroll(speed, window, returnparameters)
    return returnparameters.returnbkg

def newImage(image):
    global backdrop1, backdrop2
    backdrop1.newimagerequest = str(image)
    backdrop2.newimagerequest = str(image)

def resetImage(image):
    global backdrop1, backrop2
    backdrop1.newimagerequest = None
    backdrop2.newimagerequest = None
    backdrop1.imagename = str(image)
    backdrop2.imagename = str(image)
    backdrop1.image = pygame.image.load("./resources/images/" + str(image) + ".png")
    backdrop2.image = pygame.image.load("./resources/images/" + str(image) + ".png")
import pygame, random

#Objects File

pygame.init()
powerupimgs = {"bandage":pygame.image.load("./resources/images/bandage.png"), "medkit":pygame.image.load("./resources/images/medkit.png"), "coffee":pygame.image.load("./resources/images/coffee.png")}
objectimages = {"oil spill":pygame.image.load("./resources/images/oil-spill.png"), "traffic cone":pygame.image.load("./resources/images/traffic-cone.png"), "fallen tree":pygame.image.load("./resources/images/tree.png"),
                "puddle":pygame.image.load("./resources/images/puddle.png"), "manhole":pygame.image.load("./resources/images/manhole.png"), "construction":pygame.image.load("./resources/images/construction.png"),
                "car":pygame.image.load("./resources/images/car.png")}

class obstacle(pygame.sprite.Sprite):
    def __init__(self, lane, type):
        global objectimages
        pygame.sprite.Sprite.__init__(self)
        self.lane = int(lane)
        self.type = str(type)
        if self.type == "fallen tree" or self.type == "construction":
            try:
                self.image = objectimages[str(type)]
            except:
                self.image = pygame.surface.Surface([300, 100])
        else:
            worked = True
            try:
                self.image = objectimages[str(type)]
            except:
                worked = False
            if not worked:
                self.image = pygame.surface.Surface([100, 100])
                self.image.fill([255, 0, 0])

        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = random.randint(800, 850), 50 + (lane*200)
    def update(self, speed):
        #SCROLLING AND RESETING
        if self.rect.left >= -300:
            self.rect.left -= speed
        elif self.rect.left < -300:
            self.kill()

class powerup(pygame.sprite.Sprite):
    def __init__(self, lane, type):
        pygame.sprite.Sprite.__init__(self)
        self.type = str(type)
        try:
            self.image = powerupimgs[self.type]
        except:
            self.image = pygame.surface.Surface([50, 50])

        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = random.randint(800, 850), (75 + (lane*200))
    def update(self, speed):
        if self.rect.left >= -50:
            self.rect.left -= speed
        elif self.rect.left < -50:
            self.kill()

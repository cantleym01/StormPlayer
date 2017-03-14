import pygame

class Sprite(pygame.sprite.Sprite):
    destructable = False
    identity = 0 #0 = misc, 1 = player

    def __init__(self, sprite, startx, starty, width, height, identity = 0):
        super().__init__()

        self.identity = identity

        self.width = width
        self.height = height

        #set the image
        self.image = pygame.image.load(sprite)

        #Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()

        #set the starting location
        self.rect.topleft = [startx, starty]

        #scale the image down to a manageable size
        self.image = pygame.transform.smoothscale(self.image, (width, height))

        #scale hitbox to new size
        self.rect = self.rect.clip(pygame.Rect(startx, starty, width, height))

    def collide(self, coll, speed):
        #player clause
        if self.identity == 1:
            for hit in coll:
                if hit.identity == 0: #a thing was hit
                    if speed > 0:  #was moving right
                        while pygame.sprite.collide_rect(self, hit):
                            self.rect.centerx -= 1
                        return 1 #a barrier to not go past
                    if speed < 0:  #was moving left
                        while pygame.sprite.collide_rect(self, hit):
                            self.rect.centerx += 1
                        return 1 #a barrier to not go past
        return 0
        #this will return a number. So far, only 0 and 1 are accounted for (0 means nothing to worry about, 1 is player hitting a barrier)
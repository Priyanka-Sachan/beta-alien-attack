import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet"""

    def __init__(self,screen,settings):
        super(Alien,self).__init__()
        self.screen=screen
        self.settings=settings

        self.image=pygame.image.load('images/space_ship.bmp')
        self.image=pygame.transform.scale(self.image,(80,80))
        self.rect=self.image.get_rect()

        self.rect.x=self.rect.width
        self.rect.y=self.rect.height

        self.x=float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image,self.rect)
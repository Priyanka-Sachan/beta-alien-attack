import pygame

class Ship():
    
    """ Class to control the ship"""
    def __init__(self,screen,settings):
        self.screen=screen
        self.speed=settings.ship_speed
        
        self.image=pygame.image.load('images/ship_hard.bmp')
        self.image=pygame.transform.scale(self.image,(50,100))
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()
            
        self.rect.centerx=self.screen_rect.centerx
        self.center=float(self.rect.centerx)
        self.rect.bottom=self.screen_rect.bottom

        self.moving_right=False
        self.moving_left=False

    def update(self):
        if self.moving_right and self.rect.right<self.screen_rect.right:
            self.center+=self.speed
        if self.moving_left and self.rect.left>0:
            self.center-=self.speed
        self.rect.centerx=self.center

    def blitme(self):
        self.screen.blit(self.image,self.rect)
            
            
    

import pygame.font
from pygame.sprite import Group

from ship import Ship

class Scoreboard():
    """A class to report scoring information."""

    def __init__(self,screen,settings,stats):
        self.screen=screen
        self.screen_rect=screen.get_rect()
        self.settings=settings
        self.stats=stats

        self.text_color=(255,255,255)
        self.font=pygame.font.SysFont(None,48)
        
        self.prep_level()
        self.prep_score()
        self.prep_high_score()
        self.prep_ships()

    def prep_score(self):
        rounded_score=int(round(self.stats.score,-1))
        score_str="{:,}".format(rounded_score)
        self.score_image=self.font.render("Score: "+score_str,True,self.text_color,self.settings.bg_color)
        self.score_rect=self.score_image.get_rect()
        self.score_rect.right=self.level_rect.left-200
        self.score_rect.top=20

    def prep_high_score(self):
        high_score=int(round(self.stats.high_score,-1))
        high_score_str="{:,}".format(high_score)
        self.high_score_image=self.font.render("High Score: "+high_score_str,True,self.text_color,self.settings.bg_color)
        self.high_score_rect=self.high_score_image.get_rect()
        self.high_score_rect.centerx=self.screen_rect.centerx-200
        self.high_score_rect.top=self.score_rect.top

    def prep_level(self):
        self.level_image=self.font.render("Level: "+str(self.stats.level),True,self.text_color,self.settings.bg_color)
        self.level_rect=self.level_image.get_rect()
        self.level_rect.right=self.screen_rect.right-50
        self.level_rect.top=20

    def prep_ships(self):
        self.ships=Group()
        for ship_number in range(self.stats.ships_left):
            ship=Ship(self.screen,self.settings)
            ship.rect.x=10+ship_number*ship.rect.width
            ship.rect.y=10
            ship.image=pygame.transform.scale(ship.image,(25,50))
            self.ships.add(ship)

    def show_score(self):
        self.screen.blit(self.score_image,self.score_rect)
        self.screen.blit(self.high_score_image,self.high_score_rect)
        self.screen.blit(self.level_image,self.level_rect)
        self.ships.draw(self.screen)
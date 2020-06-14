import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf

def run_game():
    
    pygame.init()
    settings=Settings()
    screen=pygame.display.set_mode((settings.screen_width,settings.screen_height))
    pygame.display.set_caption("ALIEN INVASION")
    ship=Ship(screen,settings)
    alien=Alien(screen,settings)
    bullets=Group()
    aliens=Group()
    gf.create_fleet(screen,settings,ship,aliens)
    while True:
        gf.check_events(screen,settings,ship,bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_aliens(settings,aliens)
        gf.update_screen(screen,settings,ship,aliens,bullets)
        
run_game()

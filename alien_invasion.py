import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    
    pygame.init()
    settings=Settings()
    screen=pygame.display.set_mode((settings.screen_width,settings.screen_height))
    pygame.display.set_caption("ALIEN INVASION")
    ship=Ship(screen,settings)
    bullets=Group()
    while True:
        gf.check_events(screen,settings,ship,bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(screen,settings,ship,bullets)
        
run_game()

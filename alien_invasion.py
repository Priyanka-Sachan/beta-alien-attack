import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from alien import Alien
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
import game_functions as gf

def run_game():
    
    pygame.init()
    settings=Settings()
    screen=pygame.display.set_mode((settings.screen_width,settings.screen_height))
    pygame.display.set_caption("ALIEN INVASION")
    play_button=Button(screen,settings,"PLAY")
    stats=GameStats(settings)
    sb=Scoreboard(screen,settings,stats)
    ship=Ship(screen,settings)
    alien=Alien(screen,settings)
    bullets=Group()
    aliens=Group()
    gf.create_fleet(screen,settings,ship,aliens)
    while True:
        gf.check_events(screen,settings,stats,sb,play_button,ship,aliens,bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(screen,settings,stats,sb,ship,aliens,bullets)
            gf.update_aliens(screen,settings,stats,sb,ship,aliens,bullets)
        gf.update_screen(screen,settings,stats,sb,ship,aliens,bullets,play_button)
        
run_game()

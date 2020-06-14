import sys
import pygame
from time import sleep

from bullet import Bullet
from alien import Alien

def check_keydown_events(event,screen,settings,ship,bullets):
    if event.key==pygame.K_RIGHT:
        ship.moving_right=True
    elif event.key==pygame.K_LEFT:
        ship.moving_left=True
    elif event.key==pygame.K_SPACE:
        fire_bullet(screen,settings,ship,bullets)
    elif event.key==pygame.K_q:
        sys.exit()

def check_keyup_events(event,ship):
    if event.key==pygame.K_RIGHT:
        ship.moving_right=False
    if event.key==pygame.K_LEFT:
        ship.moving_left=False
        
def check_events(screen,settings,ship,bullets):
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            check_keydown_events(event,screen,settings,ship,bullets)
        elif event.type==pygame.KEYUP:
            check_keyup_events(event,ship)

def update_screen(screen,settings,ship,aliens,bullets):
    #screen.fill(settings.bg_color)
    bg_image=pygame.image.load('images/background.jpg')
    bg_image=pygame.transform.scale(bg_image,(settings.screen_width,settings.screen_height))
    screen.blit(bg_image,(0,0))
    ship.blitme()
    aliens.draw(screen)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    pygame.display.flip()

def update_bullets(screen,settings,ship,aliens,bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom<=0:
            bullets.remove(bullet)
    check_alien_bullet_collision(screen,settings,ship,aliens,bullets)
    

def check_alien_bullet_collision(screen,settings,ship,aliens,bullets):
    collisions=pygame.sprite.pygame.sprite.groupcollide(aliens, bullets, True, True)
    if len(aliens)==0:
        bullets.empty()
        create_fleet(screen,settings,ship,aliens)


def fire_bullet(screen,settings,ship,bullets):
    if len(bullets)<settings.bullets_allowed:
        new_bullet=Bullet(screen,settings,ship)
        bullets.add(new_bullet)

def ship_hit(screen,settings,stats,ship,aliens,bullets):
    if stats.ships_left>0:
        stats.ships_left-=1
        aliens.empty()
        bullets.empty()
        create_fleet(screen,settings,ship,aliens)
        ship.center_ship()
        sleep(0.5)
    else:
        stats.game_active=False

def check_alien_bottom(screen,settings,stats,ship,aliens,bullets):
    screen_rect=screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom>=screen_rect.bottom:
            ship_hit(screen,settings,stats,ship,aliens,bullets)
            break

def check_fleet_edges(settings,aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_directions(settings,aliens)
            break

def change_fleet_directions(settings,aliens):
    for alien in aliens.sprites():
        alien.rect.y+=settings.fleet_drop_speed
    settings.fleet_direction*=-1

def update_aliens(screen,settings,stats,ship,aliens,bullets):
    check_fleet_edges(settings,aliens)
    for alien in aliens:
        alien.update()
    if pygame.sprite.spritecollideany(ship,aliens):
        ship_hit(screen,settings,stats,ship,aliens,bullets)
    check_alien_bottom(screen,settings,stats,ship,aliens,bullets)

def get_number_aliens_x(settings,alien_width):
    available_space_x=settings.screen_width-2*alien_width
    number_aliens_x=int(available_space_x/(2*alien_width))
    return number_aliens_x

def get_number_aliens_y(settings,ship_height,alien_height):
    available_space_y=settings.screen_height-(2*alien_height)-ship_height
    number_aliens_y=int(available_space_y/(2*alien_height))
    return number_aliens_y

def create_alien(screen,settings,aliens,alien_number_x,alien_number_y):
    alien=Alien(screen,settings)
    alien.rect.y=alien.rect.height+1.5*alien.rect.height*alien_number_y
    alien.rect.x=alien.rect.width+2*alien.rect.width*alien_number_x
    alien.x=alien.rect.x
    if alien_number_y%2:
        alien.rect.x+=alien.rect.width
        alien.x=alien.rect.x
    aliens.add(alien)

def create_fleet(screen,settings,ship,aliens):
    alien=Alien(screen,settings)
    number_aliens_x=get_number_aliens_x(settings,alien.rect.width)
    number_aliens_y=get_number_aliens_y(settings,ship.rect.height,alien.rect.height)
    for alien_number_y in range(number_aliens_y):
        for alien_number_x in range(number_aliens_x):
            create_alien(screen,settings,aliens,alien_number_x,alien_number_y)

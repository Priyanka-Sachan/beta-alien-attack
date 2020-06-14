import sys
import pygame

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

def update_bullets(bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom<=0:
            bullets.remove(bullet)

def fire_bullet(screen,settings,ship,bullets):
    if len(bullets)<settings.bullets_allowed:
        new_bullet=Bullet(screen,settings,ship)
        bullets.add(new_bullet)

def check_fleet_edges(settings,aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_directions(settings,aliens)
            break

def change_fleet_directions(settings,aliens):
    for alien in aliens.sprites():
        alien.rect.y+=settings.fleet_drop_speed
    settings.fleet_direction*=-1

def update_aliens(settings,aliens):
    check_fleet_edges(settings,aliens)
    for alien in aliens:
        alien.update()

def get_number_aliens_x(settings,alien_width):
    available_space_x=settings.screen_width-2*alien_width
    number_aliens_x=int(available_space_x/(2*alien_width))
    return number_aliens_x

def get_number_aliens_y(settings,ship_height,alien_height):
    available_space_y=settings.screen_height-(3*alien_height)-ship_height
    number_aliens_y=int(available_space_y/(2*alien_height))
    return number_aliens_y

def create_alien(screen,settings,aliens,alien_number_x,alien_number_y):
    alien=Alien(screen,settings)
    alien.rect.x=alien.rect.width+2*alien.rect.width*alien_number_x
    alien.x=alien.rect.x
    alien.rect.y=alien.rect.height+2*alien.rect.height*alien_number_y
    aliens.add(alien)

def create_fleet(screen,settings,ship,aliens):
    alien=Alien(screen,settings)
    number_aliens_x=get_number_aliens_x(settings,alien.rect.width)
    number_aliens_y=get_number_aliens_y(settings,ship.rect.height,alien.rect.height)
    for alien_number_y in range(number_aliens_y):
        for alien_number_x in range(number_aliens_x):
            create_alien(screen,settings,aliens,alien_number_x,alien_number_y)

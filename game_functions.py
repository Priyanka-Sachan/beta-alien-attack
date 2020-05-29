import sys
import pygame

from bullet import Bullet

def check_keydown_events(event,screen,settings,ship,bullets):
    if event.key==pygame.K_RIGHT:
        ship.moving_right=True
    elif event.key==pygame.K_LEFT:
        ship.moving_left=True
    elif event.key==pygame.K_SPACE:
        fire_bullet(screen,settings,ship,bullets)

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

def update_screen(screen,settings,ship,bullets):
    #screen.fill(settings.bg_color)
    bg_image=pygame.image.load('images/background.jpg')
    screen.blit(bg_image,(0,0))
    ship.blitme()
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

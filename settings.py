class Settings():
    
    """A class to store all settings for Alien Invasion."""
    def __init__(self):
        self.screen_height=700
        self.screen_width=1000
        self.bg_color=(230,230,230)
        self.ship_speed=1
        self.ship_speed_factor=1
        self.ship_limit=3
        self.bullet_speed=1
        self.bullet_width=300
        self.bullet_height=15
        self.bullet_color=(255,255,255)
        self.bullets_allowed=3
        self.alien_speed_factor=1
        self.fleet_drop_speed=30
        #fleet_diretion of 1 represents right ;-1 represents left.
        self.fleet_direction=1

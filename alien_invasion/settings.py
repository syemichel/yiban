import pygame

class Settings():

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)
        self.fps = 60
        self.clock = pygame.time.Clock()
        self.ship_speed_factor = 5
        self.bullet_speed_factor = 5
        self.bullet_width = 10
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullet_allowed = 60
        self.alien_speed_factor = 5
        self.fleet_drop_speed = 20
        self.fleet_direction = 1
        self.ship_limit = 3

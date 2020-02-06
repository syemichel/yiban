import pygame

class Variables():
    def __init__(self,screen,settings):
        self.screen_rect = screen.get_rect()
        self.value = 1
        self.rect = pygame.Rect(0,0,settings.body_width,settings.body_height)
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery + settings.body_height
        self.body_limit = 5
        self.game_active = False
        self.score = 0

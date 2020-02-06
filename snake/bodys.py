import pygame
from pygame.sprite import Sprite

class Body(Sprite):
    def __init__(self,settings,screen):
        super().__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.rect = pygame.Rect(0,0,settings.body_width,settings.body_height)
        self.rect.center = self.screen_rect.center
        self.color = settings.body_color

    def draw_body(self):
        pygame.draw.rect(self.screen,self.color,self.rect)


        

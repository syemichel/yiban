import pygame
import random

class Egg():
    def __init__(self,screen,settings):
       
        self.screen = screen
        self.color = settings.egg_color
        self.rect = pygame.Rect(random.randint(0,settings.screen_mode[0]-settings.egg_width),random.randint(0,settings.screen_mode[1]-settings.egg_height),settings.egg_width,settings.egg_height)

    def draw_egg(self):
        pygame.draw.rect(self.screen,self.color,self.rect)
                       

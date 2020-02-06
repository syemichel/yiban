import pygame

class Buttons():
    def __init__(self,msg,screen,settings):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.text_color = settings.text_color
        self.button_color = settings.button_color
        self.button_width = settings.button_width
        self.button_height = settings.button_height
        self.font = pygame.font.SysFont(settings.font_style,settings.button_text_size)
        self.rect = pygame.Rect(0,0,self.button_width,self.button_height)
        self.rect.center = self.screen_rect.center
        self.prep_msg(msg)
    def prep_msg(self,msg):
        self.msg_image = self.font.render(msg,True,self.text_color,self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.screen_rect.center

    def draw_button(self):
        self.screen.fill(self.button_color,self.rect)
        self.screen.blit(self.msg_image,self.msg_image_rect)
    
        

import pygame

class Score():
    def __init__(self,settings,screen,variables):
        self.variables = variables
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.font = pygame.font.SysFont(settings.font_style,settings.score_text_size)
        self.score_color = settings.score_color
        self.screen_color = settings.screen_color
        self.prep_score()
        
    def prep_score(self):
        score_str = str(self.variables.score)
        self.score_image = self.font.render(score_str,True,self.score_color,self.screen_color)
        self.score_image_rect = self.score_image.get_rect()
        self.score_image_rect.right = self.screen_rect.right - 20
        self.score_image_rect.top = 20

    def show_score(self):
        self.screen.blit(self.score_image,self.score_image_rect)
        
        
        
    

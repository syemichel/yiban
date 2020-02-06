import pygame
from settings import Settings
from bodys import Body
from pygame.sprite import Group
import game_function as gf
from variable import Variables
from eggs import Egg
from buttons import Buttons
from score import Score
def run_game():
    pygame.init()
    
    settings = Settings()
    screen = pygame.display.set_mode(settings.screen_mode)
    pygame.display.set_caption(settings.game_name)
    bodys = Group()
    variables = Variables(screen,settings)
    egg = Egg(screen,settings)
    play_button = Buttons("play",screen,settings)
    score = Score(settings,screen,variables)
    #set the parametre of the screen
    while True:
        
        gf.event_check(variables,play_button)
        if variables.game_active:
            gf.create_bodys(bodys,settings,screen,variables,score)
            bodys.update()
            gf.update_egg(bodys,variables,egg,settings,score)
        gf.screen_update(settings,screen,bodys,egg,play_button,variables,score)
    
    #main loop
run_game()

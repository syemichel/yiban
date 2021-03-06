import sys
import pygame
from bodys import Body
from variable import Variables
from time import sleep
from eggs import Egg
import random
from buttons import Buttons
from score import Score
def screen_update(settings,screen,bodys,egg,play_button,variables,score):
    settings.clock.tick(settings.fps)
    screen.fill(settings.screen_color)
    for body in bodys.sprites():
        body.draw_body()
    egg.draw_egg()
    if not variables.game_active :
        play_button.draw_button()
    score.show_score()
    pygame.display.flip()

def event_check(variables,play_button):
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                keydown_check(event,variables)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x,mouse_y = pygame.mouse.get_pos()
                check_play_button(mouse_x,mouse_y,variables,play_button)
                
def create_bodys(bodys,settings,screen,variables,score):
    new_body = Body(settings,screen)
    update_variable_rect(new_body,bodys,settings,screen,variables)
    game_over(new_body,bodys,variables,settings,score)
    bodys.add(new_body)
    for body in bodys.sprites():
        if len(bodys) > variables.body_limit:
            bodys.remove(body)
            break
    
def keydown_check(event,variables):
    if event.key == pygame.K_q:
        sys.exit()
    elif event.key == pygame.K_UP and variables.value != 2:
        variables.value = 1
    elif event.key == pygame.K_DOWN and variables.value != 1:
        variables.value = 2
    elif event.key == pygame.K_LEFT and variables.value != 4:
        variables.value = 3
    elif event.key == pygame.K_RIGHT and variables.value != 3:
        variables.value = 4

def selecte_edge_reach(screen,variables,settings):
    if variables.value <= 2:
        if variables.rect.y < 0:
            variables.rect.y = settings.screen_mode[1] - settings.body_height
        if variables.rect.y > settings.screen_mode[1]:
            variables.rect.y = 0
    if variables.value > 2:
        if variables.rect.x < 0:
            variables.rect.x = settings.screen_mode[0] - settings.body_width
        if variables.rect.x > settings.screen_mode[0]:
            variables.rect.x = 0;

def update_variable_rect(new_body,bodys,settings,screen,variables):
     if variables.value <= 2:
        
        variables.rect.y +=  settings.body_height * (-1)**variables.value
        selecte_edge_reach(screen,variables,settings)
        new_body.rect.center = variables.rect.center
     else :
        variables.rect.x += settings.body_width * (-1)**variables.value
        selecte_edge_reach(screen,variables,settings)
        new_body.rect.center = variables.rect.center
        
def update_egg(bodys,variables,egg,settings,score):
    if pygame.sprite.spritecollideany(egg,bodys):
       
        variables.body_limit += 1
        variables.score += 1
        score.prep_score()
        egg.rect.x = random.randint(0,settings.screen_mode[0]-settings.egg_width)
        egg.rect.y = random.randint(0,settings.screen_mode[1]-settings.egg_height)      

def game_over(new_body,bodys,variables,settings,score):
    if pygame.sprite.spritecollideany(new_body,bodys):
        sleep(0.5)
        bodys.empty()
        variables.body_limit = settings.body_limit_init
        variables.score = 0
        score.prep_score()
        variables.game_active = False

def check_play_button(mouse_x,mouse_y,variables,play_button):
    if play_button.rect.collidepoint(mouse_x,mouse_y):
        variables.game_active = True

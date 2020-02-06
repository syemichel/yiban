import pygame
import game_functions as gf
from settings import Settings
from ship import Ship
from pygame.sprite import Group
from alien import Alien
from game_stats import GameStats
from button import Button

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen =pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    clock = pygame.time.Clock()
    ship = Ship(ai_settings,screen)
    bullets = Group()
    aliens = Group()
    stats = GameStats(ai_settings)
    gf.create_fleet(ai_settings,screen,ship,aliens)
    play_button = Button(ai_settings,screen,"play")
    while True:
      gf.check_events(stats,play_button,ai_settings,ship,screen,aliens,bullets)
      if stats.game_active :
          ship.update()
          gf.update_bullets(ai_settings,screen,ship,aliens,bullets)
          gf.update_aliens(ai_settings,aliens,ship,stats,bullets,screen)
      gf.update_screen(ai_settings,screen,ship,aliens,bullets,play_button,stats)

run_game()

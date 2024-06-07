import pygame 
import random 

from player import Player
from enemies import Enemies
from burst import Burst
from settings import Settings
import game_functions as gf 


def run_game():
    pygame.init()
    pygame.mixer.init()
    ai_settings = Settings()
    explosion_list = gf.fill_list_images(ai_settings)
    window = pygame.display.set_mode((ai_settings.width, ai_settings.height))
    pygame.display.set_caption("JUego Space Invaders")
    clock = pygame.time.Clock()
    player = Player(ai_settings.width,ai_settings.height,ai_settings.player_group,ai_settings.bullets_group_player,ai_settings.laser_sound) 
    ai_settings.player_group.add(player)
    ai_settings.bullets_group_player.add(player)
    gf.charge_enemies(ai_settings)
    score = ai_settings.score
    run = True 
    while run:
        score = ai_settings.score
        clock.tick(ai_settings.fps)
        window.blit(ai_settings.fondo, (0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.disparar()
        ai_settings.player_group.update()
        ai_settings.enemy_group.update()
        ai_settings.bullets_group_player.update()
        ai_settings.enemy_bullets_group.update()
        ai_settings.player_group.draw(window)
        gf.collisions1(ai_settings)

        if gf.collisions2(player,ai_settings) == False:
            print("Game over")
            run = False
    
        if gf.hits(player,ai_settings) == False:
            print("Game over")
            run = False

        gf.texto_puntuacion(ai_settings,window, (' SCORE: '+ str(score)+ '       '), 30, ai_settings.width-85,2)
        gf.barra_vida(ai_settings,window,ai_settings.width-285,0,player.vida)

        pygame.display.flip()
    pygame.quit()
    
run_game()
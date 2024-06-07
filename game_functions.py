import pygame
from enemies import Enemies
from burst import Burst

def texto_puntuacion(ai_settings,frame,text,size,x,y):
    font = pygame.font.SysFont('Small Fonts', size, bold=True)
    text_frame = font.render(text, True, ai_settings.blanco, ai_settings.negro)
    text_rect = text_frame.get_rect()
    text_rect.midtop = (x,y)
    frame.blit(text_frame, text_rect)

def barra_vida(ai_settings,frame,x,y,nivel):
    longitud = 100
    alto=20
    fill=int((nivel/100)*longitud)
    border=pygame.Rect(x,y,longitud,alto)
    fill=pygame.Rect(x,y,fill,alto)
    pygame.draw.rect(frame,(255,0,255),fill)
    pygame.draw.rect(frame,ai_settings.negro,border,4)
    
def fill_list_images(ai_settings):
    for i in range(1,13):
        explosion = pygame.image.load(f"explosion/{i}.png")
        ai_settings.explosion_list.append(explosion)

    return ai_settings.explosion_list

def collisions1(ai_settings):
    colicion1 = pygame.sprite.groupcollide(ai_settings.enemy_group,ai_settings.bullets_group_player,True,True)
    for i in colicion1:
        ai_settings.score +=10
        enemigo = Enemies(300,10,ai_settings.width,ai_settings.height,ai_settings.player_group,ai_settings.enemy_bullets_group,ai_settings.laser_sound)
        enemigo.disparar_enemigos()
        ai_settings.enemy_group.add(enemigo)
        ai_settings.player_group.add(enemigo)

        explo = Burst(i.rect.center,ai_settings.explosion_list)
        ai_settings.player_group.add(explo)
        ai_settings.burst_sound.set_volume(0.3)
        ai_settings.burst_sound.play()

def collisions2(player,ai_settings):
    colicion2 = pygame.sprite.spritecollide(player, ai_settings.enemy_bullets_group, True)
    for j in colicion2:
        player.vida -= 10
        if player.vida <= 0:
            #run = False
            return False
            
        explo1 = Burst(j.rect.center,ai_settings.explosion_list)
        ai_settings.player_group.add(explo1)
        ai_settings.knock_sound.play()

def hits(player,ai_settings):
    hits = pygame.sprite.spritecollide(player, ai_settings.enemy_group, False)
    for hit in hits:
        player.vida -= 100
        enemigos = Enemies(10,10,ai_settings.width,ai_settings.height,ai_settings.player_group,ai_settings.enemy_bullets_group,ai_settings.laser_sound)
        ai_settings.player_group.add(enemigos)
        ai_settings.enemy_group.add(enemigos)
        if player.vida <= 0:
            #print("Game Over")
            #run = False
            return False

def charge_enemies(ai_settings):
    for x in range(10):
        enemigo = Enemies(10,10,ai_settings.width,ai_settings.height,ai_settings.player_group,ai_settings.enemy_bullets_group,ai_settings.laser_sound)
        ai_settings.enemy_group.add(enemigo)
        ai_settings.player_group.add(enemigo)




import pygame
import random 

from bullets_enemy import Balas_enemigos

class Enemies(pygame.sprite.Sprite):
    def __init__(self,x,y,width,height,player_group,enemy_bullets_group,laser_sound):
        super().__init__()
        self.image = pygame.image.load('imagenes/E1.png').convert_alpha()
        self.width = width
        self.height = height
        self.player_group = player_group
        self.enemy_bullets_group = enemy_bullets_group
        self.laser_sound = laser_sound
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(1, width-50)
        self.rect.y = 10
        self.velocidad_y = random.randrange(-5,20)
    
    def update(self):
        self.time = random.randrange(-1, pygame.time.get_ticks()//5000)
        self.rect.x += self.time
        if self.rect.x >= self.width:
            self.rect.x = 0
            self.rect.y += 50
    
    def disparar_enemigos(self):
        bala = Balas_enemigos(self.rect.centerx, self.rect.bottom,self.width,self.height,self.player_group)
        self.player_group.add(bala)
        self.enemy_bullets_group.add(bala)
        self.laser_sound.play()
import pygame
import random 

class Balas_enemigos(pygame.sprite.Sprite):
    def __init__(self,x,y,width,height,player_group):
        super().__init__()
        self.image = pygame.image.load('imagenes/B1.png').convert_alpha()
        self.width = width
        self.height = height
        self.player_group = player_group
        self.image = pygame.transform.rotate(self.image,180)
        self.rect = self.image.get_rect()
        self.rect.centerx = x 
        self.rect.y = random.randrange(10, width) 
        self.velocidad_y = 4
    
    def update(self):
        self.rect.y += self.velocidad_y
        if self.rect.bottom > self.height:
            self.kill()

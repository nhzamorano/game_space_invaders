import pygame
from bullets_player import Bullets 

class Player(pygame.sprite.Sprite):
    def __init__(self,width,height,player_group,bullets_group_player,laser_sound):
        super().__init__()
        self.image=pygame.image.load('imagenes/A1.png').convert_alpha()
        pygame.display.set_icon(self.image)
        self.width = width
        self.height = height
        self.player_group = player_group
        self.bullets_group_player = bullets_group_player
        self.laser_sound = laser_sound
        self.rect = self.image.get_rect()
        self.rect.centerx=self.width//2
        self.rect.centery=self.height-50
        self.velocidad_x=0
        self.vida=100
    
    def update(self):
        self.velocidad_x = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.velocidad_x= -5
        elif keystate[pygame.K_RIGHT]:
            self.velocidad_x = 5

        self.rect.x += self.velocidad_x
        if self.rect.right > self.width:
            self.rect.right=self.width
        elif self.rect.left <0:
            self.rect.left = 0
    
    def disparar(self):
        self.bullet = Bullets(self.rect.centerx, self.rect.top)
        self.player_group.add(self.bullet)
        self.bullets_group_player.add(self.bullet)
        self.laser_sound.play()
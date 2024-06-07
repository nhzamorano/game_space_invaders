import pygame 

class Bullets(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.image.load('imagenes/B2.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = x 
        self.rect.y = y 
        self.velocidad = -18
    
    def update(self):
        self.rect.y += self.velocidad
        if self.rect.bottom < 0:
            self.kill()
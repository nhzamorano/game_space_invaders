import pygame

class Settings():
    def __init__(self):
        self.blanco = (255,255,255)
        self.negro = (0,0,0)
        self.score = 0
        self.vida = 100
        self.explosion_list = []
        self.fondo = pygame.image.load('imagenes/fondo.png')
        self.width = self.fondo.get_width()
        self.height = self.fondo.get_height()
        self.fps = 60
        self.enemy_group = pygame.sprite.Group()
        self.bullets_group_player = pygame.sprite.Group()
        self.laser_sound = pygame.mixer.Sound('sonidos/laser.wav')
        self.burst_sound = pygame.mixer.Sound('sonidos/explosion.wav')
        self.knock_sound = pygame.mixer.Sound('sonidos/golpe.wav')
        self.player_group = pygame.sprite.Group()
        self.enemy_bullets_group = pygame.sprite.Group()
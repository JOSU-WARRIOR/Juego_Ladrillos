# paleta.py
import pygame
from constantes import ANCHO, ALTO, color_blanco, color_azul

class Paleta(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('juego_clases/imagenes/paleta.png')
        self.rect = self.image.get_rect()
        self.rect.midbottom = (ANCHO / 2, ALTO - 20)
        self.speed = [0, 0]

    def update(self, evento):
        if evento.key == pygame.K_LEFT and self.rect.left > 0:
            self.speed = [-5, 0]
        elif evento.key == pygame.K_RIGHT and self.rect.right < ANCHO:
            self.speed = [5, 0]
        else:
            self.speed = [0, 0]
        self.rect.move_ip(self.speed)
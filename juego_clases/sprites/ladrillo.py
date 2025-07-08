# ladrillo.py
import pygame
from constantes import ANCHO, ALTO, color_blanco, color_azul

class Ladrillo(pygame.sprite.Sprite):
    def __init__(self, posicion):
        super().__init__()
        self.image = pygame.image.load('juego_clases/imagenes/ladrillo.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = posicion
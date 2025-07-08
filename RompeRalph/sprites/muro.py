# muro.py
import pygame
from sprites.ladrillo import Ladrillo
from constantes import ANCHO, ALTO

class Muro(pygame.sprite.Group):
   def __init__(self, disposiciones):
        super().__init__()
        for pos in disposiciones:
            ladrillo = Ladrillo(pos)
            self.add(ladrillo)
# muro.py
import pygame
from sprites.ladrillo import Ladrillo
from constantes import ANCHO, ALTO

class Muro(pygame.sprite.Group):
    def __init__(self, cantidadLadrillos):
        super().__init__()
        pos_x = 0
        pos_y = 20
        for i in range(cantidadLadrillos):
            ladrillo = Ladrillo((pos_x, pos_y))
            self.add(ladrillo)
            pos_x += ladrillo.rect.width
            if pos_x >= ANCHO:
                pos_x = 0
                pos_y += ladrillo.rect.height
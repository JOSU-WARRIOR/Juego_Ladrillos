# escenas/juego_terminado.py
from escena import Escena
import pygame
from constantes import ANCHO, ALTO, color_blanco, color_azul

class EscenaJuegoTerminado(Escena):
    def actualizar(self):
        self.jugando = False

    def dibujar(self, pantalla):
        pantalla.fill(color_azul)
        fuente = pygame.font.SysFont('Arial', 72)
        texto = fuente.render('Juego Terminado', True, color_blanco)
        rect = texto.get_rect(center=(ANCHO // 2, ALTO // 2))
        pantalla.blit(texto, rect)

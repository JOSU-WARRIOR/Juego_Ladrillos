#pantallaInicio.py
from escena import Escena
import pygame
from constantes import ANCHO, ALTO, color_azul, color_blanco

class EscenaInicio(Escena):
    def __init__(self):
        super().__init__()

    def leer_eventos(self, eventos):
        for evento in eventos:
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_RETURN:
                self.cambiar_escena('Nivel1')

    def actualizar(self):
        pass

    def dibujar(self, pantalla):
        pantalla.fill(color_azul)
        fuente_titulo = pygame.font.SysFont('Arial', 60)
        fuente_indicacion = pygame.font.SysFont('Consolas', 30)

        texto_titulo = fuente_titulo.render('ROMPE MUROS', True, color_blanco)
        texto_pulsa = fuente_indicacion.render('Pulsa ENTER para comenzar', True, color_blanco)

        rect_titulo = texto_titulo.get_rect(center=(ANCHO // 2, ALTO // 2 - 50))
        rect_pulsa = texto_pulsa.get_rect(center=(ANCHO // 2, ALTO // 2 + 30))

        pantalla.blit(texto_titulo, rect_titulo)
        pantalla.blit(texto_pulsa, rect_pulsa)

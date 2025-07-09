# Pantalla de fin del juego
from escena import Escena
import pygame
import estado_juego as EstadoJuego
from constantes import ANCHO, ALTO, color_azul, color_blanco

class EscenaFin(Escena):
    def __init__(self):
        super().__init__()
        self.fuente_titulo = pygame.font.SysFont('Arial', 60)
        self.fuente_indicacion = pygame.font.SysFont('Consolas', 30)

        self.texto1 = self.fuente_titulo.render('FIN DEL JUEGO', True, color_blanco)
        self.texto2 = self.fuente_titulo.render('GRACIAS POR JUGAR', True, color_blanco)
        self.texto3 = self.fuente_indicacion.render('Pulsa ENTER para volver al inicio', True, color_blanco)
        self.texto4 = self.fuente_indicacion.render('Pulsa ESCAPE para salir', True, color_blanco)

    def actualizar(self):
        pass  # no hay movimiento ni lógica

    def dibujar(self, pantalla):
        pantalla.fill(color_azul)
        pantalla.blit(self.texto1, self.texto1.get_rect(center=(ANCHO // 2, ALTO // 2 - 100)))
        pantalla.blit(self.texto2, self.texto2.get_rect(center=(ANCHO // 2, ALTO // 2 - 30)))
        pantalla.blit(self.texto3, self.texto3.get_rect(center=(ANCHO // 2, ALTO // 2 + 40)))
        pantalla.blit(self.texto4, self.texto4.get_rect(center=(ANCHO // 2, ALTO // 2 + 80)))

    def leer_eventos(self, eventos):
        for evento in eventos:
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                  # Reiniciar estado del juego
                    EstadoJuego.nivel = 1
                    EstadoJuego.puntuacion = 0
                    EstadoJuego.vidas = 3
                    self.cambiar_escena("Nivel1")  # Cambiar a la escena de inicio
                elif evento.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()
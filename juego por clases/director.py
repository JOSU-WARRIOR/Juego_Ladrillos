# director.py
import pygame
import time

class Director:
    def __init__(self, titulo, resolucion, escenas):
        pygame.init()
        self.pantalla = pygame.display.set_mode(resolucion)
        pygame.display.set_caption(titulo)
        self.reloj = pygame.time.Clock()
        self.escenas = escenas
        self.escena_actual = None

    def ejecutar(self, escena_inicial, fps=60):
        self.escena_actual = self.escenas[escena_inicial]()
        jugando = True

        while jugando:
            self.reloj.tick(fps)
            eventos = pygame.event.get()

            for evento in eventos:
                if evento.type == pygame.QUIT:
                    jugando = False
                    self.escena_actual.jugando = False

            self.escena_actual.leer_eventos(eventos)
            self.escena_actual.actualizar()
            self.escena_actual.dibujar(self.pantalla)

            if self.escena_actual.proximaEscena:
                nueva = self.escena_actual.proximaEscena
                self.escena_actual = self.escenas[nueva]()

            jugando = self.escena_actual.jugando
            pygame.display.flip()

        time.sleep(3)

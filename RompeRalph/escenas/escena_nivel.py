from escena import Escena
import pygame
from constantes import ANCHO, ALTO, color_azul, color_blanco
from sprites.bolita import Bolita
from sprites.paleta import Paleta
from muros.cargar_muro import cargar_muro
from estado_juego import EstadoJuego

class EscenaNivel(Escena):
    def __init__(self, nivel, puntuacion=0, vidas=3):
        super().__init__()
        self.nivel = nivel
        self.puntuacion = puntuacion
        self.vidas = vidas
        self.bolita = Bolita()
        self.jugador = Paleta()
        self.muro = cargar_muro(f"Nivel{nivel}")
        self.esperando_saque = True
        pygame.key.set_repeat(30)

    def leer_eventos(self, eventos):
        for evento in eventos:
            if evento.type == pygame.KEYDOWN:
                self.jugador.update(evento)
                if self.esperando_saque and evento.key == pygame.K_SPACE:
                    self.esperando_saque = False
                    if self.bolita.rect.centerx < ANCHO / 2:
                        self.bolita.speed = [3, -3]
                    else:
                        self.bolita.speed = [-3, -3]

    def actualizar(self):
        if not self.esperando_saque:
            self.bolita.update()
        else:
            self.bolita.rect.midbottom = self.jugador.rect.midtop

        if pygame.sprite.collide_rect(self.bolita, self.jugador):
            self.bolita.speed[1] = -self.bolita.speed[1]

        lista = pygame.sprite.spritecollide(self.bolita, self.muro, False)
        if lista:
            #self.muro.remove(lista[0])
            #self.puntuacion += 10
            ladrillo = lista[0]
            cx = self.bolita.rect.centerx
            if cx < ladrillo.rect.left or cx > ladrillo.rect.right:
                self.bolita.speed[0] = -self.bolita.speed[0]
            else:
                self.bolita.speed[1] = -self.bolita.speed[1]
            self.muro.remove(ladrillo)
            self.puntuacion += 10

        if self.bolita.rect.top > ALTO:
            self.vidas -= 1
            self.esperando_saque = True

        if self.vidas <= 0:
            self.cambiar_escena('JuegoTerminado')

        if len(self.muro) == 0:
            EstadoJuego.nivel = self.nivel + 1
            EstadoJuego.puntuacion = self.puntuacion + 50
            EstadoJuego.vidas = self.vidas + 1
            self.cambiar_escena(f'Nivel{EstadoJuego.nivel}')

    def dibujar(self, pantalla):
        pantalla.fill(color_azul)
        self.mostrar_puntuacion(pantalla)
        self.mostrar_vidas(pantalla)
        pantalla.blit(self.bolita.image, self.bolita.rect)
        pantalla.blit(self.jugador.image, self.jugador.rect)
        self.muro.draw(pantalla)

    def mostrar_puntuacion(self, pantalla):
        fuente = pygame.font.SysFont('Consolas', 20)
        texto = fuente.render(str(self.puntuacion).zfill(5), True, color_blanco)
        pantalla.blit(texto, (0, 0))

    def mostrar_vidas(self, pantalla):
        fuente = pygame.font.SysFont('Consolas', 20)
        texto = fuente.render("Vidas: " + str(self.vidas).zfill(2), True, color_blanco)
        texto_rect = texto.get_rect()
        texto_rect.topright = [ANCHO, 0]
        pantalla.blit(texto, texto_rect)

# escena.py
import pygame

class Escena:
    def __init__(self):
        self.proximaEscena = False
        self.jugando = True

    def leer_eventos(self, eventos):
        pass

    def actualizar(self):
        pass

    def dibujar(self, pantalla):
        pass

    def cambiar_escena(self, escena):
        self.proximaEscena = escena
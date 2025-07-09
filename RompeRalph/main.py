# main.py
import pygame
pygame.init()
pygame.mixer.init()

from director import Director
from escenas.pantallaInicio import EscenaInicio
from escenas.escena_nivel import EscenaNivel
from escenas.juego_terminado import EscenaJuegoTerminado
from escenas.escena_fin import EscenaFin
from estado_juego import EstadoJuego
from constantes import ANCHO, ALTO


# Mapeo de escenas para el director
escenas_disponibles = {
    'Inicio': EscenaInicio,
    "Nivel1": lambda: EscenaNivel(1, 0, 3),
    #"Nivel1": lambda: EscenaNivel(EstadoJuego.nivel, EstadoJuego.puntuacion, EstadoJuego.vidas),
    "Nivel2": lambda: EscenaNivel(EstadoJuego.nivel, EstadoJuego.puntuacion, EstadoJuego.vidas),
    "Nivel3": lambda: EscenaNivel(EstadoJuego.nivel, EstadoJuego.puntuacion, EstadoJuego.vidas),
    "Nivel4": lambda: EscenaNivel(EstadoJuego.nivel, EstadoJuego.puntuacion, EstadoJuego.vidas),
    "Fin": lambda: EscenaFin(),
    "JuegoTerminado": EscenaJuegoTerminado
}

# Iniciar juego
director = Director("Rompe Muros", (ANCHO, ALTO), escenas_disponibles)
director.ejecutar("Inicio")

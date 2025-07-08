# main.py
from director import Director
from escenas.escena_nivel import EscenaNivel
from escenas.juego_terminado import EscenaJuegoTerminado
from estado_juego import EstadoJuego
from constantes import ANCHO, ALTO

# Mapeo de escenas para el director
escenas_disponibles = {
    "Nivel1": lambda: EscenaNivel(1, 0, 3),
    "Nivel2": lambda: EscenaNivel(EstadoJuego.nivel, EstadoJuego.puntuacion, EstadoJuego.vidas),
    "Nivel3": lambda: EscenaNivel(EstadoJuego.nivel, EstadoJuego.puntuacion, EstadoJuego.vidas),
    "JuegoTerminado": EscenaJuegoTerminado
}

# Iniciar juego
director = Director("Rompe Muros", (ANCHO, ALTO), escenas_disponibles)
director.ejecutar("Nivel1")

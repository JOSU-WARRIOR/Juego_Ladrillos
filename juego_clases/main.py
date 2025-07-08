# main.py
from director import Director
from escenas.pantallaInicio import EscenaInicio
from escenas.nivel1 import EscenaNivel1
from escenas.juego_terminado import EscenaJuegoTerminado
from constantes import ANCHO, ALTO

# Mapeo de escenas para el director
escenas_disponibles = {
    'Inicio': EscenaInicio,
    'Nivel1': EscenaNivel1,
    'JuegoTerminado': EscenaJuegoTerminado
}

# Iniciar juego
director = Director('Rompe Muros', (ANCHO, ALTO), escenas_disponibles)
director.ejecutar('Inicio')

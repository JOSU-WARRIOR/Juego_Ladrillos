from constantes import ANCHO, ALTO
from sprites.ladrillo import Ladrillo
from sprites.muro import Muro

def muro_escalera():
    ladrillo = Ladrillo((0, 0))
    w, h = ladrillo.rect.width, ladrillo.rect.height
    posiciones = []
    for i in range(6):
        posiciones.append((i * w, 20 + i * h))
    return posiciones
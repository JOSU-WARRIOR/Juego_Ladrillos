from constantes import ANCHO, ALTO
from sprites.ladrillo import Ladrillo
from sprites.muro import Muro

def muro_lineal():
    ladrillo = Ladrillo((0, 0))  # Solo para obtener ancho y alto
    w = ladrillo.rect.width
    h = ladrillo.rect.height
    cantidad = 50  # Número fijo de ladrillos
    posiciones = []

    pos_x, pos_y = 0, 20
    for i in range(cantidad):
        posiciones.append((pos_x, pos_y))
        pos_x += w
        if pos_x + w > ANCHO:  # Si se pasa del borde, salto de línea
            pos_x = 0
            pos_y += h

    return posiciones
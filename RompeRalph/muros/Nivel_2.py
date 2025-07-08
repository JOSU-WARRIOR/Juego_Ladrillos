from constantes import ANCHO, ALTO
from sprites.ladrillo import Ladrillo
from sprites.muro import Muro

def muro_rombo():
    ladrillo = Ladrillo((0, 0))
    w, h = ladrillo.rect.width, ladrillo.rect.height
    centro_x = ANCHO // 2
    centro_y = ALTO // 4
    posiciones = [
        (centro_x, centro_y - 2 * h),
        (centro_x - 2 * w, centro_y),
        (centro_x + 2 * w, centro_y),
        (centro_x, centro_y + 2 * h)
    ]
    return posiciones
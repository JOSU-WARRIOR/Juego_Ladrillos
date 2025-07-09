from constantes import ANCHO, ALTO
from sprites.ladrillo import Ladrillo
from sprites.muro import Muro

def muro_rombo():
    ladrillo = Ladrillo((0, 0))
    w, h = ladrillo.rect.width, ladrillo.rect.height
    centro_x = ANCHO // 2
    centro_y = ALTO // 4
    posiciones = []

    # Número de capas hacia arriba y abajo desde el centro
    capas = 5  # Puedes ajustar esto para cambiar el tamaño visual del rombo

    for fila in range(-capas, capas + 1):  # Desde -5 hasta +5
        num_ladrillos = capas - abs(fila) + 1  # N ladrillos por fila
        offset_y = centro_y + fila * h
        offset_x = centro_x - (num_ladrillos - 1) * w // 2
        for i in range(num_ladrillos):
            x = offset_x + i * w
            y = offset_y
            posiciones.append((x, y))

    # Recortar a máximo 50 ladrillos
    return posiciones[:50]
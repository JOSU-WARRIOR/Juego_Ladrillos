from constantes import ANCHO, ALTO,cantidad, color_azul, color_blanco
from sprites.ladrillo import Ladrillo
from sprites.muro import Muro

def muro_triangulo():
    ladrillo = Ladrillo((0, 0))
    w, h = ladrillo.rect.width, ladrillo.rect.height
    centro_x = ANCHO // 2
    centro_y = ALTO // 4
    posiciones = []

    # Número de capas hacia arriba y abajo desde el centro
    capas = 5  # Puedes ajustar esto para cambiar el tamaño visual del triángulo

    for fila in range(capas + 1):  # Desde 0 hasta 3
        num_ladrillos = fila + 1  # N ladrillos en fila 0
        offset_y = centro_y + fila * h
        offset_x = centro_x - (num_ladrillos - 1) * w // 2  # Numero de ladrillos por fila centrado
        for i in range(num_ladrillos):
            x = offset_x + i * w
            y = offset_y
            posiciones.append((x, y))

    # Recortar a máximo cantidad de ladrillos
    return posiciones[:cantidad]
from constantes import ANCHO, ALTO, cantidad
from sprites.ladrillo import Ladrillo
from sprites.muro import Muro

def muro_escalera():
    ladrillo = Ladrillo((0, 0))
    w, h = ladrillo.rect.width, ladrillo.rect.height

    posiciones = []
    x, y = 0, h  # Punto de inicio
    columna_actual = 0

    for i in range(cantidad):
        posiciones.append((x, y))
        x += w
        y += h
     # Si se pasa de los bordes de la pantalla, reiniciar en una nueva columna
        if x + w > ANCHO:
            break
        if y + h > ALTO // 3:
            columna_actual += 1  # saltamos a la siguiente escalera
            x = columna_actual * 3 * w  # nueva columna escalonada
            y = h  # reinicio arriba
    return posiciones
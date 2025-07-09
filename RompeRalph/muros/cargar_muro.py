from sprites.muro import Muro
from muros.Nivel_1 import muro_lineal
from muros.Nivel_2 import muro_rombo   
from muros.Nivel_3 import muro_escalera
from muros.Nivel_4 import muro_triangulo

def cargar_muro(nombre):
    if nombre == "Nivel1":
        return Muro(muro_lineal())
    elif nombre == "Nivel2":
        return Muro(muro_rombo())
    elif nombre == "Nivel3":
        return Muro(muro_escalera())
    elif nombre == "Nivel4":
        return Muro(muro_triangulo())
    else:
        return Muro([])  # Devuelve muro vacío como respaldo
   
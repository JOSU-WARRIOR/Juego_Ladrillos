from sprites.muro import Muro
from muros.Nivel_1 import muro_lineal
from muros.Nivel_2 import muro_rombo   
from muros.Nivel_3 import muro_escalera

def cargar_muro(nombre):
    if nombre == "Nivel1":
        return Muro(muro_lineal())
    elif nombre == "Nivel2":
        return Muro(muro_rombo())
    elif nombre == "Nivel3":
        return Muro(muro_escalera())
   
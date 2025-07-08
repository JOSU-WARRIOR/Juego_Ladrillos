from sprites.muro import Muro

def cargar_muro(nombre):
    if nombre == "Nivel1":
        return Muro(40)
    elif nombre == "Nivel2":
        return Muro(50)
    elif nombre == "Nivel3":
        return Muro(60)
    else:
        return Muro(20)


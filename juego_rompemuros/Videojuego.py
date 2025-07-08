import sys
import pygame
import time

ancho = 640 # Ancho de la pantalla
alto = 480 # Alto de la pantalla
color_azul = (0, 0, 64) # Color azul oscuro para el fondo
color_blanco = (255, 255, 255) # Color blanco para el texto


# Inicializar Pygame
pygame.init()

class Bolita(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # Cargar imagen
        self.image = pygame.image.load("imagenes/bolita.png")
        # Obtener el rectángulo de la imagen
        self.rect = self.image.get_rect()
        # Posicionar la bolita en el centro de la pantalla
        self.rect.center = (ancho // 2, alto // 2)
        # self.rect.centerx = (ancho // 2)
        # self.rect.centery = (alto // 2)
        # Velocidad de la bolita inicial
        self.speed = [3, 3]

    def update(self):
        # Evitar que la bolita salga de los límites de la pantalla
        if self.rect.left <= 0 or self.rect.right >= ancho:
            self.speed[0] = -self.speed[0]
        # Evitar que la bolita salga de los límites de la pantalla
        if self.rect.top <= 0 :
            self.speed[1] = -self.speed[1]
        # Mover la bolita con respecto a su posición actual y velocidad
        self.rect.move_ip(self.speed)

class Paleta(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # Cargar imagen
        self.image = pygame.image.load("imagenes/paleta.png")
        # Obtener el rectángulo de la imagen
        self.rect = self.image.get_rect()
        # Posicionar la paleta en el centro en la parte inferior de la pantalla 
        self.rect.midbottom = (ancho // 2, alto - 20)
        # self.rect.centerx = (ancho // 2)
        # self.rect.centery = (alto // 2)
        # Velocidad de la bolita inicial
        self.speed = [0, 0]
    
    def update(self, evento):
        # Mover la paleta con respecto a su posición actual y velocidad
        if evento.key == pygame.K_LEFT and self.rect.left > 0:
            self.speed = [-5,0]
        elif evento.key == pygame.K_RIGHT and self.rect.right < ancho:
            self.speed = [5,0]
        else:
            self.speed = [0,0]
        # Mover la paleta con respecto a su posición actual y velocidad
        self.rect.move_ip(self.speed)
                
        # Evitar que la paleta salga de los límites de la pantalla
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > ancho:
            self.rect.right = ancho

class Ladrillo(pygame.sprite.Sprite):
    def __init__(self,posicion):
        pygame.sprite.Sprite.__init__(self)
        # Cargar imagen
        self.image = pygame.image.load("imagenes/ladrillo.png")
        # Obtener el rectángulo de la imagen
        self.rect = self.image.get_rect()
        # Posicionar el ladrillo en la pantalla
        self.rect.topleft = posicion

class Muro(pygame.sprite.Group):
    def __init__(self, cantidadLadrillos):
        pygame.sprite.Group.__init__(self)
        pos_x = 0
        pos_y = 20
        for i in range(cantidadLadrillos):
            ladrillo = Ladrillo((pos_x, pos_y))
            self.add(ladrillo)
            pos_x += ladrillo.rect.width
            if pos_x >= ancho:
                pos_x = 0
                pos_y += ladrillo.rect.height

        """   # Crear ladrillos y agregarlos al grupo
        for i in range(5):  # 5 filas de ladrillos
            for j in range(10):  # 10 ladrillos por fila
                ladrillo = Ladrillo((j * 64, i * 32))  # Espacio entre ladrillos
                self.add(ladrillo)    """
       
def juego_terminado():
    # Si la bolita sale de la pantalla, finalizar el jueg
    fuente = pygame.font.SysFont('Arial', 72)
    texto = fuente.render("Juego Terminado", True, color_blanco)
    texto_rect = texto.get_rect()
    texto_rect.center = (ancho // 2, alto // 2)
    pantalla.blit(texto, texto_rect)
    pygame.display.flip()
    time.sleep(3)  # Esperar 3 segundos
    sys.exit()  # Salir del juego
    # pygame.time.delay(3000)  # Esperar 3 segundos
    # print("Juego terminado. Reiniciando...")

def mostrar_puntuacion():
    # Si la bolita sale de la pantalla por abajo, finalizar el juego
    fuente = pygame.font.SysFont('Consolas', 20)
    texto = fuente.render(str(puntuacion).zfill(5), True, color_blanco)
    texto_rect = texto.get_rect()
    texto_rect.topleft = [0,0]  # Posicionar en la esquina superior izquierda
    pantalla.blit(texto, texto_rect)

def mostrar_vidas():
    # Si la bolita sale de la pantalla por abajo, finalizar el juego
    fuente = pygame.font.SysFont('Consolas', 20)
    cadena = "Vidas: " + str(vidas).zfill(2)
    texto = fuente.render(cadena, True, color_blanco)
    texto_rect = texto.get_rect()
    texto_rect.topright = [ancho,0]  # Posicionar en la esquina superior izquierda
    pantalla.blit(texto, texto_rect)
    
# Inicializar Pantalla
pantalla = pygame.display.set_mode((ancho, alto))
# Titulo de la pantalla
pygame.display.set_caption("Juego de ladrillos")
# Crear reloj para controlar la velocidad de actualización
reloj = pygame.time.Clock()
# Ajustar repetición de teclas
pygame.key.set_repeat(30)

bolita = Bolita()
jugador = Paleta()
muro = Muro(48)
puntuacion = 0 # Puntuación inicial
vidas = 3 # Vidas iniciales
esperando_saque = True

while True:
    # Establecer la velocidad de actualización fps
    reloj.tick(60)

    # Revisar todos los eventos.
    for evento in pygame.event.get():
        # Si se presiona una tecla cerrar el juego
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()
        # Buscar eventos de teclado
        elif evento.type == pygame.KEYDOWN:
            jugador.update(evento)
            if esperando_saque == True and evento.key == pygame.K_SPACE:
                # Iniciar el juego al presionar la barra espaciadora
                esperando_saque = False
                if bolita.rect.centerx < ancho / 2:
                    bolita.speed = [3, 3]  # Velocidad hacia la derecha
                else:
                    bolita.speed = [-3, 3]
              
    # Actualizar posicion de la bolita
    if esperando_saque == False:
        bolita.update()
    else:   
        bolita.rect.midbottom = jugador.rect.midtop
    
    # Colisionar la bolita con la paleta
    if pygame.sprite.collide_rect(bolita, jugador):
        # Invertir la velocidad de la bolita al colisionar con la paleta
        bolita.speed[1] = -bolita.speed[1]
        # Ajustar la posición de la bolita para que no se quede pegada a la paleta
        bolita.rect.bottom = jugador.rect.top
    # Colisionar la bolita con los ladrillos
    lista = pygame.sprite.spritecollide(bolita, muro, False)
    if lista:
        ladrillo = lista[0]
        cx = bolita.rect.centerx
        if cx < ladrillo.rect.left or cx > ladrillo.rect.right:
            # Si la bolita colisiona con los lados del ladrillo
            bolita.speed[0] = -bolita.speed[0]
        else:
            # Si la bolita colisiona con la parte superior o inferior del ladrillo
            bolita.speed[1] = -bolita.speed[1]
        muro.remove(ladrillo)
        puntuacion += 10

    # Revisar si la bolita sale de la pantalla
    if bolita.rect.top > alto:
        vidas -= 1  # Restar una vida
        esperando_saque = True
            
    # Rellenar la pantalla con un color azul oscuro
    pantalla.fill(color_azul)
    # Mostrar la puntuación en la pantalla
    mostrar_puntuacion()
    # Mostrar las vidas en la pantalla
    mostrar_vidas()
    # Dibujar la bolita en la pantalla
    pantalla.blit(bolita.image, bolita.rect)
    # Dibujar la paleta en la pantalla
    pantalla.blit(jugador.image, jugador.rect)
    # Dibujar el muro de ladrillos en la pantalla
    muro.draw(pantalla)

    # Rellenar la pantalla con un color
    pygame.display.flip()

    if vidas <= 0:
        juego_terminado()

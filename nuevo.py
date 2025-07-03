import sys
import time
import pygame

ANCHO = 640
ALTO = 480
color_azul = (0, 0, 64)
color_blanco = (255, 255, 255)

class Escena:
    def __init__(self):
        self.proximaEscena = False
        self.jugando = True

    def leer_eventos(self, eventos):
        pass

    def actualizar(self):
        pass

    def dibujar(self, pantalla):
        pass

    def cambiar_escena(self, escena):
        self.proximaEscena = escena

class Director:
    def __init__(self, titulo = "", res = (ANCHO, ALTO)):
        pygame.init()
        self.pantalla = pygame.display.set_mode(res)
        pygame.display.set_caption(titulo)
        self.reloj = pygame.time.Clock()
        self.escena = None
        self.escenas = {}

    def ejecutar(self, escena_inicial, fps = 60):
        self.escena = self.escenas[escena_inicial]
        jugando = True
        while jugando:
            self.reloj.tick(fps)
            eventos = pygame.event.get()
            for evento in eventos:
                if evento.type == pygame.QUIT:
                    jugando = False

            self.escena.leer_eventos(eventos)
            self.escena.actualizar()
            self.escena.dibujar(self.pantalla)

            self.elegirEscena(self.escena.proximaEscena)

            if jugando:
                jugando = self.escena.jugando

            pygame.display.flip()

        time.sleep(3)

    def elegirEscena(self, proximaEscena):
        if proximaEscena:
            if proximaEscena not in self.escenas:
                self.agregarEscena(proximaEscena)
            self.escena = self.escenas[proximaEscena]

    def agregarEscena(self, escena):
        escenaClase = 'Escena' + escena
        escenaObj = globals()[escenaClase]
        self.escenas[escena] = escenaObj()

# ---------------- ESCENAS ----------------

class EscenaInicio(Escena):
    def __init__(self):
        super().__init__()

    def leer_eventos(self, eventos):
        for evento in eventos:
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_RETURN:
                self.cambiar_escena('Nivel1')

    def actualizar(self):
        pass

    def dibujar(self, pantalla):
        pantalla.fill(color_azul)
        fuente_titulo = pygame.font.SysFont('Arial', 60)
        fuente_indicacion = pygame.font.SysFont('Consolas', 30)

        texto_titulo = fuente_titulo.render('ROMPE MUROS', True, color_blanco)
        texto_pulsa = fuente_indicacion.render('Pulsa ENTER para comenzar', True, color_blanco)

        rect_titulo = texto_titulo.get_rect(center=(ANCHO // 2, ALTO // 2 - 50))
        rect_pulsa = texto_pulsa.get_rect(center=(ANCHO // 2, ALTO // 2 + 30))

        pantalla.blit(texto_titulo, rect_titulo)
        pantalla.blit(texto_pulsa, rect_pulsa)

class EscenaNivel1(Escena):
    def __init__(self):
        super().__init__()
        self.bolita = Bolita()
        self.jugador = Paleta()
        self.muro = Muro(50)
        self.puntuacion = 0
        self.vidas = 3
        self.esperando_saque = True
        pygame.key.set_repeat(30)

    def leer_eventos(self, eventos):
        for evento in eventos:
            if evento.type == pygame.KEYDOWN:
                self.jugador.update(evento)
                if self.esperando_saque and evento.key == pygame.K_SPACE:
                    self.esperando_saque = False
                    if self.bolita.rect.centerx < ANCHO / 2:
                        self.bolita.speed = [3, -3]
                    else:
                        self.bolita.speed = [-3, -3]

    def actualizar(self):
        if not self.esperando_saque:
            self.bolita.update()
        else:
            self.bolita.rect.midbottom = self.jugador.rect.midtop

        if pygame.sprite.collide_rect(self.bolita, self.jugador):
            self.bolita.speed[1] = -self.bolita.speed[1]

        lista = pygame.sprite.spritecollide(self.bolita, self.muro, False)
        if lista:
            ladrillo = lista[0]
            cx = self.bolita.rect.centerx
            if cx < ladrillo.rect.left or cx > ladrillo.rect.right:
                self.bolita.speed[0] = -self.bolita.speed[0]
            else:
                self.bolita.speed[1] = -self.bolita.speed[1]
            self.muro.remove(ladrillo)
            self.puntuacion += 10

        if self.bolita.rect.top > ALTO:
            self.vidas -= 1
            self.esperando_saque = True

        if self.vidas <= 0:
            self.cambiar_escena('JuegoTerminado')

    def dibujar(self, pantalla):
        pantalla.fill(color_azul)
        self.mostrar_puntuacion(pantalla)
        self.mostrar_vidas(pantalla)
        pantalla.blit(self.bolita.image, self.bolita.rect)
        pantalla.blit(self.jugador.image, self.jugador.rect)
        self.muro.draw(pantalla)

    def mostrar_puntuacion(self, pantalla):
        fuente = pygame.font.SysFont('Consolas', 20)
        texto = fuente.render(str(self.puntuacion).zfill(5), True, color_blanco)
        pantalla.blit(texto, (0, 0))

    def mostrar_vidas(self, pantalla):
        fuente = pygame.font.SysFont('Consolas', 20)
        texto = fuente.render("Vidas: " + str(self.vidas).zfill(2), True, color_blanco)
        texto_rect = texto.get_rect()
        texto_rect.topright = [ANCHO, 0]
        pantalla.blit(texto, texto_rect)

class EscenaJuegoTerminado(Escena):
    def actualizar(self):
        self.jugando = False

    def dibujar(self, pantalla):
        pantalla.fill(color_azul)
        fuente = pygame.font.SysFont('Arial', 72)
        texto = fuente.render('Juego terminado :(', True, color_blanco)
        rect = texto.get_rect(center=(ANCHO // 2, ALTO // 2))
        pantalla.blit(texto, rect)

# ---------------- SPRITES ----------------

class Bolita(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('imagenes/bolita.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = ANCHO / 2
        self.rect.centery = ALTO / 2
        self.speed = [3, 3]

    def update(self):
        if self.rect.top <= 0:
            self.speed[1] = -self.speed[1]
        elif self.rect.right >= ANCHO or self.rect.left <= 0:
            self.speed[0] = -self.speed[0]
        self.rect.move_ip(self.speed)

class Paleta(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('imagenes/paleta.png')
        self.rect = self.image.get_rect()
        self.rect.midbottom = (ANCHO / 2, ALTO - 20)
        self.speed = [0, 0]

    def update(self, evento):
        if evento.key == pygame.K_LEFT and self.rect.left > 0:
            self.speed = [-5, 0]
        elif evento.key == pygame.K_RIGHT and self.rect.right < ANCHO:
            self.speed = [5, 0]
        else:
            self.speed = [0, 0]
        self.rect.move_ip(self.speed)

class Ladrillo(pygame.sprite.Sprite):
    def __init__(self, posicion):
        super().__init__()
        self.image = pygame.image.load('imagenes/ladrillo.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = posicion

class Muro(pygame.sprite.Group):
    def __init__(self, cantidadLadrillos):
        super().__init__()
        pos_x = 0
        pos_y = 20
        for i in range(cantidadLadrillos):
            ladrillo = Ladrillo((pos_x, pos_y))
            self.add(ladrillo)
            pos_x += ladrillo.rect.width
            if pos_x >= ANCHO:
                pos_x = 0
                pos_y += ladrillo.rect.height

# ---------------- INICIO DEL JUEGO ----------------

director = Director('Juego de ladrillos', (ANCHO, ALTO))
director.agregarEscena('Inicio')
director.agregarEscena('Nivel1')
director.agregarEscena('JuegoTerminado')
director.ejecutar('Inicio')

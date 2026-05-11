"""
Mario Bros 1 - Versión simplificada en Pygame
Un juego de plataformas inspirado en el clásico Mario Bros
"""

import pygame
import random
from enum import Enum

# Inicializar Pygame
pygame.init()

# Constantes
ANCHO = 800
ALTO = 600
FPS = 60
GRAVEDAD = 0.6
VELOCIDAD_SALTO = 15

# Colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
AMARILLO = (255, 255, 0)
MARRÓN = (139, 69, 19)
NARANJA = (255, 165, 0)
CIELO = (135, 206, 235)

class EstadoJuego(Enum):
    JUGANDO = 1
    GANADO = 2
    PERDIDO = 3

class Jugador(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.ancho = 30
        self.alto = 40
        self.image = pygame.Surface((self.ancho, self.alto))
        self.image.fill(ROJO)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        self.vel_x = 0
        self.vel_y = 0
        self.en_aire = True
        self.direccion = 1  # 1 = derecha, -1 = izquierda
        self.vidas = 3
        self.monedas = 0
        
    def manejar_entrada(self, teclas):
        """Controla el movimiento del jugador."""
        self.vel_x = 0
        
        if teclas[pygame.K_LEFT] or teclas[pygame.K_a]:
            self.vel_x = -5
            self.direccion = -1
        if teclas[pygame.K_RIGHT] or teclas[pygame.K_d]:
            self.vel_x = 5
            self.direccion = 1
        
        if teclas[pygame.K_SPACE] and not self.en_aire:
            self.vel_y = -VELOCIDAD_SALTO
            self.en_aire = True
    
    def aplicar_gravedad(self):
        """Aplica la gravedad al jugador."""
        self.vel_y += GRAVEDAD
        if self.vel_y > 20:
            self.vel_y = 20
    
    def actualizar(self, plataformas, enemigos, monedas):
        """Actualiza la posición del jugador."""
        self.aplicar_gravedad()
        
        # Movimiento horizontal
        self.rect.x += self.vel_x
        
        # Colisión horizontal con plataformas
        for plataforma in plataformas:
            if self.rect.colliderect(plataforma.rect):
                if self.vel_x > 0:  # Moviéndose a la derecha
                    self.rect.right = plataforma.rect.left
                elif self.vel_x < 0:  # Moviéndose a la izquierda
                    self.rect.left = plataforma.rect.right
        
        # Mantener en los límites horizontales
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > ANCHO:
            self.rect.right = ANCHO
        
        # Movimiento vertical
        self.rect.y += self.vel_y
        self.en_aire = True
        
        # Colisión vertical con plataformas
        for plataforma in plataformas:
            if self.rect.colliderect(plataforma.rect):
                if self.vel_y > 0:  # Cayendo
                    self.rect.bottom = plataforma.rect.top
                    self.vel_y = 0
                    self.en_aire = False
                elif self.vel_y < 0:  # Saltando hacia arriba
                    self.rect.top = plataforma.rect.bottom
                    self.vel_y = 0
        
        # Caer del mapa = perder vida
        if self.rect.top > ALTO:
            self.vidas -= 1
            self.rect.x = 50
            self.rect.y = ALTO - 100
            self.vel_y = 0
            self.vel_x = 0
        
        # Colisión con enemigos
        for enemigo in enemigos:
            if self.rect.colliderect(enemigo.rect):
                if self.vel_y > 0 and self.rect.bottom - enemigo.rect.top < 20:
                    # Saltar sobre el enemigo
                    enemigo.matar()
                    self.vel_y = -VELOCIDAD_SALTO
                    self.en_aire = True
                else:
                    # Colisión normal
                    self.vidas -= 1
                    self.rect.x = 50
                    self.rect.y = ALTO - 100
                    self.vel_y = 0
                    self.vel_x = 0
        
        # Colisión con monedas
        for moneda in monedas[:]:
            if self.rect.colliderect(moneda.rect):
                self.monedas += 1
                moneda.kill()
    
    def dibujar(self, pantalla):
        """Dibuja el jugador."""
        # Cuerpo (cuadrado rojo)
        pygame.draw.rect(pantalla, ROJO, self.rect)
        
        # Ojos
        ojo_x = self.rect.centerx + (5 if self.direccion == 1 else -5)
        pygame.draw.circle(pantalla, BLANCO, (ojo_x, self.rect.top + 10), 3)
        pygame.draw.circle(pantalla, NEGRO, (ojo_x, self.rect.top + 10), 1)


class Plataforma(pygame.sprite.Sprite):
    def __init__(self, x, y, ancho, alto, tipo="normal"):
        super().__init__()
        self.ancho = ancho
        self.alto = alto
        self.tipo = tipo
        self.image = pygame.Surface((ancho, alto))
        
        if tipo == "normal":
            self.image.fill(MARRÓN)
        elif tipo == "especial":
            self.image.fill(VERDE)
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def dibujar(self, pantalla):
        """Dibuja la plataforma."""
        if self.tipo == "normal":
            pygame.draw.rect(pantalla, MARRÓN, self.rect)
            # Efecto 3D
            pygame.draw.line(pantalla, (184, 92, 25), self.rect.topleft, self.rect.topright, 2)
        elif self.tipo == "especial":
            pygame.draw.rect(pantalla, VERDE, self.rect)


class Moneda(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.ancho = 15
        self.alto = 15
        self.image = pygame.Surface((self.ancho, self.alto))
        self.image.fill(AMARILLO)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.contador_animacion = 0
    
    def actualizar(self):
        """Actualiza la animación de la moneda."""
        self.contador_animacion += 1
    
    def dibujar(self, pantalla):
        """Dibuja la moneda."""
        pygame.draw.circle(pantalla, AMARILLO, self.rect.center, 7)
        pygame.draw.circle(pantalla, NARANJA, self.rect.center, 5)


class Enemigo(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.ancho = 25
        self.alto = 25
        self.image = pygame.Surface((self.ancho, self.alto))
        self.image.fill(AZUL)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        self.vel_x = random.choice([-2, 2])
        self.vivo = True
    
    def actualizar(self, plataformas):
        """Actualiza la posición del enemigo."""
        if not self.vivo:
            return
        
        self.rect.x += self.vel_x
        
        # Rebotar en los límites
        if self.rect.left < 0 or self.rect.right > ANCHO:
            self.vel_x *= -1
        
        # Gravedad simple
        self.rect.y += 2
        
        # Colisión con plataformas
        for plataforma in plataformas:
            if self.rect.colliderect(plataforma.rect):
                self.rect.bottom = plataforma.rect.top
    
    def matar(self):
        """Mata al enemigo."""
        self.vivo = False
    
    def dibujar(self, pantalla):
        """Dibuja el enemigo."""
        if self.vivo:
            pygame.draw.rect(pantalla, AZUL, self.rect)
            # Ojos
            pygame.draw.circle(pantalla, BLANCO, (self.rect.left + 6, self.rect.top + 6), 2)
            pygame.draw.circle(pantalla, BLANCO, (self.rect.right - 6, self.rect.top + 6), 2)
            pygame.draw.circle(pantalla, NEGRO, (self.rect.left + 6, self.rect.top + 6), 1)
            pygame.draw.circle(pantalla, NEGRO, (self.rect.right - 6, self.rect.top + 6), 1)


class Mario:
    def __init__(self):
        self.pantalla = pygame.display.set_mode((ANCHO, ALTO))
        pygame.display.set_caption("Mario Bros 1 - Python")
        self.reloj = pygame.time.Clock()
        self.fuente_grande = pygame.font.Font(None, 48)
        self.fuente_pequeña = pygame.font.Font(None, 32)
        
        self.crear_nivel()
    
    def crear_nivel(self):
        """Crea el nivel del juego."""
        self.jugador = Jugador(50, ALTO - 100)
        self.plataformas = pygame.sprite.Group()
        self.enemigos = pygame.sprite.Group()
        self.monedas = pygame.sprite.Group()
        
        self.estado = EstadoJuego.JUGANDO
        self.contador = 0
        
        # Plataforma base
        self.plataformas.add(Plataforma(0, ALTO - 40, ANCHO, 40, "normal"))
        
        # Plataformas en escalera
        self.plataformas.add(Plataforma(100, ALTO - 150, 150, 20, "normal"))
        self.plataformas.add(Plataforma(350, ALTO - 200, 150, 20, "normal"))
        self.plataformas.add(Plataforma(600, ALTO - 150, 150, 20, "normal"))
        
        # Plataformas superiores
        self.plataformas.add(Plataforma(50, ALTO - 300, 200, 20, "normal"))
        self.plataformas.add(Plataforma(550, ALTO - 300, 200, 20, "normal"))
        
        # Plataforma final
        self.plataformas.add(Plataforma(300, ALTO - 400, 200, 20, "especial"))
        
        # Crear monedas
        posiciones_monedas = [
            (150, ALTO - 180), (250, ALTO - 180),
            (420, ALTO - 230), (520, ALTO - 230),
            (700, ALTO - 180),
            (150, ALTO - 330), (400, ALTO - 330), (750, ALTO - 330),
            (400, ALTO - 430)
        ]
        
        for pos in posiciones_monedas:
            self.monedas.add(Moneda(pos[0], pos[1]))
        
        # Crear enemigos
        self.enemigos.add(Enemigo(250, ALTO - 180))
        self.enemigos.add(Enemigo(600, ALTO - 180))
        self.enemigos.add(Enemigo(400, ALTO - 330))
    
    def manejar_eventos(self):
        """Maneja los eventos del juego."""
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    return False
        return True
    
    def actualizar(self):
        """Actualiza la lógica del juego."""
        if self.estado == EstadoJuego.JUGANDO:
            teclas = pygame.key.get_pressed()
            self.jugador.manejar_entrada(teclas)
            self.jugador.actualizar(self.plataformas.sprites(), 
                                   [e for e in self.enemigos if e.vivo], 
                                   self.monedas.sprites())
            
            # Actualizar enemigos
            for enemigo in self.enemigos:
                enemigo.actualizar(self.plataformas.sprites())
            
            # Actualizar monedas
            for moneda in self.monedas:
                moneda.actualizar()
            
            # Verificar victoria
            if self.jugador.rect.y < 150 and len(self.monedas) == 0:
                self.estado = EstadoJuego.GANADO
            
            # Verificar derrota
            if self.jugador.vidas <= 0:
                self.estado = EstadoJuego.PERDIDO
        
        self.contador += 1
    
    def dibujar(self):
        """Dibuja todos los elementos del juego."""
        self.pantalla.fill(CIELO)
        
        # Dibujar plataformas
        for plataforma in self.plataformas:
            plataforma.dibujar(self.pantalla)
        
        # Dibujar monedas
        for moneda in self.monedas:
            moneda.dibujar(self.pantalla)
        
        # Dibujar enemigos
        for enemigo in self.enemigos:
            enemigo.dibujar(self.pantalla)
        
        # Dibujar jugador
        self.jugador.dibujar(self.pantalla)
        
        # Dibujar HUD
        self.dibujar_hud()
        
        # Dibujar mensaje de fin de juego
        if self.estado == EstadoJuego.GANADO:
            self.dibujar_victoria()
        elif self.estado == EstadoJuego.PERDIDO:
            self.dibujar_derrota()
        
        pygame.display.flip()
    
    def dibujar_hud(self):
        """Dibuja la interfaz de usuario."""
        # Vidas
        texto_vidas = self.fuente_pequeña.render(f"Vidas: {self.jugador.vidas}", True, NEGRO)
        self.pantalla.blit(texto_vidas, (10, 10))
        
        # Monedas
        texto_monedas = self.fuente_pequeña.render(f"Monedas: {self.jugador.monedas}", True, AMARILLO)
        self.pantalla.blit(texto_monedas, (ANCHO - 200, 10))
    
    def dibujar_victoria(self):
        """Dibuja el mensaje de victoria."""
        overlay = pygame.Surface((ANCHO, ALTO))
        overlay.set_alpha(200)
        overlay.fill(NEGRO)
        self.pantalla.blit(overlay, (0, 0))
        
        texto_victoria = self.fuente_grande.render("¡GANASTE!", True, AMARILLO)
        rect = texto_victoria.get_rect(center=(ANCHO // 2, ALTO // 2))
        self.pantalla.blit(texto_victoria, rect)
        
        texto_reinicio = self.fuente_pequeña.render("Presiona ESC para salir", True, BLANCO)
        rect2 = texto_reinicio.get_rect(center=(ANCHO // 2, ALTO // 2 + 60))
        self.pantalla.blit(texto_reinicio, rect2)
    
    def dibujar_derrota(self):
        """Dibuja el mensaje de derrota."""
        overlay = pygame.Surface((ANCHO, ALTO))
        overlay.set_alpha(200)
        overlay.fill(NEGRO)
        self.pantalla.blit(overlay, (0, 0))
        
        texto_derrota = self.fuente_grande.render("GAME OVER", True, ROJO)
        rect = texto_derrota.get_rect(center=(ANCHO // 2, ALTO // 2))
        self.pantalla.blit(texto_derrota, rect)
        
        texto_reinicio = self.fuente_pequeña.render("Presiona ESC para salir", True, BLANCO)
        rect2 = texto_reinicio.get_rect(center=(ANCHO // 2, ALTO // 2 + 60))
        self.pantalla.blit(texto_reinicio, rect2)
    
    def ejecutar(self):
        """Bucle principal del juego."""
        corriendo = True
        
        print("=" * 50)
        print("🍄 MARIO BROS 1 - PYTHON")
        print("=" * 50)
        print("\n⌨️  CONTROLES:")
        print("  → A o FLECHA IZQUIERDA: Mover izquierda")
        print("  → D o FLECHA DERECHA: Mover derecha")
        print("  → ESPACIO: Saltar")
        print("  → ESC: Salir")
        print("\n🎯 OBJETIVO:")
        print("  ✓ Recolecta todas las monedas")
        print("  ✓ Evita los enemigos azules")
        print("  ✓ ¡Salta sobre ellos para vencerlos!")
        print("\n¡A JUGAR!\n")
        
        while corriendo:
            corriendo = self.manejar_eventos()
            self.actualizar()
            self.dibujar()
            self.reloj.tick(FPS)
        
        pygame.quit()
        print("👋 ¡Gracias por jugar Mario Bros!")


if __name__ == "__main__":
    juego = Mario()
    juego.ejecutar()

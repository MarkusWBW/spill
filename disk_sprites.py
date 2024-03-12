import pygame as pg
import random 
from disk_settings import *
from math import sqrt
    
    
# Lager en klasse for gjeteren
class Frisbee:
    def __init__(self):
        self.x = WIDTH//2
        self.y = HEIGHT - 30
        self.image = pg.Surface((PLAYER_WIDTH, PLAYER_HEIGHT))
        self.image.fill(RED)
        # Lager en firkant for overflaten (Tegner firkanten) 
        self.rect = self.image.get_rect()
        self.rect.center = (self.x - PLAYER_WIDTH//2, self.y - PLAYER_HEIGHT//2)
                
        self.vx = 0
        self.vy = 0
        self.r = 20
        
        self.pos = list(self.rect.center)
        
        self.throws = 0 
        self.stop = False 

    
    # Oppdaterer klassen
    def update(self):
        # Sjekker kollisjon med høyre side
        if self.x - self.r >= WIDTH:
            # Endrer retning på hastigheten
            self.vx *= -1
            self.x = WIDTH - self.r
        
        # Sjekker kollisjon med venstre side
        elif self.x <= -self.r:
            self.vx *= -1
            self.x = 0
        
        # Sjekker kollisjon med bunn
        elif self.y - self.r >= HEIGHT:
            self.vy *= -1
            self.y = HEIGHT - self.r
        
        # Sjekker kollisjon med topp
        elif self.y <= -self.r:
            self.vy *= -1
            self.y = 0
        
    # Metode som håndterer input
    def move(self, delta):
        
        # Sjekker om du kan kaste frisbeen
        can_throw = self.vx == 0 and self.vy == 0
        if can_throw and pg.mouse.get_pressed()[0]:
            
            mouse_pos = pg.mouse.get_pos()
            # Finner musen sin x og y koordinat 
            mx, my = mouse_pos
            
            # Kaster frisbeen i musen sin retning
            self.vx = mx - self.x
            self.vy = my - self.y
            
            # Legger til et kast
            self.throws += 1
            print(self.throws)
            
            # Setter magnetude 
            mag = sqrt(self.vx ** 2 + self.vy ** 2)
            
            # Normaliserer vektoren og setter fart 
            self.vx = self.vx / mag * SPEED
            self.vy = self.vy / mag * SPEED
        
        # Gir en akselerasjon til frisbeen 
        self.vx *= 1 - (0.95 * delta)
        self.vy *= 1 - (0.95 * delta)
        
        # Endrer posisjonen til rektangelet
        self.x += self.vx * delta
        self.y += self.vy * delta
        
        
        self.rect.center = (
            self.x - PLAYER_WIDTH//2,
            self.y - PLAYER_HEIGHT//2
        )
        self.pos = list(self.rect.center)
        
        # Fikser slik at frisbeen stopper hvis den ikke treffer et hinder
        if self.vx < 0:
            if self.vy < 0: 
                if self.vx > -1 or self.vy > -1:
                    self.vx = 0
                    self.vy = 0
                
            elif self.vy > 0:
                if self.vx > -1 or self.vy < 1:
                    self.vx = 0
                    self.vy = 0
                    
        elif self.vx > 0:
            if self.vy > 0:
                if self.vx < 1 or self.vy < 1:
                    self.vx = 0
                    self.vy = 0

            elif self.vy < 0:
                if self.vx < 1 or self.vy > -1:
                    self.vx = 0
                    self.vy = 0
            
            
    # Funksjon som viser antall poeng
    def displayThrows(self):
        # Henter font
        font = pg.font.SysFont('Arial', 26)
        
        text_img = font.render(f"Antall kast: {self.throws}", True, WHITE)
        surface.blit(text_img, (20, 10))
        
# Lager en klasse for hindrene 
class Tree:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y


        self.w = w
        self.h = h
        
        self.image = pg.Surface((self.w, self.h))
        self.image.fill(DARKGREEN)
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        
        
# Lager en vei for frisbeen
class Path:
    def __init__(self):
        self.w = random.randint(50, 80)
        self.h = HEIGHT
        self.x = random.randint(100, WIDTH-100 - self.w)
        self.y = 10
        
        self.image = pg.Surface((self.w, self.h))
        self.image.fill(WHITE)
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        
        
class Basket:
    def __init__(self):
        self.x = WIDTH//2 
        self.y = 50
        self.r = 35
        
        self.image = pg.Surface((self.r, self.r))
        self.image.fill(RED)
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        
        self.hole = 1
        
        
    # Funksjon som viser hvilket hull
    def displayHole(self):
        # Henter font
        font = pg.font.SysFont('Arial', 26)
        
        text_img = font.render(f"Hull nummer: {self.hole}", True, WHITE)
        surface.blit(text_img, (WIDTH - 160, 10))

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

        
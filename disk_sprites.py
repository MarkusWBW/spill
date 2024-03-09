import pygame as pg
import random 
from disk_settings import *
    
    
# Lager en klasse for gjeteren
class Frisbee:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pg.Surface((PLAYER_WIDTH, PLAYER_HEIGHT))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (
            self.x - PLAYER_WIDTH//2,
            self.y - PLAYER_HEIGHT//2
            )
                
        self.vx = 0
        self.vy = 0
        self.r = 20
        
        self.pos = list(self.rect.center)
        self.vel = [0, 0]
        self.acc = [0, 0]
        
        self.throws = 0 
        self.stop = False 

    
    # Oppdaterer klassen
    def update(self):
        # Endrer posisjonen til rektangelet
        self.x += self.vx
        self.y += self.vy
        
        # Sjekker kollisjon med høyre side
        if self.x + self.r >= WIDTH:
            # Endrer retning på hastigheten
            self.vx *= -1
            self.x = WIDTH - self.r
        
        # Sjekker kollisjon med venstre side
        elif self.x <= 0:
            self.vx *= -1
            self.x = 0
        
        # Sjekker kollisjon med bunn
        elif self.y >= HEIGHT - self.r:
            self.vy *= -1
            self.y = HEIGHT - self.r
        
        # Sjekker kollisjon med topp
        elif self.y <= 0:
            self.vy *= -1
            self.y = 0
        
    # Metode som håndterer tastaturinput
    def move(self):
        # Nullstiller farten
        self.vy = 0
        self.vx = 0
                
    # Funksjon som viser antall poeng
    def displayPoints(self):
        return 
        
# Lager en klasse for hindrene 
class Tree:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
        """
        self.w = random.randint(10, 60)
        self.h = random.randint(10, 60)
        """
        self.w = 30
        
        self.image = pg.Surface((self.w, self.w))
        self.image.fill(DARKGREEN)
        
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
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

        
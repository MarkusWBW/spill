import pygame as pg
import sys, random
from disk_settings import *
from disk_sprites import * 

# Lager en liste for trærne
tree_list = []
class Game:
    def __init__(self):
        # Initiere pygame
        pg.init()

        # Lager hovedvinduet
        self.screen = pg.display.set_mode(SIZE)

        # Lager en klokke
        self.clock = pg.time.Clock()
        
        # Attributt som styrer om spillet skal kjøres
        self.running = True
        
        
    # Metode for å starte et nytt spill
    def new(self):
        # Lager spiller-objekt
        self.frisbee = Frisbee(WIDTH//2, HEIGHT - 30)
        
        self.basket = Basket()
        
        # Lager plattformer
        while len(tree_list) < 100:
            # Lager nytt tre
            new_tree = Tree(
                random.randint(0, WIDTH),
                random.randint(100, HEIGHT),
            )
            
            safe = True
            
            # Sjekker om det nye treet kolliderer med noen av de gamle
            for t in tree_list:
                """
                if pg.Rect.colliderect(new_tree.rect, t.rect):
                    safe = False
                    break
                """
                if 450 < t.x > 350 and t.y >= HEIGHT - 100:
                    safe = False
                    
                    
            if safe:
                # Legger i lista
                tree_list.append(new_tree)
            else:
                print("Tre kolliderer, prøv på nytt")
                
        
        self.run()


    # Metode som kjører spillet
    def run(self):
        # Game loop
        self.playing = True
        
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
        
        
    # Metode som håndterer hendelser
    def events(self):
        # Går gjennom hendelser (events)
        for event in pg.event.get():
            # Sjekker om vi ønsker å lukke vinduet
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False # Spillet skal avsluttes
                
            if event.type == pg.KEYDOWN:
                return 
    
    # Metode som oppdaterer
    def update(self):
        self.frisbee.update()
        
        # sjekker om den beveger seg
        if self.frisbee.vx > 0 or self.frisbee.vy > 0:
            collide = False
            
            # Sjekker om frisbeen kolliderer med et tre 
            for t in tree_list: 
                if pg.Rect.colliderect(self.frisbee.rect, t.rect):
                    collide = True
                    break
            
                if collide:
                    self.frisbee.pos[1] = t.rect.y - self.frisbee.x
                    self.frisbee.vx = 0
                    self.frisbee.vy = 0 
                
    # Metode som sjekker om frisbeen kræsjer i et tre
    def checkCollision(self):
        return 
            
            
    
    # Metode som tegner ting på skjermen
    def draw(self):
        # Fyller skjermen med en farge
        self.screen.fill(WHITE)
        
        # Tegner trærne
        for t in tree_list:
            self.screen.blit(t.image, (t.rect.x, t.rect.y))
        
        # Tegner spilleren
        self.screen.blit(self.frisbee.image, self.frisbee.pos)
        
        self.screen.blit(self.basket.image, (self.basket.x, self.basket.y))
        
        # "Flipper" displayet for å vise hva vi har tegnet
        pg.display.flip()
    
    
    # Metode som viser start-skjerm
    def show_start_screen(self):
        pass


    
    
# Lager et spill-objekt
game_object = Game()

# Spill-løkken
while game_object.running:
    # Starter et nytt spill
    game_object.new()
    


# Avslutter pygame
pg.quit()
#sys.exit() # Dersom det ikke er tilstrekkelig med pg.quit()

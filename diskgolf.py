import pygame as pg
import sys, random
from disk_settings import *
from disk_sprites import * 

# Lager en liste for trærne
tree_list = []

# Putter skog inn på sidene 
tree_list.append(Tree(0, 0, 100, HEIGHT))
tree_list.append(Tree(WIDTH-100, 0, 100, HEIGHT))


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
        self.frisbee = Frisbee()
        
        self.basket = Basket()
        
        self.path = Path()
        
        # Lager plattformer
        while len(tree_list) < 100:
            # Lager nytt tre
            new_tree = Tree(
                random.randint(80, WIDTH - 80),
                random.randint(100, HEIGHT),
                random.randint(10, 40),
                random.randint(10, 40)
            )
            
            safe = True
            
            # Sjekker om det nye treet er innenfor grensene 
            if new_tree.x > 350 and new_tree.y >= HEIGHT - 100:
                safe = False
            elif new_tree.x < 450 and new_tree.y >= HEIGHT - 100:
                safe = False
            
            # Sjekker om trærne treffer veien
            if pg.Rect.colliderect(self.path.rect, new_tree.rect):
                safe = False
                    
            if safe:
                # Legger i lista
                tree_list.append(new_tree)
                
        
        self.run()


    # Metode som kjører spillet
    def run(self):
        # Game loop
        self.playing = True
        
        while self.playing:
            # Lager en delta som oppdaterer spillet etter tid 
            delta = self.clock.tick(FPS) / 1000
            self.events()
            self.update(delta)
            self.checkCollision()
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
                
    
    # Metode som oppdaterer
    def update(self, delta):          
        self.frisbee.move(delta)
        
        self.frisbee.update()
            
    # Metode som sjekker om frisbeen kræsjer i et tre
    def checkCollision(self):
        collide = False
        
        # Sjekker om frisbeen treffer kurven
        if pg.Rect.colliderect(self.frisbee.rect, self.basket.rect):
            collide = True
            self.basket.hole += 1
            print("Ferdig med hull 1")
            
            
        # Sjekker om frisbeen kolliderer med et tre 
        for t in tree_list: 
            if pg.Rect.colliderect(self.frisbee.rect, t.rect):
                collide = True
                break
            
        if collide:
            self.frisbee.vx = 0
            self.frisbee.vy = 0
                
            
    
    # Metode som tegner ting på skjermen
    def draw(self):
        
        # Fyller skjermen med en farge
        self.screen.blit(grass_img, (0,0))
        
        # Tegner trærne
        for t in tree_list:
            self.screen.blit(t.image, (t.rect.x, t.rect.y))
                
        # Tegner spilleren
        self.screen.blit(self.frisbee.image, self.frisbee.pos)
        
        self.screen.blit(self.basket.image, (self.basket.x, self.basket.y))
        
        self.frisbee.displayThrows()
        self.basket.displayHole()
        
        # "Flipper" displayet for å vise hva vi har tegnet
        pg.display.flip()
    
    def reset(self):
        pass
    
    
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

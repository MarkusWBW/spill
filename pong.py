# Importerer biblioteket
import pygame as pg
import sys, random
import math

# Konstanter
WIDTH = 650  # bredden av vinduet
HEIGHT = 500 # høyden til vinduet

# størrelsen til vinduet
SIZE = (WIDTH, HEIGHT)

FPS = 60 # frames per second (bilder per sekund)

# Farger (RGB)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Initiere pygame
pg.init()

# Lager en overflate (surface) vi kan tegne på
surface = pg.display.set_mode(SIZE)

# Henter font
font = pg.font.SysFont("Arial", 28)

# Lager en klokke 
clock = pg.time.Clock()

running = True

# Funksjon som tegner score til skjermen
def drawScore():
    scoreLeftImg = font.render(f"Score: {player1.score}", True, BLACK)
    surface.blit(scoreLeftImg, (20,20))
    
    scoreRightImg = font.render(f"Score: {player2.score}", True, BLACK)
    # Henter rektangelet fra tekstbildet
    scoreRightRect = scoreRightImg.get_rect()
    surface.blit(scoreRightImg, (WIDTH - scoreRightRect.width -20,20))


# Funksjon som skriver tekst til vinduet
def drawText(text, x, y, color, fontSize):
    # Henter font
    font = pg.font.SysFont("Arial", fontSize)
    
    # Lager et tekstbilde
    textImg = font.render(text, True, color)
    
    # Henter rektangelet til tekstboksen
    textRect = textImg.get_rect()
    
    # Putter i vinduet
    surface.blit(textImg, (x - textRect.width//2, y - textRect.height//2))

# Klasse for rektangler
class Rektangel:
    # Konstruktør
    def __init__(self, x, y, w, h, color):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color
        
        # Hastighet/fart
        self.speed = 5
        self.vx = 0
        self.vy = 0
        
        # Score
        self.score = 0
        
    # Metode som tegner figuren
    def draw(self):
        rect = pg.Rect(self.x, self.y, self.w, self.h)
        pg.draw.rect(surface, self.color, rect)
        
    # Metode som oppdaterer posisjonen til figuren
    def update(self):
        # Endrer posisjonen til rektangelet
        self.x += self.vx
        self.y += self.vy
        
        # Sjekker kollisjon med høyre side
        if self.x + self.w + 50 >= WIDTH:
            # Endrer retning på hastigheten
            self.vx *= -1
            self.x = WIDTH - self.w - 50
        
        # Sjekker kollisjon med venstre side
        if self.x - 50 <= 0:
            self.vx *= -1
            self.x = 50 

        # Sjekker kollisjon med toppen 
        if self.y - 50 <= 0:
            self.vy *= -1
            self.y = 0 + 50
            
        # Sjekker kollisjon med bunnen
        if self.y + self.h + 50 >= HEIGHT:
            self.vy *= -1
            self.y = HEIGHT - self.h - 50

    
# Lager en subklasse som arver fra superklassen
class Paddle(Rektangel):
    def __init__(self, x, y, w, h, color):
        super().__init__(x, y, w, h, color)

    # Metode som håndterer tastaturinput
    def move(self):
        # Nullstiller farten
        self.vy = 0
        self.vx = 0 
        


# Klasse for sirkler
class Circle:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r
        self.color = GREEN
        
        # Oppdaterer posisjonen fra farten
        self.vx = random.randint(-4, 4)
        self.vy = random.randint(-2, 2)
    
    # Tegner ballen 
    def draw(self):
        center = (self.x, self.y)
        pg.draw.circle(surface, self.color, center, self.r)
             
    def update(self):
        # Gir ny posisjon til ballen
        self.x += self.vx
        self.y += self.vy
        
        if self.vx >= 6:
            self.vx = 6
        elif self.vx <= -6:
            self.vx = -6
        elif self.vy >= 6:
            self.vy = 6
        elif self.vy <= -6:
            self.vy = -6
        
    def reset(self):
        self.x = WIDTH//2
        self.y = HEIGHT//2
        self.vx = random.randint(-4,4)
        self.vy = random.randint(-2,2)
        if self.vx == 0:
            self.vx = 0.5
        elif self.vy == 0:
            self.vy = 0.5 
        
        
# Funksjon som sjekker kollisjon mellom ball og padle
def collision(ball, paddle1, paddle2, paddle3, paddle4):
    global gameOver

    # Rød paddle
    # Sjekker om ballen kolliderer med venstre paddle
    if ball.x - ball.r <= paddle1.x + paddle1.w:
        if ball.y + ball.r >= paddle1.y and ball.y - ball.r <= paddle1.y + paddle1.h:
            ball.vx *= -1.5
            ball.vy = math.cos(random.randint(30, 150))
            
    # Sjekker om ballen treffer topp paddle 
    if ball.y - ball.r <= paddle3.y + paddle3.h:
        if ball.x + ball.r >= paddle3.x and ball.x - ball.r <= paddle3.x + paddle3.w:
            ball.vy *= -1.5
            ball.vx = math.cos(random.randint(30,150))
            
            
    # Sjekker om ballen treffer rød side
    if ball.x < 60 or ball.y < 60:
        paddle2.score += 1 # Øker score til høyre spiller
        # Nullstiller ballen
        ball.reset()
            
            
    # Blå paddle
    # Sjekker om ballen treffer høyre paddle
    if ball.x + ball.r >= paddle2.x:
        if ball.y + ball.r >= paddle2.y and ball.y - ball.r <= paddle2.y + paddle2.h:
            ball.vx *= -1.5
            ball.vy = math.cos(random.randint(30,150))
    # Sjekker om ballen treffer bunn paddle 
    elif ball.y + ball.r >= paddle4.y:
        if ball.x + ball.r >= paddle4.x and ball.x - ball.r <= paddle4.x + paddle4.w:
            ball.vy *= -1.5
            ball.vx = math.cos(random.randint(30,150))

    # Sjekker om ballen treffer blå side
    if ball.x > WIDTH - 60 or ball.y > HEIGHT - 60:
        paddle1.score += 1 # Øker score til rød spiller
        # Nullstiller ballen  
        ball.reset()
            
    
    # Sjekker om en spiller har vunnet
    if paddle1.score >= 5:
        gameOver = True
        drawText("Venstre spiller vant", WIDTH//2, HEIGHT//2 - 100, BLACK, 50)
        paddle2.score = 0
        paddle1.score = 0 
        
    elif paddle2.score >= 5:
        gameOver = True
        drawText("Høyre spiller vant", WIDTH//2, HEIGHT//2 - 100, BLACK, 50)
        paddle2.score = 0
        paddle1.score = 0 
        

# Lager objekter
player1 = Paddle(30, HEIGHT//2, 20, 120, RED)
player2 = Paddle(WIDTH - 50, HEIGHT//2, 20, 120, BLUE)
player3 = Paddle(WIDTH//2, 30, 120, 20, RED)
player4 = Paddle(WIDTH//2, HEIGHT - 50, 120, 20, BLUE)
ball = Circle(WIDTH//2, HEIGHT//2, 10)

# Lager en klasse for en knapp 
class Button():
    def __init__(self, color, x, y, w, h, b_text=""):
        self.color = color
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.b_text = b_text
        
    def draw(self, win, outline = None):
        if outline:
            pg.draw.rect(win, outline, (self.x - 2, self.y - 2, self.w + 4, self.h + 4), 0)
            
        pg.draw.rect(win, self.color, (self.x, self.y, self.w, self.h), 0)
        
        if self.b_text != "":
            b_font = pg.font.SysFont('Arial', 60)
            b_text = b_font.render(self.b_text, 1, (0,0,0))
            # Putter knappen i midten
            win.blit(b_text, (self.x + (self.w/2 - b_text.get_width()/2), self.y + (self.h/2 - b_text.get_height()/2)))
            
    def isOver(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.w:
            if pos[1] > self.y and pos[1] < self.y + self.h:
                return True
        return False

button = Button(GREEN, WIDTH/2 - 125, HEIGHT/2 - 50, 250, 100, "SPILL")


# Variabel som styrer om spillet skal kjøres
run = True

# Variabel som styrer om spillet er ferdig
gameOver = True

# Spill-løkken
while run:
    # Løkken kjører i korrekt hastighet
    clock.tick(FPS)
    
    # Fyller skjermen med en farge
    surface.fill(WHITE)
    
    
    if gameOver:
        button.draw(surface, (0,0,0))
    
    # Går gjennom hendelser (events)
    for event in pg.event.get():
        # Sjekket om vi ønsker å lukke vinduet
        if event.type == pg.QUIT:
            run = False # Spillet skal avsluttes
            
        if gameOver:
            # Finner posisjonen til musen 
            pos = pg.mouse.get_pos()
            
            if event.type == pg.MOUSEBUTTONDOWN:
                if button.isOver(pos):
                    print("Du har startet spillet")
                    gameOver = False
                    
            
            if event.type == pg.MOUSEMOTION:
                if button.isOver(pos):
                    button.color = RED
                else:
                    button.color = GREEN 
        
    
    if not gameOver:
        # Rød spiller
        player1.move()
        
        # Henter knappene fra tastaturet som trykkes på
        keys = pg.key.get_pressed()
        
        # Sjekker om tasten "w" er trykket på
        if keys[pg.K_w]:
            player1.vy = -player1.speed
            
        # Sjekker om tasten "s" er trykket på
        if keys[pg.K_s]:
            player1.vy = player1.speed
            
        player1.update()
        player1.draw()
        
        player3.move()
        
        # Sjekker om tasten "a" er trykket på
        if keys[pg.K_a]:
            player3.vx = -player3.speed
            
        # Sjekker om tasten "d" er trykket på
        if keys[pg.K_d]:
            player3.vx = player3.speed
        
        player3.update()
        player3.draw()
        
        
        # Blå spiller
        player2.move()
        
        # Sjekker om piltast oppover er trykket på
        if keys[pg.K_UP]:
            player2.vy = -player2.speed
            
        # Sjekker om piltast nedover er trykket på
        if keys[pg.K_DOWN]:
            player2.vy = player2.speed
            
        player2.update()
        player2.draw()
        
        player4.move()
        
        # Sjekker om piltast venstre er trykket på
        if keys[pg.K_LEFT]:
            player4.vx = -player4.speed
            
        # Sjekker om piltast høyre er trykket på
        if keys[pg.K_RIGHT]:
            player4.vx = player4.speed
        
        player4.update()
        player4.draw()
        
        # Ball
        ball.update()
        ball.draw()
    
        # Tegner score
        drawScore()
        
        
    # Kollisjon med paddles
    collision(ball, player1, player2, player3, player4)
        
    

    # Etter vi har tegner alt, "flipper" vi displayet
    pg.display.flip()


# Avslutter pygame
pg.quit()
sys.exit()




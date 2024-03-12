import pygame as pg
# Konstanter
WIDTH = 800  # Bredden til vinduet
HEIGHT = 600 # Høyden til vinduet

# Størrelsen til vinduet
SIZE = (WIDTH, HEIGHT)

# Frames Per Second (bilder per sekund)
FPS = 60

# Farger (RGB)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
DARKGREEN = (0, 100, 0)
LIGHTBLUE = (100, 100, 255)
GREY = (142, 142, 142)
LIGHTRED = (255, 100, 100)


# Innstillinger til spilleren
PLAYER_WIDTH = 20
PLAYER_HEIGHT = 20
SPEED = 500

# Henter inn bilder til spillet
grass_img = pg.image.load('grass.png')

# Lager en overflate (surface) vi kan tegne på
surface = pg.display.set_mode(SIZE)
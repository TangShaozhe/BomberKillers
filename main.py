import pygame
import random

WIDTH = 1024 # 16 * 64  or 32 * 32
HEIGHT = 768 # 16 * 48 or 32 * 24 or 64 * 12
FPS = 30

# define colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)


# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("BomberKillers")
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    # Process input(events)
    for event in pygame.event.get():
        # check for closing the window
        if event.type == pygame.QUIT:
            running = False
    # Update

    # Draw / render
    screen.fill(BLACK)
    # * after drawing everything , flip the display
    pygame.display.flip()


pygame.quit()
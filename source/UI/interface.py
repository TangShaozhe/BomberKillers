import pygame

pygame.init()
pygame.display.set_caption("Bomberman")
heigh,width = 1280,720
screen = pygame.display.set_mode((heigh,width))
screen_On = True

background = pygame.image.load("./resources/bg.jpg")
while screen_On:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            screen_On = False

    screen.blit(background,(0,0))
    pygame.display.update()


import pygame
from Canard import Canard

pygame.init()

pygame.display.set_caption('Epiduck - Step 2')
fenetre = pygame.display.set_mode((1600, 600))
background = pygame.image.load('assets/backgroundEASY.png')
clock = pygame.time.Clock()

canard = Canard()
pressed = {}

running = True
while running:
    fenetre.blit(background, (0, 0))
    fenetre.blit(canard.image, canard.rect)

    if pressed.get(pygame.K_d):
        canard.deplacement_droite()
    elif pressed.get(pygame.K_q):
        canard.deplacement_gauche()

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            pressed[event.key] = False
            
    clock.tick(60)
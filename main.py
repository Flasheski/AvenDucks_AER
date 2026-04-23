import pygame
from jeu import Jeu

pygame.init()

# fenetre du jeu 
pygame.display.set_caption('Epiduck')
fenetre = pygame.display.set_mode((1600,600))
background = pygame.image.load('assets/backgroundEASY.png')

jeu = Jeu()

running = True

# pour garder la fenetre ouverte
while running:

    fenetre.blit(background, (0,0)) # largeur et hauteur
    
    # verifier colision
    jeu.verifier_collision()

    # On affiche le canard
    fenetre.blit(jeu.canard.image, jeu.canard.rect)
    
    # au départ afficher l'épée que si elle est au sol
    if jeu.epee_au_sol:
        fenetre.blit(jeu.epee.image, jeu.epee.rect)

    # deplacements
    if jeu.pressed.get(pygame.K_d):
        jeu.canard.deplacement_droite()
    elif jeu.pressed.get(pygame.K_q):
        jeu.canard.deplacement_gauche()

    pygame.display.flip() # pour recharger l'écran

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        elif event.type == pygame.KEYDOWN:
            jeu.pressed[event.key]= True
        elif event.type == pygame.KEYUP:
            jeu.pressed[event.key]= False
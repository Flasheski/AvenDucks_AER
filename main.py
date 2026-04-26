import pygame
from jeu import Jeu

pygame.init()
jeu = Jeu()

# fenetre du jeu 
pygame.display.set_caption('Epiduck')
fenetre = pygame.display.set_mode((1600,600))
background = pygame.image.load('assets/backgroundEASY.png')

# pour garder la fenetre ouverte
running = True
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

    # attaque avec e que si il a lépée
    if jeu.pressed.get(pygame.K_e) and jeu.canard.a_une_epee:
        if not jeu.canard.en_attaque:
            jeu.canard.en_attaque = True
            jeu.canard.actualiser_image()
    else:
        if jeu.canard.en_attaque:
            jeu.canard.en_attaque = False
            jeu.canard.actualiser_image()

    pygame.display.flip() # pour recharger l'écran

    # si on quitte pas la fenetre se ferme pas 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        # persistance de la touche en mode tu gardes la touches enfoncé ca avance
        elif event.type == pygame.KEYDOWN:
            jeu.pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            jeu.pressed[event.key] = False
import pygame
from jeu import Jeu

pygame.init()
jeu = Jeu()

# fenetre du jeu 
pygame.display.set_caption('Epiduck')
fenetre = pygame.display.set_mode((1600,600))
background = pygame.image.load('assets/backgroundEASY.png')

# Horloge pour réguler la vitesse du jeu
clock = pygame.time.Clock()

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

    # Gestion du Boss Easy
    if jeu.boss_vivant:
        jeu.boss_easy.deplacer() # Le boss fait ses allers-retours
        fenetre.blit(jeu.boss_easy.image, jeu.boss_easy.rect) # On affiche le boss
        jeu.boss_easy.update_pv(fenetre) # On affiche sa barre de vie

    # Affichage de la pierre si elle est au sol ---
    if jeu.pierre_au_sol:
        # On dessine un cercle bleu/cyan pour représenter la pierre provisoirement
        pygame.draw.circle(fenetre, (0, 255, 255), jeu.pierre_rect.center, 25)

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
            
            # On lance l'attaque sur le boss
            jeu.attaquer_boss() 
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

    # je limite le jeu à 60 FPS
    clock.tick(60)
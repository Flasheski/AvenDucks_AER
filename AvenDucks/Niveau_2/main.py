import pygame
import random
from AvenDucks.Niveau_2.jeu import Jeu

pygame.init()
jeu = Jeu()
pygame.display.set_caption('Epiduck - Niveau 2')
fenetre = pygame.display.set_mode((1600, 600))
background = pygame.image.load('assets/background_game.png')
clock = pygame.time.Clock()

running = True
while running:
    fenetre.blit(background, (0, 0))
    
    # Mécaniques
    jeu.canard.appliquer_gravite()
    jeu.canard.actualiser_projectiles()
    jeu.verifier_collision()

    # Affichage du canard, de ses tirs et de sa barre de vie
    fenetre.blit(jeu.canard.image, jeu.canard.rect)
    jeu.canard.projectiles.draw(fenetre)
    jeu.canard.update_pv(fenetre)

    # Affichage du boss et de ses tirs
    if jeu.boss_vivant:
        jeu.boss.deplacer()
        fenetre.blit(jeu.boss.image, jeu.boss.rect)
        jeu.boss.update_pv(fenetre)
        jeu.boss.projectiles.draw(fenetre)
        
        # Cadence de tir réduite (1 chance sur 60)
        if random.randint(1, 60) == 1:
            jeu.boss.tirer()

    if jeu.pressed.get(pygame.K_d):
        jeu.canard.deplacement_droite()
    elif jeu.pressed.get(pygame.K_q):
        jeu.canard.deplacement_gauche()

    # Fermeture de la fenêtre si fin de partie
    if jeu.victoire:
        print("Fermeture du niveau (Victoire)...")
        running = False 
        
    if jeu.game_over:
        running = False

    pygame.display.flip() 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            jeu.pressed[event.key] = True
            if event.key == pygame.K_SPACE:
                jeu.canard.sauter() # SAUT
            if event.key == pygame.K_e:
                jeu.canard.tirer() # TIR
        elif event.type == pygame.KEYUP:
            jeu.pressed[event.key] = False

    clock.tick(60)
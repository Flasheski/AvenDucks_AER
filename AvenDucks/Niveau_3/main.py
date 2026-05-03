import pygame
import random
from AvenDucks.Niveau_3.jeu import Jeu

pygame.init()
jeu = Jeu()

pygame.display.set_caption('Epiduck - Niveau 3 (FINAL)')
fenetre = pygame.display.set_mode((1600, 600))
background = pygame.image.load('assets/background_game.png')
clock = pygame.time.Clock()

running = True
while running:
    fenetre.blit(background, (0, 0))
    
    # Mécaniques et physique
    jeu.canard.appliquer_gravite()
    jeu.canard.actualiser_projectiles()
    jeu.verifier_collision()

    # Affichage du canard, de ses DEUX types de tirs, et de sa barre de vie
    fenetre.blit(jeu.canard.image, jeu.canard.rect)
    jeu.canard.projectiles.draw(fenetre)
    jeu.canard.projectiles_speciaux.draw(fenetre)
    jeu.canard.update_pv(fenetre)

    # Affichage et gestion du boss final
    if jeu.boss_vivant:
        jeu.boss.deplacer()
        fenetre.blit(jeu.boss.image, jeu.boss.rect)
        jeu.boss.update_pv(fenetre)
        jeu.boss.projectiles.draw(fenetre)
        
        # Le boss tire aléatoirement plus vite qu'au niveau 2 (1 chance sur 30)
        if random.randint(1, 30) == 1:
            jeu.boss.tirer()

    # Déplacements continus
    if jeu.pressed.get(pygame.K_d):
        jeu.canard.deplacement_droite()
    elif jeu.pressed.get(pygame.K_q):
        jeu.canard.deplacement_gauche()

    # Fin de partie
    if jeu.victoire:
        print("Fermeture du jeu (Victoire Ultime)...")
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
            
            # Actions du player
            if event.key == pygame.K_SPACE:
                jeu.canard.sauter() # SAUT
            if event.key == pygame.K_e:
                jeu.canard.tirer() # TIR NORMAL
            if event.key == pygame.K_f:
                jeu.canard.tirer_special() # ATTAQUE SPÉCIALE BAZOOKA
                
        elif event.type == pygame.KEYUP:
            jeu.pressed[event.key] = False

    clock.tick(60)
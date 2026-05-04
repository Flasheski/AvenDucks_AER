import pygame
from AvenDucks.Niveau_1.jeu import Jeu

pygame.init()
jeu = Jeu()

pygame.display.set_caption('Epiduck - Step 4')
fenetre = pygame.display.set_mode((____, ____))
background = pygame.image.load('____________________')
clock = pygame.time.Clock()

running = True
while running:
    fenetre.blit(background, (0, 0))
    
    jeu.verifier_collision()

    fenetre.blit(jeu.canard.image, jeu.canard.rect)

    if jeu.epee_au_sol:
        fenetre.blit(jeu.epee.image, jeu.epee.rect)

    # Gestion du Boss Easy
    if jeu.boss_vivant:
        jeu.boss_easy.deplacer()
        fenetre.blit(jeu.boss_easy.image, jeu.boss_easy.rect)
        jeu.boss_easy.update_pv(fenetre)        
    if jeu.pressed.get(pygame.K_d):
        jeu.canard.deplacement_droite()
    elif jeu.pressed.get(pygame.K_q):
        jeu.canard.deplacement_gauche()  
      
    if jeu.pressed.get(pygame.K_e) and jeu.canard.a_une_epee:
        if not jeu.canard.en_attaque:
            jeu.canard.en_attaque = True
            jeu.canard.actualiser_image()
            
        jeu.verifier_attaque_joueur()
        if not jeu.boss_vivant:
            print("Bravo ! Fermeture du Niveau 1...")
            running = False
    else:
        if jeu.canard.en_attaque:
            jeu.canard.en_attaque = False
            jeu.canard.actualiser_image()
            
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            jeu.pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            jeu.pressed[event.key] = False
            
    clock.tick(60)
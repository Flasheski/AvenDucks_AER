import pygame

pygame.init()

pygame.display.set_caption('Epiduck - Step 1')
fenetre = pygame.display.set_mode((1600, 600))
background = pygame.image.load('assets/background_game.png') # c'est ça qu'il faut mettre en texte à trou

# FPS (frame per second -> ton nombre d'images par seconde (expl pour les petits))
clock = pygame.time.Clock()
running = True

# tout ce qui est ici on s'en fout c'est pour la window -> faire la doc après
while running:
    fenetre.blit(background, (0, 0))

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

    clock.tick(60)
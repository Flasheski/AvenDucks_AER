import pygame

class Epee(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        # 1. D'ABORD on crée la variable (ligne 8)
        epee_original = pygame.image.load('assets/lame.png') 
        
        # 2. ENSUITE on l'utilise pour la redimensionner (ligne 11)
        self.image = pygame.transform.scale(epee_original, (130, 130))
        
        # 3. APRES, on récupère le rectangle (ligne 14)
        self.rect = self.image.get_rect()
        
        # Coordonnées où l'épée sera posée par terre
        self.rect.x = 800
        self.rect.y = 400
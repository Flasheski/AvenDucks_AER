import pygame

class Epee(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        
        epee_original = pygame.image.load('assets/lame.png') 
        
        
        self.image = pygame.transform.scale(epee_original, (110, 110))
        
        
        self.rect = self.image.get_rect()
        
        # Coordonnées où l'épée sera posée par terre
        self.rect.x = 800
        self.rect.y = 450 
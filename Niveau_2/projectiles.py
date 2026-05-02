import pygame

class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y, direction, couleur):
        super().__init__()
        self.velocity = 8
        self.direction = direction # 1 pour la droite (Canard), -1 pour la gauche (Boss)
        
        # rectangle qui fait office de balle quand le boss tire (remplacer par une image / sprite si on en a besoin)
        self.image = pygame.Surface((20, 10))
        self.image.fill(couleur) 
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def deplacer(self):
        self.rect.x += self.velocity * self.direction
import pygame

class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y, direction, couleur, width=20, height=10):
        super().__init__()
        self.velocity = 8
        self.direction = direction # 1 = vers la droite, -1 = vers la gauche
        
        self.image = pygame.Surface((width, height))
        self.image.fill(couleur) 
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def deplacer(self):
        self.rect.x += self.velocity * self.direction
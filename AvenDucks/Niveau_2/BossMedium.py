import pygame
from AvenDucks.Niveau_2.projectiles import Projectile

class BossMedium(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.health = 200
        self.max_health = 200
        self.velocity = 3
        
        # Sprite du cyber-dragon
        self.image_base = pygame.image.load('assets/bossMEDIUM.png')
        self.image = pygame.transform.scale(self.image_base, (250, 250))
        self.rect = self.image.get_rect()
        self.rect.x = 1300
        self.rect.y = 200
        
        self.direction_y = 1 # 1 = descend, -1 = monte
        self.projectiles = pygame.sprite.Group()

    def deplacer(self):
        self.rect.y += self.velocity * self.direction_y
        if self.rect.y <= 50:
            self.direction_y = 1
        elif self.rect.y >= 350:
            self.direction_y = -1
            
        for projectile in self.projectiles:
            projectile.deplacer()
            if projectile.rect.x < 0:
                self.projectiles.remove(projectile)

    def tirer(self):
        tir = Projectile(self.rect.x, self.rect.y + 100, -1, (255, 0, 0))
        self.projectiles.add(tir)

    def update_pv(self, surface):
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x, self.rect.y - 20, self.max_health, 10])
        pygame.draw.rect(surface, (255, 0, 0), [self.rect.x, self.rect.y - 20, max(0, self.health), 10])
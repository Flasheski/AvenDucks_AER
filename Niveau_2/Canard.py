import pygame
from projectiles import Projectile

class Canard(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.velocity = 5 # Il est plus rapide
        
        self.image = pygame.image.load('assets/canardpistolet.png')
        self.image = pygame.transform.scale(self.image, (300, 200))
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 350 # Position au sol
        
        # Variables pour le saut (Step 2)
        self.is_jumping = False
        self.velocity_y = 0
        self.gravity = 1
        
        self.projectiles = pygame.sprite.Group()

    def deplacement_droite(self):
        self.rect.x += self.velocity
    def deplacement_gauche(self):
        self.rect.x -= self.velocity

    def sauter(self):
        if not self.is_jumping:
            self.is_jumping = True
            self.velocity_y = -18 # Force du saut

    def appliquer_gravite(self):
        if self.is_jumping:
            self.rect.y += self.velocity_y
            self.velocity_y += self.gravity
            if self.rect.y >= 350: # S'il retouche le sol
                self.rect.y = 350
                self.is_jumping = False

    def tirer(self):
        # Tire un projectile bleu clair vers la droite
        tir = Projectile(self.rect.x + 200, self.rect.y + 80, 1, (0, 255, 255))
        self.projectiles.add(tir)
        
    def actualiser_projectiles(self):
        for projectile in self.projectiles:
            projectile.deplacer()
            if projectile.rect.x > 1600:
                self.projectiles.remove(projectile)
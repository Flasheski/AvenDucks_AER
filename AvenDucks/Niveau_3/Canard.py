import pygame
from AvenDucks.Niveau_3.projectiles import Projectile

class Canard(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.velocity = 5 
        
        # Sprite du canard bazooka
        self.image = pygame.image.load('assets/canardbazooka.png')
        self.image = pygame.transform.scale(self.image, (300, 200))
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 350 
        
        # Variables de Saut
        self.is_jumping = False
        self.velocity_y = 0
        self.gravity = 1
        
        # Deux types d'attaque
        self.projectiles = pygame.sprite.Group()          # Tirs normaux (Touche E)
        self.projectiles_speciaux = pygame.sprite.Group() # Tirs Bazooka (Touche F)

    def deplacement_droite(self):
        self.rect.x += self.velocity

    def deplacement_gauche(self):
        self.rect.x -= self.velocity

    def sauter(self):
        if not self.is_jumping:
            self.is_jumping = True
            self.velocity_y = -18 

    def appliquer_gravite(self):
        if self.is_jumping:
            self.rect.y += self.velocity_y
            self.velocity_y += self.gravity
            if self.rect.y >= 350:
                self.rect.y = 350
                self.is_jumping = False

    def tirer(self):
        # tir normal
        tir = Projectile(self.rect.x + 200, self.rect.y + 80, 1, (0, 255, 255))
        self.projectiles.add(tir)
        
    def tirer_special(self):
        # missile orange/rouge
        tir_spe = Projectile(self.rect.x + 200, self.rect.y + 50, 1, (255, 100, 0), width=60, height=30)
        self.projectiles_speciaux.add(tir_spe)

    def actualiser_projectiles(self):
        # Actualise les deux groupes de tirs
        for projectile in self.projectiles:
            projectile.deplacer()
            if projectile.rect.x > 1600:
                self.projectiles.remove(projectile)
                
        for projectile in self.projectiles_speciaux:
            projectile.deplacer()
            if projectile.rect.x > 1600:
                self.projectiles_speciaux.remove(projectile)

    def update_pv(self, surface):
        # Barre de vie en haut à gauche
        pygame.draw.rect(surface, (60, 63, 60), [20, 20, self.max_health, 15])
        pygame.draw.rect(surface, (50, 205, 50), [20, 20, max(0, self.health), 15])
import pygame

class BossEasy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.attack = 5
        self.velocity = 2

        # je vais mettre les sprites après
        self.image = pygame.Surface((150,150))
        self.image.fill((255,0,0)) # en gros je mets pour faire office du boss
        self.rect = self.image.get_rect()

        # je le mets à droite de l'écran
        self.rect.x = 1200
        self.rect.y = 450
        self.direction = -1 # je mets -1 pour aller à gauche pour -x et 1 pour aller à droite

    def deplacer(self):
        self.rect.x += self.velocity *self.direction

        # je vais faire en sorte que le boss fasse des aller-retour dans sa zone
        if self.rect.x <= 700:
            self.direction = 1
        elif self.rect.x >= 1300:
            self.direction = -1
        
    def update_pv(self, surface):
        # je viens dessiner la barre de pv au-dessus du boss
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x, self.rect.y - 20, self.max_health, 10])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x, self.rect.y - 20, self.health, 10])
import pygame

class Canard(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.velocity = 5
        self.image = pygame.image.load('assets/canard.png')
        self.image = pygame.transform.scale(self.image, (300, 200))
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 350

    def deplacement_droite(self):
        # TODO : Si le canard n'est pas au bord droit (1600), on ajoute sa vitesse
        if self.rect.x < ________:
            self.rect.x = self.rect.x + self.________

    def deplacement_gauche(self):
        # TODO : Si le canard n'est pas au bord gauche (0), on soustrait sa vitesse
        if self.rect.x > ________:
            self.rect.x = self.rect.x - self.________
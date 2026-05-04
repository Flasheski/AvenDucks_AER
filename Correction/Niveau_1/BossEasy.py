import pygame

class BossEasy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.attack = 5
        self.velocity = 2
        
        self.image_base = pygame.image.load('assets/bosseasy.png')
        self.image_base = pygame.transform.scale(self.image_base, (150, 150)) 
        self.image = self.image_base
        self.rect = self.image.get_rect()

        self.rect.x = 1200
        self.rect.y = 450
        self.direction = -1 

    def deplacer(self):
        self.rect.x += self.velocity * self.direction
        
        if self.rect.x <= 700:
            self.direction = 1
            self.image = pygame.transform.flip(self.image_base, True, False)
        elif self.rect.x >= 1300:
            self.direction = -1
            self.image = self.image_base
            
    def update_pv(self, surface):
        # je viens dessiner la barre de pv au-dessus du boss
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x, self.rect.y - 20, self.max_health, 10])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x, self.rect.y - 20, max(0, self.health), 10])
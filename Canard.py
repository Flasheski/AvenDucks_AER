import pygame

class Canard(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.attack = 10 
        self.velocity = 1.5
        
        # charge les deux images
        self.image_base = pygame.image.load('assets/canard.png')
        self.image_epee = pygame.image.load('assets/canardepee.png') 
        
        #redimensionne les images avant de créer le rect
        self.image_base = pygame.transform.scale(self.image_base, (400, 270))
        self.image_epee = pygame.transform.scale(self.image_epee, (400, 270))
        
        self.image = self.image_base # image de depart sans épee
        self.rect = self.image.get_rect() # maj du rect
        self.rect.x = -100
        self.rect.y = 330
        
        self.a_une_epee = False # au début il a pas lépée

    def deplacement_droite(self):
        self.rect.x += self.velocity

    def deplacement_gauche(self):
        self.rect.x -= self.velocity

    def ramasser_epee(self):
        self.a_une_epee = True
        self.image = self.image_epee # fonctionn pour changer l'image pour que ca face genre qu'il l'ait ramassé
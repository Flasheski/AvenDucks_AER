import pygame
from Canard import Canard
from Epee import Epee # On importe la nouvelle classe

class Jeu():

    def __init__(self):
        self.canard = Canard()
        self.epee = Epee() # charge l'épée
        self.epee_au_sol = True # pour l'afficher ou  non on met en binaire
        self.pressed = {} 

    def verifier_collision(self):
        # on fait une nvl hitbox du canard car sinon il attrape l'épée de trop loin, plus cest bas plus il attrape de proche
        hitbox_canard = self.canard.rect.inflate(-150, -50)

        #on teste la collision sur la hitbox et non sur le grand rect
        if self.epee_au_sol and hitbox_canard.colliderect(self.epee.rect):
            self.epee_au_sol = False # L'épée n'est plus au sol
            self.canard.ramasser_epee() # Le canard change d'image
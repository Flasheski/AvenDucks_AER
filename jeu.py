import pygame
from Canard import Canard
from Epee import Epee # On importe la nouvelle classe

class Jeu():

    def __init__(self):
        self.canard = Canard()
        self.epee = Epee() # charge l'épée
        self.epee_au_sol = True # Booléen pour savoir si on doit l'afficher
        self.pressed = {} 

    def verifier_collision(self):
        # Si l'épée est par terre ET que le rect du canard touche le rect de l'épée
        if self.epee_au_sol and self.canard.rect.colliderect(self.epee.rect):
            self.epee_au_sol = False # L'épée n'est plus au sol
            self.canard.ramasser_epee() # Le canard change d'image
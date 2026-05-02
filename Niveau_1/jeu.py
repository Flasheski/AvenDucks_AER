import pygame
from Canard import Canard
from Epee import Epee 
from BossEasy import BossEasy

class Jeu():
    def __init__(self):
        self.canard = Canard()
        self.epee = Epee() 
        self.boss_easy = BossEasy()
        self.epee_au_sol = True 
        self.boss_vivant = True
        self.pressed = {} 

    def verifier_collision(self):
        hitbox_canard = self.canard.rect.inflate(-150, -50)

        if self.epee_au_sol and hitbox_canard.colliderect(self.epee.rect):
            self.epee_au_sol = False 
            self.canard.ramasser_epee() 
            
        # je retire des pv au canard quand le boss le touche
        if self.boss_vivant and hitbox_canard.colliderect(self.boss_easy.rect):
            self.canard.health -= self.boss_easy.attack / 10
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
        
        # Ramassage de l'épée
        if self.epee_au_sol and hitbox_canard.colliderect(self.epee.rect):
            self.epee_au_sol = False 
            self.canard.ramasser_epee()
            
        # Dégâts reçus par le canard quand le boss le touche
        if self.boss_vivant and hitbox_canard.colliderect(self.boss_easy.rect):
            self.canard.health -= self.boss_easy.attack / 10

    def verifier_attaque_joueur(self):
        if self.boss_vivant and self.canard.a_une_epee and self.canard.en_attaque:
            hitbox_canard = self.canard.rect.inflate(-150, -50)
            
            # Si le canard attaque en touchant le boss
            if hitbox_canard.colliderect(self.boss_easy.rect):
                self.boss_easy.health -= 1 # Le boss perd des PV
                
                # Si le boss n'a plus de vie
                if self.boss_easy.health <= 0:
                    self.boss_vivant = False
                    print("Le Boss Easy est vaincu !")
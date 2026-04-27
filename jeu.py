import pygame
from Canard import Canard
from Epee import Epee 
from BossEasy import BossEasy

class Jeu():

    def __init__(self):
        self.canard = Canard()
        self.epee = Epee() # charge l'épée
        self.boss_easy = BossEasy()
        self.epee_au_sol = True # pour l'afficher ou non on met en binaire
        self.boss_vivant = True
        self.pierres_obtenues = 0 # je démarre le compteur de pierres (à la fin du premier boss on le met à 1)
        self.pressed = {} 

    def verifier_collision(self):
        # on fait une nvl hitbox du canard car sinon il attrape l'épée de trop loin, plus cest bas plus il attrape de proche
        hitbox_canard = self.canard.rect.inflate(-150, -50)

        # on teste la collision sur la hitbox et non sur le grand rect
        if self.epee_au_sol and hitbox_canard.colliderect(self.epee.rect):
            self.epee_au_sol = False # L'épée n'est plus au sol
            self.canard.ramasser_epee() # Le canard change d'image
            
        if self.boss_vivant and hitbox_canard.colliderect(self.boss_easy.rect):
            # je retire des pv au canard quand il le touche
            self.canard.health -= self.boss_easy.attack / 10 

    def attaquer_boss(self):
        # Vérifie si on a l'épée, qu'on attaque et que le boss est en vie
        if self.boss_vivant and self.canard.a_une_epee and self.canard.en_attaque:
            # hitbox agrandie pour le canard pour l'attaque
            hitbox_attaque = self.canard.rect.inflate(50, 0) 
            
            if hitbox_attaque.colliderect(self.boss_easy.rect):
                self.boss_easy.health -= self.canard.attack # On enlève 10 PV (l'attaque du canard)
                print(f"PV du Boss : {self.boss_easy.health}")
                
                # Si le boss meurt
                if self.boss_easy.health <= 0:
                    self.boss_vivant = False
                    self.pierres_obtenues += 1
                    print(f"Boss Vaincu ! Pierres : {self.pierres_obtenues}/6")
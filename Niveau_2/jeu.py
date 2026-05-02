import pygame
from Canard import Canard
from BossMedium import BossMedium

class Jeu():
    def __init__(self):
        self.canard = Canard()
        self.boss = BossMedium()
        self.boss_vivant = True
        self.victoire = False
        self.pressed = {}

    def verifier_collision(self):
        if self.boss_vivant:
            # 1 Le canard touche le boss
            for tir in self.canard.projectiles:
                if tir.rect.colliderect(self.boss.rect):
                    self.boss.health -= 15
                    self.canard.projectiles.remove(tir)
                    
                    if self.boss.health <= 0:
                        self.boss_vivant = False
                        self.victoire = True
                        print("\n==================================================")
                        print("💀 CYBER-DRAGON BATTU ! Niveau 2 terminé !")
                        print("==================================================")

        # 2 Le boss touche le canard
        hitbox_canard = self.canard.rect.inflate(-100, -50)
        for tir in self.boss.projectiles:
            if tir.rect.colliderect(hitbox_canard):
                self.canard.health -= 20
                self.boss.projectiles.remove(tir)
                if self.canard.health <= 0:
                    print("Game Over : Tu as été désintégré !")
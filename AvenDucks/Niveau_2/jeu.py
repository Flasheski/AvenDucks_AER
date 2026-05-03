import pygame
from AvenDucks.Niveau_2.Canard import Canard
from AvenDucks.Niveau_2.BossMedium import BossMedium

class Jeu():
    def __init__(self):
        self.canard = Canard()
        self.boss = BossMedium()
        self.boss_vivant = True
        self.victoire = False
        self.game_over = False
        self.pressed = {}

    def verifier_collision(self):
        if self.boss_vivant:
            # Le canard touche le boss
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
                    break;

        # Le boss touche le canard
        hitbox_canard = self.canard.rect.inflate(-100, -50)
        for tir in self.boss.projectiles:
            if tir.rect.colliderect(hitbox_canard):
                self.canard.health -= 10
                self.boss.projectiles.remove(tir)
                
                # Déclenchement du Game Over
                if self.canard.health <= 0:
                    print("Game Over : Tu as été désintégré !")
                    self.game_over = True
import pygame
from AvenDucks.Niveau_3.Canard import Canard
from AvenDucks.Niveau_3.BossFinal import BossFinal

class Jeu():
    def __init__(self):
        self.canard = Canard()
        self.boss = BossFinal() # On charge le nouveau boss
        self.boss_vivant = True
        self.victoire = False
        self.game_over = False
        self.pressed = {}

    def verifier_collision(self):
        if self.boss_vivant:
            
            # 1. Les tirs normaux ne font PAS de dégâts
            for tir in self.canard.projectiles:
                if tir.rect.colliderect(self.boss.rect):
                    self.canard.projectiles.remove(tir)
                    print("L'armure du boss est trop épaisse pour des tirs normaux !")

            # 2. L'attaque spéciale fait de gros dégâts
            for tir_spe in self.canard.projectiles_speciaux:
                if tir_spe.rect.colliderect(self.boss.rect):
                    self.boss.health -= 100 # -100 PV par missile !
                    self.canard.projectiles_speciaux.remove(tir_spe)
                    print(f"BOOM ! PV du Boss : {self.boss.health}")
                    
                    if self.boss.health <= 0:
                        self.boss_vivant = False
                        self.victoire = True
                        print("\n==================================================")
                        print("🔥 BOSS FINAL VAINCU ! TU AS SAUVÉ L'ÉCOLE !")
                        print("🎁 RÉCOMPENSE OBTENUE : LE GANT D'INFINITÉ !")
                        print("🏆 LE GOAT : Développeur Légendaire")
                        print("==================================================")
                        break

        # 3. Le boss touche le canard
        hitbox_canard = self.canard.rect.inflate(-100, -50)
        for tir in self.boss.projectiles:
            if tir.rect.colliderect(hitbox_canard):
                self.canard.health -= 10
                self.boss.projectiles.remove(tir)
                
                if self.canard.health <= 0:
                    print("Game Over : Tu as été désintégré !")
                    self.game_over = True
                    break
import pygame
from Canard import Canard
from Epee import Epee
from BossEasy import BossEasy

class Jeu():
    def __init__(self):
        self.canard = Canard()
        self.epee = Epee()
        self.boss = BossEasy()
        self.pressed = {}

    def verifier_collision(self):
        if self.epee.active:
            # TODO : Si le rectangle du canard "entre en collision" avec l'épée
            if self.canard.rect.________(self.epee.rect):
                # TODO : L'épée n'est plus active (False)
                self.epee.active = ________
                print("Tu as ramassé l'épée !")
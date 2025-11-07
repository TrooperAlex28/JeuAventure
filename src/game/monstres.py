import random
from src.game.constants import Difficulty

class Monstre:
    def __init__(self, nom, points_vies, attaque):
        self.nom = nom
        self.points_vies = points_vies
        self.attaque = attaque

def generate_monster(difficulty):
    choix = random.randint(0, 2)
    if choix == 0: # Troll Frustré
        if difficulty == Difficulty.EASY:
            pv, att = random.randint(22, 28), random.randint(15, 19)
        elif difficulty == Difficulty.MEDIUM:
            pv, att = random.randint(25, 32), random.randint(19, 24)
        else: # HARD
            pv, att = random.randint(28, 35), random.randint(24, 29)
        return Monstre("Troll Frustré", pv, att)
    elif choix == 1: # Squelette Faché
        if difficulty == Difficulty.EASY:
            pv, att = random.randint(22, 28), random.randint(10, 15)
        elif difficulty == Difficulty.MEDIUM:
            pv, att = random.randint(25, 32), random.randint(15, 19)
        else: # HARD
            pv, att = random.randint(28, 35), random.randint(19, 24)
        return Monstre("Squelette Faché", pv, att)
    else: # Ghoul Mécontente
        if difficulty == Difficulty.EASY:
            pv, att = random.randint(18, 22), random.randint(7, 10)
        elif difficulty == Difficulty.MEDIUM:
            pv, att = random.randint(20, 27), random.randint(12, 17)
        else: # HARD
            pv, att = random.randint(25, 33), random.randint(14, 19)
        return Monstre("Ghoul Mécontente", pv, att)

def generate_final_boss(difficulty):
    if difficulty == Difficulty.EASY:
        pv, att = random.randint(90, 120), random.randint(25, 35)
    elif difficulty == Difficulty.MEDIUM:
        pv, att = random.randint(100, 130), random.randint(30, 40)
    else: # HARD
        pv, att = random.randint(100, 150), random.randint(35, 45)
    return Monstre("Dragon en /$%?/@", pv, att)
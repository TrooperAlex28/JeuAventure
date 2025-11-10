import random

class Weapon:
    def __init__(self, nom, attaque):
        self.nom = nom
        self.attaque = attaque

class Shield:
    def __init__(self, nom, defense):
        self.nom = nom
        self.defense = defense

class Potion:
    def __init__(self, nom, soin):
        self.nom = nom
        self.soin = soin

def create_items():
    epee = Weapon("Épée un peu molle", 10)
    epee_fer = Weapon("Épée en fer", 15)
    hache = Weapon("Hache qui tue", 20)
    masse = Weapon("Masse qui écrase", 25)
    bouclier = Shield("Bouclier de bois", 5)
    bouclier_fer = Shield("Bouclier de fer", 10)
    grand_bouclier = Shield("Grand Bouclier de fer", 15)
    potion = Potion("Potion de soin", random.randint(15, 30))
    return epee, epee_fer, hache, masse, bouclier, bouclier_fer, grand_bouclier, potion

def epee_legendaire():
    return Weapon("Épée Légendaire", 50)

def consume_potion(j):
    if j.inventaire:
        p = j.inventaire.pop()
        max_hp = 100
        j.points_vies += p.soin
        if j.points_vies > max_hp:
            j.points_vies = max_hp
        print(f"Vous buvez {p.nom} et récupérez {p.soin} PV. PV = {j.points_vies}")
        print(" ")
    else:
        print("Vous n'avez aucune potion...")
        print(" ")
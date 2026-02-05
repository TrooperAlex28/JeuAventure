class InfoJoueur:
    def __init__(self, points_vies, base_attaque, defense, inventaire, equipped, equipped_shield, description):
        self.points_vies = points_vies
        self.base_attaque = base_attaque
        self.defense = defense
        self.inventaire = inventaire
        self.equipped = equipped
        self.equipped_shield = equipped_shield
        self.description = description
    def defense_totale(self):
        return self.defense + (self.equipped_shield.defense if self.equipped_shield else 0)
    def attaque_totale(self):
        return self.base_attaque + (self.equipped.attaque if self.equipped else 0)

class Guerrier2(InfoJoueur):
    def __init__(self, points_vies, base_attaque, defense, inventaire, equipped, equipped_shield, description):
        super().__init__(points_vies, base_attaque, defense, inventaire, equipped, equipped_shield, description)
        
        self.description = description

class Guerrier1(InfoJoueur):
    def __init__(self, points_vies, base_attaque, defense, inventaire, equipped, equipped_shield, description):
        super().__init__(points_vies, base_attaque, defense, inventaire, equipped, equipped_shield, description)
        
        self.description = description

class Guerrier3(InfoJoueur):
    def __init__(self, points_vies, base_attaque, defense, inventaire, equipped, equipped_shield, description):
        super().__init__(points_vies, base_attaque, defense, inventaire, equipped, equipped_shield, description)
        
        self.description = description

class default_Guerrier(InfoJoueur):
    def __init__(self, points_vies, base_attaque, defense, inventaire, equipped, equipped_shield, description):
        super().__init__(points_vies, base_attaque, defense, inventaire, equipped, equipped_shield, description)
        
        self.description = description

def display_status(j):
    """Affiche l'état du joueur `j`. Conservé comme fonction pour que d'autres modules puissent simplement l'appeler display_status(j)."""
    print("-"*20)
    print("-- État du joueur --")
    att = j.attaque_totale()
    def_total = j.defense_totale()
    print(f"PV: {j.points_vies} | Att: {att} | Def: {def_total}")
    print(f"Potions: {len(j.inventaire)}")
    if j.equipped:
        print(f"Arme équipée: {j.equipped.nom} (+{j.equipped.attaque} Att)")
    else:
        print("Arme équipée: Aucune")
    if j.equipped_shield:
        print(f"Bouclier équipé: {j.equipped_shield.nom} (+{j.equipped_shield.defense} Def)")
    else:
        print("Bouclier équipé: Aucun")
    print("-"*20)
import time
import random

from jeuaventure.game.constants import CombatResult
from jeuaventure.game.objets import create_items, consume_potion
from jeuaventure.game.hero import display_status
from jeuaventure.game.utils import read_input, random_event

def combat(j, m):
    print(f"Un {m.nom} apparaît ! (PV: {m.points_vies}, Att: {m.attaque})")
    time.sleep(0.3)
    while True:
        cmd = read_input("Choix (a = attaquer/ p = potion/ f = fuir/ e = état) > ")
        if cmd in ["a", "attaquer"]:
            dmg_to_monstre = max(1, j.attaque_totale())
            m.points_vies -= dmg_to_monstre
            print(" ")
            print(f"Vous infligez {dmg_to_monstre} dégâts au {m.nom}.")
            time.sleep(0.22)

            if m.points_vies <= 0:
                print(f"Vous avez vaincu le {m.nom} !")
                print(" ")
                time.sleep(0.35)
                if random_event(20):
                    _, _, _, _, _, _, _, potion = create_items()
                    if len(j.inventaire) < 3:
                        j.inventaire.append(potion)
                        print(f"Le {m.nom} lâche une potion : {potion.nom}")
                        print(" ")
                        time.sleep(0.2)
                    else:
                        print(f"Le {m.nom} a lâché une potion, mais votre inventaire est plein.")
                        print(" ")
                        time.sleep(0.2)
                return CombatResult.DEFEATED

            dmg_to_joueur = max(1, m.attaque - j.defense_totale())
            j.points_vies -= dmg_to_joueur
            print(f"Le {m.nom} vous attaque et inflige {dmg_to_joueur} dégâts. Vos PV = {j.points_vies}")
            print(" ")
            time.sleep(0.22)

            if j.points_vies <= 0:
                print("\nVos blessures sont trop graves, vous ne pouvez plus continuer...")
                print("La mort vous emporte.\n")
                return CombatResult.DEAD

        elif cmd in ["f", "fuir"]:
            if random_event(50):
                print("\nVous réussissez à fuir.\n")
                time.sleep(0.18)
                return CombatResult.FLED
            else:
                print("Fuite échouée ! Le {} attaque.".format(m.nom))
                time.sleep(0.18)
                dmg = max(1, m.attaque - j.defense_totale())
                j.points_vies -= dmg
                print(f"\nVous subissez {dmg} dégâts en fuyant. Vos PV = {j.points_vies}\n")
                time.sleep(0.2)
                if j.points_vies <= 0:
                    print("\nVos blessures sont trop graves, vous ne pouvez plus continuer...")
                    print("La mort vous emporte.\n")
                    return CombatResult.DEAD
        
        elif cmd in ["p", "potion"]:
            if len(j.inventaire) > 0:
                consume_potion(j)
                time.sleep(0.2)
            else:
                print("Vous n'avez pas de potion.")
                time.sleep(0.2)
        
        elif cmd in ["e", "etat"]:
            # display_status is a function that prints the status
            display_status(j)
            time.sleep(0.12)
        
        else:
            print("Commande inconnue.")
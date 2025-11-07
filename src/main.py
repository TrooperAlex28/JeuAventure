import random
import time
import sys
from src.game.constants import Difficulty, CombatResult
from src.game.utils import read_input, random_event, slow_println
from src.game.objets import Weapon, Shield, Potion
from src.game.hero import Guerrier1, Guerrier2, Guerrier3, default_Guerrier
from src.game.monstres import Monstre
from src.game.monstres import generate_monster, generate_final_boss
from src.game.combat import combat
from src.game.boss import boss_encounter
from src.game.objets import create_items, consume_potion
from src.game.hero import display_status








# Difficulty and CombatResult are provided by constants.py

# slow_println moved to utils.py

def intro():
    slow_println("Bienvenue dans le jeu dont vous êtes le héros !", 400)
    slow_println("Le Roi vous a convoqué pour retrouver la princesse.", 350)
    slow_println("Dans ce jeu, vous incarnerez un aventurier qui devra faire face à divers défis.", 350)
    slow_println("Choisissez vos actions avec soin pour survivre !", 350)
    slow_println("Vous devez vaincre tous les monstres du donjon maudit.", 300)
    slow_println("Bonne chance !", 500)
    print(" ")

def parse_difficulty(s):
    s = s.strip().lower()
    if s in ["f", "facile"]:
        return Difficulty.EASY
    elif s in ["m", "moyen"]:
        return Difficulty.MEDIUM
    elif s in ["d", "difficile"]:
        return Difficulty.HARD
    else:
        return Difficulty.EASY # Default

def parse_hero_choice(s):
    s = s.strip().lower()
    if s in ["1", "guerrier"]:
        return "guerrier"
    elif s in ["2", "mage"]:
        return "mage"
    elif s in ["3", "archer"]:
        return "archer"
    else:
        return "guerrier"  # Default
    

# read_input and random_event moved to utils.py










def game_loop(j, remaining_monsters, difficulty):
    print(" ")
    slow_println("Vous êtes dans un donjon.", 300)
    slow_println("Tout au long de votre exploration, vous pouvez rencontrer des monstres ou trouver des objets.\n", 300)

    while True:
        time.sleep(0.1)
        print("Que voulez-vous faire ?")
        print("Tapez 'a' pour avancer, 'p' pour potion, 'e' pour état, 'q' pour quitter.")
        cmd = read_input("> ")
        print(" ")

        if cmd in ["a", "avancer"]:
            if random_event(40): # Rencontre monstre
                monstre = generate_monster(difficulty)
                result = combat(j, monstre)
                if result == CombatResult.DEFEATED:
                    remaining_monsters -= 1
                    print(f"Monstres restants: {remaining_monsters}\n")
                    if remaining_monsters <= 0:
                        # This part of the logic was unreachable in the original Rust code
                        # because the boss fight happens after the game_loop.
                        # I'll keep it similar for now.
                        return True
                elif result == CombatResult.DEAD:
                    print("Fin de la partie.")
                    return False # Game over
            
            elif random_event(30): # Trouvaille potion
                _, _, _, _, _, _, _, potion = create_items()
                if len(j.inventaire) < 4:
                    j.inventaire.append(potion)
                    print(f"Vous trouvez une potion : {potion.nom}")
                    print(" ")
                    time.sleep(0.22)
                else:
                    print("Vous trouvez une potion, mais l'inventaire est plein.")
                    print(" ")
                    time.sleep(0.22)

            elif random_event(25): # Trouvaille arme
                w1, w2, w3, w4, _, _, _, _ = create_items()
                found = random.choice([w1, w2, w3, w4])
                print(f"Vous trouvez une arme: {found.nom} (+{found.attaque} Att)")
                time.sleep(0.24)
                equip = read_input("Voulez-vous l'équiper ? (o/n) > ")
                if equip in ["o", "oui", "y"]:
                    j.equipped = found
                    print(f"Vous équipez {j.equipped.nom}.")
                    print(" ")
                    time.sleep(0.16)
                else:
                    print("Vous laissez l'arme.")
                    print(" ")
                    time.sleep(0.14)

            elif random_event(20): # Trouvaille bouclier
                _, _, _, _, s1, s2, s3, _ = create_items()
                found_shield = random.choice([s1, s2, s3])
                print(f"Vous trouvez un bouclier: {found_shield.nom} (+{found_shield.defense} Def)")
                print(" ")
                time.sleep(0.24)
                equip_sh = read_input("Voulez-vous l'équiper ? (o/n) > ")
                if equip_sh in ["o", "oui", "y"]:
                    j.equipped_shield = found_shield
                    print(f"Vous équipez {j.equipped_shield.nom}.")
                    print(" ")
                    time.sleep(0.16)
                else:
                    print("Vous laissez le bouclier.")
                    time.sleep(0.14)
            else:
                print("Rien d'intéressant ici...vous continuez votre quête.\n")
                time.sleep(0.12)

        elif cmd in ["p", "potion"]:
            consume_potion(j)
        elif cmd in ["e", "etat"]:
            display_status(j)
        elif cmd in ["q", "quitter"]:
            slow_println("Vous avez abandonné la quête.", 300)
            slow_println("La princesse sera dévorée par les monstres...", 300)
            slow_println("Je vous remercie d'avoir joué... mais la princesse elle...\n", 300)
            return False # Quit game
        else:
            print("Commande non reconnue. (avancer/potion/etat/quitter)")

        if j.points_vies <= 0:
            print("Fin de la partie.\n")
            return False # Game over
        
        if remaining_monsters <= 0:
            return True # Proceed to boss




def main():
    print("Jeu dont vous êtes le héros !\n")
    intro()

    print("Choisissez la difficulté : f = Facile, m = Moyen, d = Difficile")
    difficulty_input = read_input("> ")
    difficulty = parse_difficulty(difficulty_input)
    print(" ")

    epee_de_base, _, _, _, _, _, _, potion = create_items()

    print("Choix du personnage :")
    print("1. Lancelot le chevalier")
    print("2. Ivar le viking")
    print("3. Shera la guerrière")
    personnage_input = read_input("> ")
    

    if personnage_input == "1":
        joueur = Guerrier1(
            points_vies=100,
            base_attaque=10,
            defense=5,
            inventaire=[potion],
            equipped=epee_de_base,
            equipped_shield=None,
            description="Lancelot, le chevalier au courage légendaire."
        )
        print(f"Vous incarnez {joueur.description}.")
    elif personnage_input == "2":
        joueur = Guerrier2(
            points_vies=100,
            base_attaque=12,
            defense=5,
            inventaire=[potion],
            equipped=epee_de_base,
            equipped_shield=None,
            description="Ivar, le viking terrifiant."
        )
        print(f"Vous incarnez {joueur.description}.")
    elif personnage_input == "3":
        joueur = Guerrier3(
            points_vies=100,
            base_attaque=10,
            defense=3,
            inventaire=[potion],
            equipped=epee_de_base,
            equipped_shield=None,
            description="Shera, la guerrière au style inégalé."
        )
        print(f"Vous incarnez {joueur.description}.")
    else:
        print("Choix invalide, vous incarnez un Guerrier par défaut.")
        joueur = default_Guerrier(
            points_vies=100,
            base_attaque=10,
            defense=5,
            inventaire=[potion],
            equipped=epee_de_base,
            equipped_shield=None,
            description="Un guerrier robuste et courageux."
        )
        
    if difficulty == Difficulty.EASY:
        nb_monstres = 5
    elif difficulty == Difficulty.MEDIUM:
        nb_monstres = 7
    else: # HARD
        nb_monstres = 10
   


    # Lancer la boucle de jeu
    proceed_to_boss = game_loop(joueur, nb_monstres, difficulty)

    # Si le joueur n'est pas mort et n'a pas quitté
    if proceed_to_boss and joueur.points_vies > 0:
        boss_encounter(joueur, difficulty)

if __name__ == "__main__":
    main()




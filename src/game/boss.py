import time
from src.game.utils import slow_println

from src.game.constants import CombatResult
from src.game.monstres import generate_final_boss
from src.game.combat import combat
from src.game.utils import slow_println
from src.game.objets import epee_legendaire

def boss_encounter(joueur, difficulty):
    """Handle the final boss sequence: generate boss, run combat, and print outcome.

    This function is intentionally independent so it can be moved or tested separately.
    """
    time.sleep(1)
    slow_println("\n🎉 VICTOIRE ! Vous avez vaincu tous les monstres du donjon !", 300)
    slow_println("Vous vous approchez du cachot lorsque dragon en /$%?/@ sort d'une grotte derrière la princesse et vous bloque le chemin.\nSi vous fuyez, c'est la fin pour la princesse.\nPrenez votre courage à deux mains et affrontez le dragon!\n", 300)
    time.sleep(2)
    slow_println("Le Dragon en /$%?/@ rugit et se prépare à attaquer !", 300)
    time.sleep(2)
    slow_println("Vous voyez une lueur étrange dans le coin de la pièce...\nC'est une Épée Légendaire ! Vous vous précipitez afin de l'attraper avant que le dragon attaque.\n", 300)
    joueur.arme = epee_legendaire()
    slow_println(f"Vous êtes maintenant équipé de l'Épée Légendaire !", 300)
    boss = generate_final_boss(difficulty)
    result = combat(joueur, boss)

    if result == CombatResult.DEFEATED:
        slow_println("🎉 VICTOIRE ! Vous avez vaincu le Dragon !", 300 )
        slow_println("👸 Vous retournez au chateau avec la princesse !", 300)
        slow_println("👑 Le Roi vous nomme Chevalier du Royaume !", 300)
        slow_println("Je vous remercie d'avoir joué !\n", 300)
    elif result == CombatResult.FLED:
        slow_println("Vous avez fui le combat contre le boss final.", 300)
        slow_println("La princesse sera dévorée par les monstres...", 300)
        slow_println("Je vous remercie d'avoir joué... mais la princesse elle...\n", 300)
    elif result == CombatResult.DEAD:
        slow_println("\nVous êtes mort !", 300)
        slow_println("La princesse sera dévorée par les monstres...", 300)
        slow_println("Je vous remercie d'avoir joué... mais la princesse elle...\n", 300)

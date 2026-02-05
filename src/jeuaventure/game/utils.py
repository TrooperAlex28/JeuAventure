import random
import sys
import time


def read_input(prompt):
    """Lit une entrée de l'utilisateur, la normalise et retourne une chaîne en minuscules sans espaces."""
    return input(prompt).strip().lower()


def random_event(chance_percent):
    """Retourne True avec une probabilité de chance_percent (0-100)."""
    return random.randint(0, 99) < chance_percent


def slow_println(s, ms):
    """Affiche une ligne et attend ms millisecondes (vide d'abord stdout)."""
    print(s)
    sys.stdout.flush()
    time.sleep(ms / 1000.0)

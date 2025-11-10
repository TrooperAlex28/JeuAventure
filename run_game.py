"""Launcher script to run the game from the project root.

Run this instead of executing src/main.py directly. This ensures the
`src` package is importable and preserves the package-style imports
used across the codebase (e.g. `src.game.*`).
"""

import runpy
import sys
import os

# Assurer que le répertoire 'src' est dans le PYTHONPATH afin d'importer
# le paquet `jeuaventure` qui se trouve dans src/jeuaventure.
ROOT = os.path.dirname(__file__)  # dossier du projet
SRC = os.path.join(ROOT, "src")

if SRC not in sys.path:
    # on ajoute le dossier src (contenant le paquet jeuaventure)
    sys.path.insert(0, SRC)

if __name__ == "__main__":
    # Exécuter le module principal du paquet (lance le script comme s'il
    # était exécuté directement). Utilise runpy pour conserver le comportement
    # attendu (affichage, etc.).
    runpy.run_module("jeuaventure.main", run_name="__main__", alter_sys=True)

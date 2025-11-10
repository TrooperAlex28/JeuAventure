# JeuAventure

Un petit jeu textuel en Python — "Jeu dont vous êtes le héros" — organisé en paquet Python sous `src/jeuaventure`.

## Lancer le jeu

La façon recommandée d'exécuter le jeu depuis la racine du projet :

PowerShell

```powershell
python run_game.py
```

Le script `run_game.py` ajoute automatiquement `src/` au `PYTHONPATH` afin que les imports de type `jeuaventure.*` fonctionnent correctement.

## Structure du projet

```text
JeuAventure/
├─ run_game.py        # lanceur qui prépare le PYTHONPATH
├─ src/
│  └─ jeuaventure/
│     ├─ main.py      # point d'entrée principal du jeu
│     └─ game/        # modules du jeu (combat, héros, monstres, objets...)
├─ .vscode/           # réglages pour VSCode (analysis.extraPaths = ./src)
└─ README.md
```

## Exécution dans VSCode

- Le workspace contient `.vscode/settings.json` qui ajoute `./src` à `python.analysis.extraPaths` pour que Pylance résolve `jeuaventure.*`.
- Pour déboguer, tu peux configurer `launch.json` ou exécuter `run_game.py` dans la configuration de débogage.

## Développement

- Le code du jeu se trouve dans `src/jeuaventure/game/`. Ajoute de nouvelles fonctionnalités (cartes, quêtes, loot) dans ce dossier.
- Pour tester rapidement l'importation sans lancer l'interface interactive :

```powershell
python -c "import sys, os; sys.path.insert(0, os.path.join(os.getcwd(),'src')); import importlib; importlib.import_module('jeuaventure.main')"
```

Cela importe le module sans exécuter l'interface interactive (utile pour vérifier les erreurs d'import).

## Exigences

- Python 3.10+ (le projet a été testé avec Python 3.13).
- Aucune dépendance externe nécessaire pour l'instant (tout est en pur Python standard).

## Conseils et troubleshooting

- Si VSCode signale des imports non résolus, vérifie que `.vscode/settings.json` contient:

```json
{
"python.analysis.extraPaths": ["./src"]
}
```

- Si le jeu ne démarre pas correctement, lance `run_game.py` depuis la racine du projet (cela garantit que `src` est visible).

## Contributions

- Si tu souhaites que j'ajoute des fonctionnalités (carte, PNJ, arbre de compétences, sauvegarde), dis lesquelles et je peux les implémenter pas-à-pas.

Bonne exploration !

"""Launcher script to run the game from the project root.

Run this instead of executing src/main.py directly. This ensures the
`src` package is importable and preserves the package-style imports
used across the codebase (e.g. `src.game.*`).
"""
from src.main import main


if __name__ == "__main__":
    main()

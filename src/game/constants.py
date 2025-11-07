from enum import Enum


class Difficulty(Enum):
    EASY = 1
    MEDIUM = 2
    HARD = 3


class CombatResult(Enum):
    DEFEATED = 1
    FLED = 2
    DEAD = 3

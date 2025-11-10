import random

class Room:
    def __init__(self, kind='empty'):
        self.kind = kind        # 'empty', 'monster', 'treasure', 'npc', 'boss'
        self.visited = False
        self.cleared = False    # monster defeated / treasure taken / npc spoken

class WorldMap:
    def __init__(self, size: int, nb_monsters: int):
        self.size = size
        self.grid = [[Room() for _ in range(size)] for _ in range(size)]
        self.player_pos = (0, 0)
        self.boss_pos = (size - 1, size - 1)
        self.grid[self.boss_pos[0]][self.boss_pos[1]] = Room('boss')
        self._place_rooms(nb_monsters)

    def _place_rooms(self, nb_monsters):
        placed = 0
        while placed < nb_monsters:
            x = random.randrange(self.size)
            y = random.randrange(self.size)
            if (x, y) in [(0, 0), self.boss_pos]:
                continue
            if self.grid[x][y].kind == 'empty':
                self.grid[x][y].kind = 'monster'
                placed += 1
        # autres types (faible probabilité)
        for i in range(self.size):
            for j in range(self.size):
                if self.grid[i][j].kind == 'empty':
                    r = random.random()
                    if r < 0.08:
                        self.grid[i][j].kind = 'treasure'
                    elif r < 0.14:
                        self.grid[i][j].kind = 'npc'

    def current_room(self):
        x, y = self.player_pos
        return self.grid[x][y]

    def move_player(self, direction: str):
        x, y = self.player_pos
        direction = direction.lower()
        if direction in ['n', 'north', 'haut']:
            nx, ny = x - 1, y
        elif direction in ['s', 'south', 'bas']:
            nx, ny = x + 1, y
        elif direction in ['w', 'west', 'gauche']:
            nx, ny = x, y - 1
        elif direction in ['e', 'east', 'droite']:
            nx, ny = x, y + 1
        else:
            return False, "Direction inconnue."

        if 0 <= nx < self.size and 0 <= ny < self.size:
            self.player_pos = (nx, ny)
            return True, f"Vous vous déplacez en {direction}."
        else:
            return False, "Vous ne pouvez pas aller dans cette direction (mur)."

    def display_map(self, reveal=False):
        # texte simple: P = joueur, B = boss, ? = non-visité, . = visité vide, M/T/N = cleared rooms
        rows = []
        for i in range(self.size):
            cells = []
            for j in range(self.size):
                if (i, j) == self.player_pos:
                    cells.append("P")
                    continue
                room = self.grid[i][j]
                if not reveal and not room.visited:
                    cells.append("?")
                else:
                    if (i, j) == self.boss_pos:
                        cells.append("B")
                    else:
                        if room.kind == 'empty':
                            cells.append(".")
                        elif room.kind == 'monster':
                            cells.append("M" if not room.cleared else "m")
                        elif room.kind == 'treasure':
                            cells.append("T" if not room.cleared else "t")
                        elif room.kind == 'npc':
                            cells.append("N" if not room.cleared else "n")
                        else:
                            cells.append(".")
            rows.append(" ".join(cells))
        return "\n".join(rows)
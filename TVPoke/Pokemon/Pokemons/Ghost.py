from TVPoke.BaseClasses.PokeTypes import Ghost
from TVPoke.BaseClasses.Move import Move
from random import randint


class Sableye(Ghost):
    def __init__(self):
        super().__init__("Sableye", 68, [
            Move("Mega Kick", "NORMAL", 120),
            Move("Thunder", "ELECTRIC", 120),
            Move("Psywave", "PSYCHIC", randint(30,150)),
            Move("Dream Eater", "PSYCHIC", 100)
        ], "./TVPoke/Pokemon/imgs/Sableye.png")


class Shuppet(Ghost):
    def __init__(self):
        super().__init__("Shuppet", 146, [
            Move("Mega Kick", "NORMAL", 120),
            Move("Thunder", "ELECTRIC", 120),
            Move("Psywave", "PSYCHIC", randint(30,150)),
            Move("Dream Eater", "PSYCHIC", 100)
        ], "./TVPoke/Pokemon/imgs/Shuppet.png")


class Banette(Ghost):
    def __init__(self):
        super().__init__("Banette", 147, [
            Move("Mega Kick", "NORMAL", 120),
            Move("Thunder", "ELECTRIC", 120),
            Move("Psywave", "PSYCHIC", randint(30,150)),
            Move("Dream Eater", "PSYCHIC", 100)
        ], "./TVPoke/Pokemon/imgs/Banette.png")


class Duskull(Ghost):
    def __init__(self):
        super().__init__("Duskull", 148, [
            Move("Mega Kick", "NORMAL", 120),
            Move("Thunder", "ELECTRIC", 120),
            Move("Psywave", "PSYCHIC", randint(30,150)),
            Move("Dream Eater", "PSYCHIC", 100)
        ], "./TVPoke/Pokemon/imgs/Duskull.png")


class Dusclops(Ghost):
    def __init__(self):
        super().__init__("Dusclops", 149, [
            Move("Mega Kick", "NORMAL", 120),
            Move("Thunder", "ELECTRIC", 120),
            Move("Psywave", "PSYCHIC", randint(30,150)),
            Move("Dream Eater", "PSYCHIC", 100)
        ], "./TVPoke/Pokemon/imgs/Dusclops.png")
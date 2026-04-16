from TVPoke.BaseClasses.PokeTypes import Ice
from TVPoke.BaseClasses.Move import Move
from random import randint


class Snorunt(Ice):
    def __init__(self):
        super().__init__("Snorunt", 171, [
            Move("Mega Kick", "NORMAL", 120),
            Move("Thunder", "ELECTRIC", 120),
            Move("Psywave", "PSYCHIC", randint(30,150)),
            Move("Dream Eater", "PSYCHIC", 100)
        ], "./TVPoke/Pokemon/imgs/Snorunt.png")


class Glalie(Ice):
    def __init__(self):
        super().__init__("Glalie", 172, [
            Move("Mega Kick", "NORMAL", 120),
            Move("Thunder", "ELECTRIC", 120),
            Move("Psywave", "PSYCHIC", randint(30,150)),
            Move("Dream Eater", "PSYCHIC", 100)
        ], "./TVPoke/Pokemon/imgs/Glalie.png")


class Spheal(Ice):
    def __init__(self):
        super().__init__("Spheal", 173, [
            Move("Mega Kick", "NORMAL", 120),
            Move("Thunder", "ELECTRIC", 120),
            Move("Psywave", "PSYCHIC", randint(30,150)),
            Move("Dream Eater", "PSYCHIC", 100)
        ], "./TVPoke/Pokemon/imgs/Spheal.png")


class Sealeo(Ice):
    def __init__(self):
        super().__init__("Sealeo", 174, [
            Move("Mega Kick", "NORMAL", 120),
            Move("Thunder", "ELECTRIC", 120),
            Move("Psywave", "PSYCHIC", randint(30,150)),
            Move("Dream Eater", "PSYCHIC", 100)
        ], "./TVPoke/Pokemon/imgs/Sealeo.png")


class Walrein(Ice):
    def __init__(self):
        super().__init__("Walrein", 175, [
            Move("Mega Kick", "NORMAL", 120),
            Move("Thunder", "ELECTRIC", 120),
            Move("Psywave", "PSYCHIC", randint(30,150)),
            Move("Dream Eater", "PSYCHIC", 100)
        ], "./TVPoke/Pokemon/imgs/Walrein.png")


class Regice(Ice):
    def __init__(self):
        super().__init__("Regice", 194, [
            Move("Mega Kick", "NORMAL", 120),
            Move("Thunder", "ELECTRIC", 120),
            Move("Psywave", "PSYCHIC", randint(30,150)),
            Move("Dream Eater", "PSYCHIC", 100)
        ], "./TVPoke/Pokemon/imgs/Regice.png")
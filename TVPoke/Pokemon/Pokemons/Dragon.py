from TVPoke.BaseClasses.PokeTypes import Dragon
from TVPoke.BaseClasses.Move import Move
from random import randint


class Bagon(Dragon):
    def __init__(self):
        super().__init__("Bagon", 187, [
            Move("Mega Kick", "NORMAL", 120),
            Move("Thunder", "ELECTRIC", 120),
            Move("Psywave", "PSYCHIC", randint(30,150)),
            Move("Dream Eater", "PSYCHIC", 100)
        ], "./TVPoke/Pokemon/imgs/Bagon.png")


class Shelgon(Dragon):
    def __init__(self):
        super().__init__("Shelgon", 188, [
            Move("Mega Kick", "NORMAL", 120),
            Move("Thunder", "ELECTRIC", 120),
            Move("Psywave", "PSYCHIC", randint(30,150)),
            Move("Dream Eater", "PSYCHIC", 100)
        ], "./TVPoke/Pokemon/imgs/Shelgon.png")


class Salamence(Dragon):
    def __init__(self):
        super().__init__("Salamence", 189, [
            Move("Mega Kick", "NORMAL", 120),
            Move("Thunder", "ELECTRIC", 120),
            Move("Psywave", "PSYCHIC", randint(30,150)),
            Move("Dream Eater", "PSYCHIC", 100)
        ], "./TVPoke/Pokemon/imgs/Salamence.png")


class Latias(Dragon):
    def __init__(self):
        super().__init__("Latias", 196, [
            Move("Mega Kick", "NORMAL", 120),
            Move("Thunder", "ELECTRIC", 120),
            Move("Psywave", "PSYCHIC", randint(30,150)),
            Move("Dream Eater", "PSYCHIC", 100)
        ], "./TVPoke/Pokemon/imgs/Latias.png")


class Latios(Dragon):
    def __init__(self):
        super().__init__("Latios", 197, [
            Move("Mega Kick", "NORMAL", 120),
            Move("Thunder", "ELECTRIC", 120),
            Move("Psywave", "PSYCHIC", randint(30,150)),
            Move("Dream Eater", "PSYCHIC", 100)
        ], "./TVPoke/Pokemon/imgs/Latios.png")


class Rayquaza(Dragon):
    def __init__(self):
        super().__init__("Rayquaza", 200, [
            Move("Mega Kick", "NORMAL", 120),
            Move("Thunder", "ELECTRIC", 120),
            Move("Psywave", "PSYCHIC", randint(30,150)),
            Move("Dream Eater", "PSYCHIC", 100)
        ], "./TVPoke/Pokemon/imgs/Rayquaza.png")
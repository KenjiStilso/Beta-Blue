from TVPoke.BaseClasses.PokeTypes import Dark
from TVPoke.BaseClasses.Move import Move
from random import randint

class Poochyena(Dark):
    def __init__(self):
        super().__init__("Poochyena", 10, [
            Move("Mega Kick", "NORMAL", 120),
            Move("Thunder", "ELECTRIC", 120),
            Move("Psywave", "PSYCHIC", randint(30,150)),
            Move("Dream Eater", "PSYCHIC", 100)
        ], "./TVPoke/Pokemon/imgs/Poochyena.png")

class Mightyena(Dark):
    def __init__(self):
        super().__init__("Mightyena", 11, [
            Move("Mega Kick", "NORMAL", 120),
            Move("Thunder", "ELECTRIC", 120),
            Move("Psywave", "PSYCHIC", randint(30,150)),
            Move("Dream Eater", "PSYCHIC", 100)
        ], "./TVPoke/Pokemon/imgs/Mightyena.png")

class Absol(Dark):
    def __init__(self):
        super().__init__("Absol", 152, [
            Move("Mega Kick", "NORMAL", 120),
            Move("Thunder", "ELECTRIC", 120),
            Move("Psywave", "PSYCHIC", randint(30,150)),
            Move("Dream Eater", "PSYCHIC", 100)
        ], "./TVPoke/Pokemon/imgs/Absol.png")

class Sableye(Dark):
    def __init__(self):
        super().__init__("Sableye", 68, [
            Move("Mega Kick", "NORMAL", 120),
            Move("Thunder", "ELECTRIC", 120),
            Move("Psywave", "PSYCHIC", randint(30,150)),
            Move("Dream Eater", "PSYCHIC", 100)
        ], "./TVPoke/Pokemon/imgs/Sableye.png")


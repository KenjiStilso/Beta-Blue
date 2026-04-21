from TVPoke.BaseClasses.PokeTypes import Flying
from TVPoke.BaseClasses.Move import Move
from random import randint

class Taillow(Flying):
    def __init__(self):
        super().__init__("Taillow", 25, [
            Move("Mega Kick", "NORMAL", 120),
            Move("Thunder", "ELECTRIC", 120),
            Move("Psywave", "PSYCHIC", randint(30,150)),
            Move("Dream Eater", "PSYCHIC", 100)
        ], "./TVPoke/Pokemon/imgs/Taillow.png")

class Swellow(Flying):
    def __init__(self):
        super().__init__("Swellow", 26, [
            Move("Mega Kick", "NORMAL", 120),
            Move("Thunder", "ELECTRIC", 120),
            Move("Psywave", "PSYCHIC", randint(30,150)),
            Move("Dream Eater", "PSYCHIC", 100)
        ], "./TVPoke/Pokemon/imgs/Swellow.png")



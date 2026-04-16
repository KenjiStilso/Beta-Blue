from TVPoke.BaseClasses.PokeTypes import Poison
from TVPoke.BaseClasses.Move import Move
from random import randint


class Gulpin(Poison):
    def __init__(self):
        super().__init__("Gulpin", 95, [
            Move("Mega Kick", "NORMAL", 120),
            Move("Thunder", "ELECTRIC", 120),
            Move("Psywave", "PSYCHIC", randint(30,150)),
            Move("Dream Eater", "PSYCHIC", 100)
        ], "./TVPoke/Pokemon/imgs/Gulpin.png")


class Swalot(Poison):
    def __init__(self):
        super().__init__("Swalot", 96, [
            Move("Mega Kick", "NORMAL", 120),
            Move("Thunder", "ELECTRIC", 120),
            Move("Psywave", "PSYCHIC", randint(30,150)),
            Move("Dream Eater", "PSYCHIC", 100)
        ], "./TVPoke/Pokemon/imgs/Swalot.png")


class Grimer(Poison):
    def __init__(self):
        super().__init__("Grimer", 106, [
            Move("Mega Kick", "NORMAL", 120),
            Move("Thunder", "ELECTRIC", 120),
            Move("Psywave", "PSYCHIC", randint(30,150)),
            Move("Dream Eater", "PSYCHIC", 100)
        ], "./TVPoke/Pokemon/imgs/Grimer.png")


class Muk(Poison):
    def __init__(self):
        super().__init__("Muk", 107, [
            Move("Mega Kick", "NORMAL", 120),
            Move("Thunder", "ELECTRIC", 120),
            Move("Psywave", "PSYCHIC", randint(30,150)),
            Move("Dream Eater", "PSYCHIC", 100)
        ], "./TVPoke/Pokemon/imgs/Muk.png")


class Koffing(Poison):
    def __init__(self):
        super().__init__("Koffing", 108, [
            Move("Mega Kick", "NORMAL", 120),
            Move("Thunder", "ELECTRIC", 120),
            Move("Psywave", "PSYCHIC", randint(30,150)),
            Move("Dream Eater", "PSYCHIC", 100)
        ], "./TVPoke/Pokemon/imgs/Koffing.png")


class Weezing(Poison):
    def __init__(self):
        super().__init__("Weezing", 109, [
            Move("Mega Kick", "NORMAL", 120),
            Move("Thunder", "ELECTRIC", 120),
            Move("Psywave", "PSYCHIC", randint(30,150)),
            Move("Dream Eater", "PSYCHIC", 100)
        ], "./TVPoke/Pokemon/imgs/Weezing.png")


class Seviper(Poison):
    def __init__(self):
        super().__init__("Seviper", 124, [
            Move("Mega Kick", "NORMAL", 120),
            Move("Thunder", "ELECTRIC", 120),
            Move("Psywave", "PSYCHIC", randint(30,150)),
            Move("Dream Eater", "PSYCHIC", 100)
        ], "./TVPoke/Pokemon/imgs/Seviper.png")
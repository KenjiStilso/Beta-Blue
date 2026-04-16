from TVPoke.BaseClasses.PokeTypes import Steel
from TVPoke.BaseClasses.Move import Move
from random import randint


class Mawile(Steel):
    def __init__(self):
        super().__init__("Mawile", 69, [
            Move("Mega Kick", "NORMAL", 120),
            Move("Thunder", "ELECTRIC", 120),
            Move("Psywave", "PSYCHIC", randint(30,150)),
            Move("Dream Eater", "PSYCHIC", 100)
        ], "./TVPoke/Pokemon/imgs/Mawile.png")


class Aron(Steel):
    def __init__(self):
        super().__init__("Aron", 70, [
            Move("Mega Kick", "NORMAL", 120),
            Move("Thunder", "ELECTRIC", 120),
            Move("Psywave", "PSYCHIC", randint(30,150)),
            Move("Dream Eater", "PSYCHIC", 100)
        ], "./TVPoke/Pokemon/imgs/Aron.png")


class Lairon(Steel):
    def __init__(self):
        super().__init__("Lairon", 71, [
            Move("Mega Kick", "NORMAL", 120),
            Move("Thunder", "ELECTRIC", 120),
            Move("Psywave", "PSYCHIC", randint(30,150)),
            Move("Dream Eater", "PSYCHIC", 100)
        ], "./TVPoke/Pokemon/imgs/Lairon.png")


class Aggron(Steel):
    def __init__(self):
        super().__init__("Aggron", 72, [
            Move("Mega Kick", "NORMAL", 120),
            Move("Thunder", "ELECTRIC", 120),
            Move("Psywave", "PSYCHIC", randint(30,150)),
            Move("Dream Eater", "PSYCHIC", 100)
        ], "./TVPoke/Pokemon/imgs/Aggron.png")


class Beldum(Steel):
    def __init__(self):
        super().__init__("Beldum", 190, [
            Move("Mega Kick", "NORMAL", 120),
            Move("Thunder", "ELECTRIC", 120),
            Move("Psywave", "PSYCHIC", randint(30,150)),
            Move("Dream Eater", "PSYCHIC", 100)
        ], "./TVPoke/Pokemon/imgs/Beldum.png")


class Metang(Steel):
    def __init__(self):
        super().__init__("Metang", 191, [
            Move("Mega Kick", "NORMAL", 120),
            Move("Thunder", "ELECTRIC", 120),
            Move("Psywave", "PSYCHIC", randint(30,150)),
            Move("Dream Eater", "PSYCHIC", 100)
        ], "./TVPoke/Pokemon/imgs/Metang.png")


class Metagross(Steel):
    def __init__(self):
        super().__init__("Metagross", 192, [
            Move("Mega Kick", "NORMAL", 120),
            Move("Thunder", "ELECTRIC", 120),
            Move("Psywave", "PSYCHIC", randint(30,150)),
            Move("Dream Eater", "PSYCHIC", 100)
        ], "./TVPoke/Pokemon/imgs/Metagross.png")


class Registeel(Steel):
    def __init__(self):
        super().__init__("Registeel", 195, [
            Move("Mega Kick", "NORMAL", 120),
            Move("Thunder", "ELECTRIC", 120),
            Move("Psywave", "PSYCHIC", randint(30,150)),
            Move("Dream Eater", "PSYCHIC", 100)
        ], "./TVPoke/Pokemon/imgs/Registeel.png")
from TVPoke.BaseClasses.PokeTypes import Rock
from TVPoke.BaseClasses.Move import Move
from random import randint


class Geodude(Rock):
    def __init__(self):
        moves = [
            Move("Mega Kick", "NORMAL", 120),
            Move("Thunder", "ELECTRIC", 120),
            Move("Psywave", "PSYCHIC", randint(30, 150)),
            Move("Dream Eater", "PSYCHIC", 100)
        ]
        super().__init__("Geodude", 57, moves, "./TVPoke/Pokemon/imgs/Geodude.png")


class Graveler(Rock):
    def __init__(self):
        moves = [
            Move("Mega Kick", "NORMAL", 120),
            Move("Thunder", "ELECTRIC", 120),
            Move("Psywave", "PSYCHIC", randint(30, 150)),
            Move("Dream Eater", "PSYCHIC", 100)
        ]
        super().__init__("Graveler", 58, moves, "./TVPoke/Pokemon/imgs/Graveler.png")


class Golem(Rock):
    def __init__(self):
        moves = [
            Move("Mega Kick", "NORMAL", 120),
            Move("Thunder", "ELECTRIC", 120),
            Move("Psywave", "PSYCHIC", randint(30, 150)),
            Move("Dream Eater", "PSYCHIC", 100)
        ]
        super().__init__("Golem", 59, moves, "./TVPoke/Pokemon/imgs/Golem.png")


class Nosepass(Rock):
    def __init__(self):
        moves = [
            Move("Mega Kick", "NORMAL", 120),
            Move("Thunder", "ELECTRIC", 120),
            Move("Psywave", "PSYCHIC", randint(30, 150)),
            Move("Dream Eater", "PSYCHIC", 100)
        ]
        super().__init__("Nosepass", 60, moves, "./TVPoke/Pokemon/imgs/Nosepass.png")


class Magcargo(Rock):
    def __init__(self):
        moves = [
            Move("Mega Kick", "NORMAL", 120),
            Move("Thunder", "ELECTRIC", 120),
            Move("Psywave", "PSYCHIC", randint(30, 150)),
            Move("Dream Eater", "PSYCHIC", 100)
        ]
        super().__init__("Magcargo", 104, moves, "./TVPoke/Pokemon/imgs/Magcargo.png")


class Skarmory(Rock):
    def __init__(self):
        moves = [
            Move("Mega Kick", "NORMAL", 120),
            Move("Thunder", "ELECTRIC", 120),
            Move("Psywave", "PSYCHIC", randint(30, 150)),
            Move("Dream Eater", "PSYCHIC", 100)
        ]
        super().__init__("Skarmory", 115, moves, "./TVPoke/Pokemon/imgs/Skarmory.png")


class Lunatone(Rock):
    def __init__(self):
        moves = [
            Move("Mega Kick", "NORMAL", 120),
            Move("Thunder", "ELECTRIC", 120),
            Move("Psywave", "PSYCHIC", randint(30, 150)),
            Move("Dream Eater", "PSYCHIC", 100)
        ]
        super().__init__("Lunatone", 125, moves, "./TVPoke/Pokemon/imgs/Lunatone.png")


class Solrock(Rock):
    def __init__(self):
        moves = [
            Move("Mega Kick", "NORMAL", 120),
            Move("Thunder", "ELECTRIC", 120),
            Move("Psywave", "PSYCHIC", randint(30, 150)),
            Move("Dream Eater", "PSYCHIC", 100)
        ]
        super().__init__("Solrock", 126, moves, "./TVPoke/Pokemon/imgs/Solrock.png")


class Lileep(Rock):
    def __init__(self):
        moves = [
            Move("Mega Kick", "NORMAL", 120),
            Move("Thunder", "ELECTRIC", 120),
            Move("Psywave", "PSYCHIC", randint(30, 150)),
            Move("Dream Eater", "PSYCHIC", 100)
        ]
        super().__init__("Lileep", 133, moves, "./TVPoke/Pokemon/imgs/Lileep.png")


class Cradily(Rock):
    def __init__(self):
        moves = [
            Move("Mega Kick", "NORMAL", 120),
            Move("Thunder", "ELECTRIC", 120),
            Move("Psywave", "PSYCHIC", randint(30, 150)),
            Move("Dream Eater", "PSYCHIC", 100)
        ]
        super().__init__("Cradily", 134, moves, "./TVPoke/Pokemon/imgs/Cradily.png")


class Anorith(Rock):
    def __init__(self):
        moves = [
            Move("Mega Kick", "NORMAL", 120),
            Move("Thunder", "ELECTRIC", 120),
            Move("Psywave", "PSYCHIC", randint(30, 150)),
            Move("Dream Eater", "PSYCHIC", 100)
        ]
        super().__init__("Anorith", 135, moves, "./TVPoke/Pokemon/imgs/Anorith.png")


class Armaldo(Rock):
    def __init__(self):
        moves = [
            Move("Mega Kick", "NORMAL", 120),
            Move("Thunder", "ELECTRIC", 120),
            Move("Psywave", "PSYCHIC", randint(30, 150)),
            Move("Dream Eater", "PSYCHIC", 100)
        ]
        super().__init__("Armaldo", 136, moves, "./TVPoke/Pokemon/imgs/Armaldo.png")


class Relicanth(Rock):
    def __init__(self):
        moves = [
            Move("Mega Kick", "NORMAL", 120),
            Move("Thunder", "ELECTRIC", 120),
            Move("Psywave", "PSYCHIC", randint(30, 150)),
            Move("Dream Eater", "PSYCHIC", 100)
        ]
        super().__init__("Relicanth", 179, moves, "./TVPoke/Pokemon/imgs/Relicanth.png")


class Corsola(Rock):
    def __init__(self):
        moves = [
            Move("Mega Kick", "NORMAL", 120),
            Move("Thunder", "ELECTRIC", 120),
            Move("Psywave", "PSYCHIC", randint(30, 150)),
            Move("Dream Eater", "PSYCHIC", 100)
        ]
        super().__init__("Corsola", 180, moves, "./TVPoke/Pokemon/imgs/Corsola.png")


class Regirock(Rock):
    def __init__(self):
        moves = [
            Move("Mega Kick", "NORMAL", 120),
            Move("Thunder", "ELECTRIC", 120),
            Move("Psywave", "PSYCHIC", randint(30, 150)),
            Move("Dream Eater", "PSYCHIC", 100)
        ]
        super().__init__("Regirock", 193, moves, "./TVPoke/Pokemon/imgs/Regirock.png")
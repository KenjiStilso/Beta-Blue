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



class Lunatone(Rock):
    def __init__(self):
        super().__init__("Lunatone", 125, [
            Move("Mega Kick", "NORMAL", 120),
            Move("Thunder", "ELECTRIC", 120),
            Move("Psywave", "PSYCHIC", randint(30,150)),
            Move("Dream Eater", "PSYCHIC", 100)
        ], "./TVPoke/Pokemon/imgs/Lunatone.png")

class Solrock(Rock):
    def __init__(self):
        super().__init__("Solrock", 126, [
            Move("Mega Kick", "NORMAL", 120),
            Move("Thunder", "ELECTRIC", 120),
            Move("Psywave", "PSYCHIC", randint(30,150)),
            Move("Dream Eater", "PSYCHIC", 100)
        ], "./TVPoke/Pokemon/imgs/Solrock.png")

class Lileep(Rock):
    def __init__(self):
        super().__init__("Lileep", 133, [
            Move("Mega Kick", "NORMAL", 120),
            Move("Thunder", "ELECTRIC", 120),
            Move("Psywave", "PSYCHIC", randint(30,150)),
            Move("Dream Eater", "PSYCHIC", 100)
        ], "./TVPoke/Pokemon/imgs/Lileep.png")

class Cradily(Rock):
    def __init__(self):
        super().__init__("Cradily", 134, [
            Move("Mega Kick", "NORMAL", 120),
            Move("Thunder", "ELECTRIC", 120),
            Move("Psywave", "PSYCHIC", randint(30,150)),
            Move("Dream Eater", "PSYCHIC", 100)
        ], "./TVPoke/Pokemon/imgs/Cradily.png")

class Anorith(Rock):
    def __init__(self):
        super().__init__("Anorith", 135, [
            Move("Mega Kick", "NORMAL", 120),
            Move("Thunder", "ELECTRIC", 120),
            Move("Psywave", "PSYCHIC", randint(30,150)),
            Move("Dream Eater", "PSYCHIC", 100)
        ], "./TVPoke/Pokemon/imgs/Anorith.png")

class Regirock(Rock):
    def __init__(self):
        super().__init__("Regirock", 193, [
            Move("Mega Kick", "NORMAL", 120),
            Move("Thunder", "ELECTRIC", 120),
            Move("Psywave", "PSYCHIC", randint(30,150)),
            Move("Dream Eater", "PSYCHIC", 100)
        ], "./TVPoke/Pokemon/imgs/Regirock.png")


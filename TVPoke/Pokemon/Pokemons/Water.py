from TVPoke.BaseClasses.PokeTypes import Water
from TVPoke.BaseClasses.Move import Move
from random import randint


class Mudkip(Water):
    def __init__(self):
        moves = [
            Move("Mega Kick", "NORMAL", 120),
            Move("Thunder", "ELECTRIC", 120),
            Move("Psywave", "PSYCHIC", randint(30, 150)),
            Move("Dream Eater", "PSYCHIC", 100)
        ]
        super().__init__("Mudkip", 7, moves, "./TVPoke/Pokemon/imgs/Mudkip.png")


class Marshtomp(Water):
    def __init__(self):
        moves = [
            Move("Mega Kick", "NORMAL", 120),
            Move("Thunder", "ELECTRIC", 120),
            Move("Psywave", "PSYCHIC", randint(30, 150)),
            Move("Dream Eater", "PSYCHIC", 100)
        ]
        super().__init__("Marshtomp", 8, moves, "./TVPoke/Pokemon/imgs/Marshtomp.png")


class Swampert(Water):
    def __init__(self):
        moves = [
            Move("Mega Kick", "NORMAL", 120),
            Move("Thunder", "ELECTRIC", 120),
            Move("Psywave", "PSYCHIC", randint(30, 150)),
            Move("Dream Eater", "PSYCHIC", 100)
        ]
        super().__init__("Swampert", 9, moves, "./TVPoke/Pokemon/imgs/Swampert.png")


class Lotad(Water):
    def __init__(self):
        moves = [
            Move("Mega Kick", "NORMAL", 120),
            Move("Thunder", "ELECTRIC", 120),
            Move("Psywave", "PSYCHIC", randint(30, 150)),
            Move("Dream Eater", "PSYCHIC", 100)
        ]
        super().__init__("Lotad", 19, moves, "./TVPoke/Pokemon/imgs/Lotad.png")


class Lombre(Water):
    def __init__(self):
        moves = [
            Move("Mega Kick", "NORMAL", 120),
            Move("Thunder", "ELECTRIC", 120),
            Move("Psywave", "PSYCHIC", randint(30, 150)),
            Move("Dream Eater", "PSYCHIC", 100)
        ]
        super().__init__("Lombre", 20, moves, "./TVPoke/Pokemon/imgs/Lombre.png")


class Ludicolo(Water):
    def __init__(self):
        moves = [
            Move("Mega Kick", "NORMAL", 120),
            Move("Thunder", "ELECTRIC", 120),
            Move("Psywave", "PSYCHIC", randint(30, 150)),
            Move("Dream Eater", "PSYCHIC", 100)
        ]
        super().__init__("Ludicolo", 21, moves, "./TVPoke/Pokemon/imgs/Ludicolo.png")


class Wingull(Water):
    def __init__(self):
        moves = [
            Move("Mega Kick", "NORMAL", 120),
            Move("Thunder", "ELECTRIC", 120),
            Move("Psywave", "PSYCHIC", randint(30, 150)),
            Move("Dream Eater", "PSYCHIC", 100)
        ]
        super().__init__("Wingull", 27, moves, "./TVPoke/Pokemon/imgs/Wingull.png")


class Pelipper(Water):
    def __init__(self):
        moves = [
            Move("Mega Kick", "NORMAL", 120),
            Move("Thunder", "ELECTRIC", 120),
            Move("Psywave", "PSYCHIC", randint(30, 150)),
            Move("Dream Eater", "PSYCHIC", 100)
        ]
        super().__init__("Pelipper", 28, moves, "./TVPoke/Pokemon/imgs/Pelipper.png")


class Surskit(Water):
    def __init__(self):
        moves = [
            Move("Mega Kick", "NORMAL", 120),
            Move("Thunder", "ELECTRIC", 120),
            Move("Psywave", "PSYCHIC", randint(30, 150)),
            Move("Dream Eater", "PSYCHIC", 100)
        ]
        super().__init__("Surskit", 32, moves, "./TVPoke/Pokemon/imgs/Surskit.png")


class Goldeen(Water):
    def __init__(self):
        moves = [
            Move("Mega Kick", "NORMAL", 120),
            Move("Thunder", "ELECTRIC", 120),
            Move("Psywave", "PSYCHIC", randint(30, 150)),
            Move("Dream Eater", "PSYCHIC", 100)
        ]
        super().__init__("Goldeen", 50, moves, "./TVPoke/Pokemon/imgs/Goldeen.png")


class Seaking(Water):
    def __init__(self):
        moves = [
            Move("Mega Kick", "NORMAL", 120),
            Move("Thunder", "ELECTRIC", 120),
            Move("Psywave", "PSYCHIC", randint(30, 150)),
            Move("Dream Eater", "PSYCHIC", 100)
        ]
        super().__init__("Seaking", 51, moves, "./TVPoke/Pokemon/imgs/Seaking.png")


class Magikarp(Water):
    def __init__(self):
        moves = [
            Move("Mega Kick", "NORMAL", 120),
            Move("Thunder", "ELECTRIC", 120),
            Move("Psywave", "PSYCHIC", randint(30, 150)),
            Move("Dream Eater", "PSYCHIC", 100)
        ]
        super().__init__("Magikarp", 52, moves, "./TVPoke/Pokemon/imgs/Magikarp.png")


class Gyarados(Water):
    def __init__(self):
        moves = [
            Move("Mega Kick", "NORMAL", 120),
            Move("Thunder", "ELECTRIC", 120),
            Move("Psywave", "PSYCHIC", randint(30, 150)),
            Move("Dream Eater", "PSYCHIC", 100)
        ]
        super().__init__("Gyarados", 53, moves, "./TVPoke/Pokemon/imgs/Gyarados.png")


class Azurill(Water):
    def __init__(self):
        moves = [
            Move("Mega Kick", "NORMAL", 120),
            Move("Thunder", "ELECTRIC", 120),
            Move("Psywave", "PSYCHIC", randint(30, 150)),
            Move("Dream Eater", "PSYCHIC", 100)
        ]
        super().__init__("Azurill", 54, moves, "./TVPoke/Pokemon/imgs/Azurill.png")


class Marill(Water):
    def __init__(self):
        moves = [
            Move("Mega Kick", "NORMAL", 120),
            Move("Thunder", "ELECTRIC", 120),
            Move("Psywave", "PSYCHIC", randint(30, 150)),
            Move("Dream Eater", "PSYCHIC", 100)
        ]
        super().__init__("Marill", 55, moves, "./TVPoke/Pokemon/imgs/Marill.png")


class Azumarill(Water):
    def __init__(self):
        moves = [
            Move("Mega Kick", "NORMAL", 120),
            Move("Thunder", "ELECTRIC", 120),
            Move("Psywave", "PSYCHIC", randint(30, 150)),
            Move("Dream Eater", "PSYCHIC", 100)
        ]
        super().__init__("Azumarill", 56, moves, "./TVPoke/Pokemon/imgs/Azumarill.png")


class Tentacool(Water):
    def __init__(self):
        moves = [
            Move("Mega Kick", "NORMAL", 120),
            Move("Thunder", "ELECTRIC", 120),
            Move("Psywave", "PSYCHIC", randint(30, 150)),
            Move("Dream Eater", "PSYCHIC", 100)
        ]
        super().__init__("Tentacool", 66, moves, "./TVPoke/Pokemon/imgs/Tentacool.png")


class Tentacruel(Water):
    def __init__(self):
        moves = [
            Move("Mega Kick", "NORMAL", 120),
            Move("Thunder", "ELECTRIC", 120),
            Move("Psywave", "PSYCHIC", randint(30, 150)),
            Move("Dream Eater", "PSYCHIC", 100)
        ]
        super().__init__("Tentacruel", 67, moves, "./TVPoke/Pokemon/imgs/Tentacruel.png")


class Carvanha(Water):
    def __init__(self):
        moves = [
            Move("Mega Kick", "NORMAL", 120),
            Move("Thunder", "ELECTRIC", 120),
            Move("Psywave", "PSYCHIC", randint(30, 150)),
            Move("Dream Eater", "PSYCHIC", 100)
        ]
        super().__init__("Carvanha", 97, moves, "./TVPoke/Pokemon/imgs/Carvanha.png")


class Sharpedo(Water):
    def __init__(self):
        moves = [
            Move("Mega Kick", "NORMAL", 120),
            Move("Thunder", "ELECTRIC", 120),
            Move("Psywave", "PSYCHIC", randint(30, 150)),
            Move("Dream Eater", "PSYCHIC", 100)
        ]
        super().__init__("Sharpedo", 98, moves, "./TVPoke/Pokemon/imgs/Sharpedo.png")


class Wailmer(Water):
    def __init__(self):
        moves = [
            Move("Mega Kick", "NORMAL", 120),
            Move("Thunder", "ELECTRIC", 120),
            Move("Psywave", "PSYCHIC", randint(30, 150)),
            Move("Dream Eater", "PSYCHIC", 100)
        ]
        super().__init__("Wailmer", 99, moves, "./TVPoke/Pokemon/imgs/Wailmer.png")


class Wailord(Water):
    def __init__(self):
        moves = [
            Move("Mega Kick", "NORMAL", 120),
            Move("Thunder", "ELECTRIC", 120),
            Move("Psywave", "PSYCHIC", randint(30, 150)),
            Move("Dream Eater", "PSYCHIC", 100)
        ]
        super().__init__("Wailord", 100, moves, "./TVPoke/Pokemon/imgs/Wailord.png")


class Barboach(Water):
    def __init__(self):
        moves = [
            Move("Mega Kick", "NORMAL", 120),
            Move("Thunder", "ELECTRIC", 120),
            Move("Psywave", "PSYCHIC", randint(30, 150)),
            Move("Dream Eater", "PSYCHIC", 100)
        ]
        super().__init__("Barboach", 127, moves, "./TVPoke/Pokemon/imgs/Barboach.png")


class Whiscash(Water):
    def __init__(self):
        moves = [
            Move("Mega Kick", "NORMAL", 120),
            Move("Thunder", "ELECTRIC", 120),
            Move("Psywave", "PSYCHIC", randint(30, 150)),
            Move("Dream Eater", "PSYCHIC", 100)
        ]
        super().__init__("Whiscash", 128, moves, "./TVPoke/Pokemon/imgs/Whiscash.png")


class Corphish(Water):
    def __init__(self):
        moves = [
            Move("Mega Kick", "NORMAL", 120),
            Move("Thunder", "ELECTRIC", 120),
            Move("Psywave", "PSYCHIC", randint(30, 150)),
            Move("Dream Eater", "PSYCHIC", 100)
        ]
        super().__init__("Corphish", 129, moves, "./TVPoke/Pokemon/imgs/Corphish.png")


class Crawdaunt(Water):
    def __init__(self):
        moves = [
            Move("Mega Kick", "NORMAL", 120),
            Move("Thunder", "ELECTRIC", 120),
            Move("Psywave", "PSYCHIC", randint(30, 150)),
            Move("Dream Eater", "PSYCHIC", 100)
        ]
        super().__init__("Crawdaunt", 130, moves, "./TVPoke/Pokemon/imgs/Crawdaunt.png")


class Feebas(Water):
    def __init__(self):
        moves = [
            Move("Mega Kick", "NORMAL", 120),
            Move("Thunder", "ELECTRIC", 120),
            Move("Psywave", "PSYCHIC", randint(30, 150)),
            Move("Dream Eater", "PSYCHIC", 100)
        ]
        super().__init__("Feebas", 140, moves, "./TVPoke/Pokemon/imgs/Feebas.png")


class Milotic(Water):
    def __init__(self):
        moves = [
            Move("Mega Kick", "NORMAL", 120),
            Move("Thunder", "ELECTRIC", 120),
            Move("Psywave", "PSYCHIC", randint(30, 150)),
            Move("Dream Eater", "PSYCHIC", 100)
        ]
        super().__init__("Milotic", 141, moves, "./TVPoke/Pokemon/imgs/Milotic.png")


class Staryu(Water):
    def __init__(self):
        moves = [
            Move("Mega Kick", "NORMAL", 120),
            Move("Thunder", "ELECTRIC", 120),
            Move("Psywave", "PSYCHIC", randint(30, 150)),
            Move("Dream Eater", "PSYCHIC", 100)
        ]
        super().__init__("Staryu", 143, moves, "./TVPoke/Pokemon/imgs/Staryu.png")


class Starmie(Water):
    def __init__(self):
        moves = [
            Move("Mega Kick", "NORMAL", 120),
            Move("Thunder", "ELECTRIC", 120),
            Move("Psywave", "PSYCHIC", randint(30, 150)),
            Move("Dream Eater", "PSYCHIC", 100)
        ]
        super().__init__("Starmie", 144, moves, "./TVPoke/Pokemon/imgs/Starmie.png")


class Psyduck(Water):
    def __init__(self):
        moves = [
            Move("Mega Kick", "NORMAL", 120),
            Move("Thunder", "ELECTRIC", 120),
            Move("Psywave", "PSYCHIC", randint(30, 150)),
            Move("Dream Eater", "PSYCHIC", 100)
        ]
        super().__init__("Psyduck", 158, moves, "./TVPoke/Pokemon/imgs/Psyduck.png")


class Golduck(Water):
    def __init__(self):
        moves = [
            Move("Mega Kick", "NORMAL", 120),
            Move("Thunder", "ELECTRIC", 120),
            Move("Psywave", "PSYCHIC", randint(30, 150)),
            Move("Dream Eater", "PSYCHIC", 100)
        ]
        super().__init__("Golduck", 159, moves, "./TVPoke/Pokemon/imgs/Golduck.png")
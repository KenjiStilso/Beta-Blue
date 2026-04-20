import os
import sys

this_dir = os.path.dirname(os.path.abspath(__file__))
tvpoke_root = os.path.join(this_dir, "TVPoke")
if tvpoke_root not in sys.path:
    sys.path.insert(0, tvpoke_root)

from PyUI.Window import Window
from PyUI.Examples.StartScreen import StartScreen
from PyUI.Examples.VillageScreen import VillageScreen
import pygame


def main():
    window = Window("Beta-Blue", (120, 184, 255))
    start = StartScreen(window)
    screen = start
    clock = pygame.time.Clock()

    while True:
        window.checkForInput(screen)

        if hasattr(screen, "next_screen") and screen.next_screen:
            screen = screen.next_screen

        window.update(screen)
        clock.tick(60)


if __name__ == "__main__":
    main()

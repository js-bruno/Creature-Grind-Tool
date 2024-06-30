from random import choice
from time import sleep

from creature_core.domain.adapter import GameInput


class FindBattle:
    def __init__(self, game_input: GameInput):
        self._autogui = game_input
        self.moviment_keys = ["w", "s", "a", "d"]

    def run(self):
        self._autogui.moving_in_square(1)
        sleep(0.5)

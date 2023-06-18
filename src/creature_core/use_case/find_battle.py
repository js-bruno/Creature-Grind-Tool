from time import sleep
from creature_core.domain.adapter import Autogui
from random import choice


class FindBattle:
    def __init__(self, autogui: Autogui):
        self._autogui = autogui
        self.moviment_keys = ["w", "s", "a", "d"]

    def run(self):
        self._autogui.keyDown(choice(self.moviment_keys))
        sleep(1)
        self._autogui.keyUp(choice(self.moviment_keys))
        self._autogui.press(self.moviment_keys)

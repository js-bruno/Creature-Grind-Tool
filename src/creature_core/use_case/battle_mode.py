from random import choice
from creature_core.domain.adapter import Autogui
from creature_core.domain.file_storage import ImageStorage
from time import sleep


class BattleMode:
    def __init__(self, autogui: Autogui, image_storage: ImageStorage):
        self._autogui = autogui
        self._image_storage = image_storage

    def run(self):
        in_battle = self._autogui.locateOnScreen(image=self._image_storage.hp_label_battle_image(), grayscale=True)
        while in_battle != None:
            self._open_attack_menu()
            sleep(1)
            self._attack_with_efficient_move()
            in_battle = self._autogui.locateOnScreen(image=self._image_storage.hp_label_battle_image(), grayscale=True)
        return False

    def _open_attack_menu(self):
        self._autogui.press(["a", "w"])
        self._autogui.press(["a", "w"])
        self._autogui.press("z")

    def _attack_with_efficient_move(self):
        # super_effetive_move = self._autogui.locateOnScreen(self._image_storage.load_super_effetive_image())
        # if super_effetive_move != None:
        #     left_pos, top_pos = super_effetive_move
        #     self._autogui.click([left_pos, top_pos])
        #     return True
        self._battle_move([1, 2, 3, 4])
        # return False

    def _battle_move(self, random_move: list):
        move = choice(random_move)
        if move == 1:
            self._autogui.press(["a", "w"])
        elif move == 2:
            self._autogui.press(["d", "w"])
        elif move == 3:
            self._autogui.press(["a", "s"])
        elif move == 4:
            self._autogui.press(["s", "d"])

        self._autogui.press(["z", "z"])

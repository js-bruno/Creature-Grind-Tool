# CRIAR ADAPTERS PARA BIBLIOTECAS ABAIXO.
from time import sleep

from PIL import Image

from creature_core.domain.adapter import Autogui, OpticalRecognition, GameInput
from creature_core.domain.file_storage import ImageStorage


class FirstPartyCreatureIsAlive:
    def __init__(
        self,
        game_input: GameInput,
        autogui: Autogui,
        optical_recognition: OpticalRecognition,
        image_storage: ImageStorage,
    ):
        self._autogui = autogui
        self._optical_recognition = optical_recognition
        self._image_storage = image_storage
        self._game_input = game_input

        self._hp_modal_image: Image = image_storage.health_points_label_modal()
        self._close_modal_image: Image = image_storage.load_close_modal_image()

    def run(self):
        sleep(300 / 1000)
        hp_creature_int = self._game_input.find_and_print_creature_health_points(0)

        if hp_creature_int > 0:
            return True
        return False

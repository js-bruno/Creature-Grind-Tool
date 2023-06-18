# CRIAR ADAPTERS PARA BIBLIOTECAS ABAIXO.
from time import sleep
from PIL import Image

from creature_core.domain.adapter import OpticalRecognition, Autogui
from creature_core.domain.file_storage import ImageStorage


class FirstPartyCreatureIsAlive:
    def __init__(
        self,
        autogui: Autogui,
        optical_recognition: OpticalRecognition,
        image_storage: ImageStorage,
    ):
        self._autogui = autogui
        self._optical_recognition = optical_recognition

        self._hp_modal_image: Image = image_storage.load_hp_modal_image()
        self._close_modal_image: Image = image_storage.load_close_modal_image()

    def run(self):
        self.__open_dialog()
        sleep(300 / 1000)

        cordenates: list[int] = self._print_and_find_creature_modal()
        # UseTempFiles Insted save
        hp_creature_print = self._autogui.screenshot(cordenates)
        hp_creature_print.save("creature_modal.png")

        self.__close_dialog()
        hp_creature_data = self._optical_recognition.image_to_string(
            Image.open("creature_modal.png")
        )
        hp_creature_int = int(hp_creature_data.split("/")[0])

        if hp_creature_int > 0:
            return True
        elif hp_creature_int == 0:
            return False
        else:
            raise Exception()

    def __open_dialog(self):
        self._autogui.press("k")
        for _ in range(4):
            self._autogui.press("z")
        self._autogui.press("d")
        self._autogui.press("d")
        self._autogui.press("d")

    def __close_dialog(self):
        self._autogui.press("x")
        self._autogui.press("x")
        self._autogui.press("x")
        # self._autogui.locateAndClick(self._close_modal_image, 0.9)

    def _print_and_find_creature_modal(self) -> list[int]:
        # actual_screen_shot = self._autogui.screenshot()
        # dialog_hp_modal = Image.open("./src/creature_core/repository/images/dialog_HP.png")
        # cordenates = self._autogui.locateOnScreen(
        #     Image.open("./src/creature_core/repository/images/dialog_HP.png"), confidence=0.9
        # )
        cordenates = self._autogui.locateOnScreen(self._hp_modal_image, confidence=0.9)
        left, top, width, heigh = cordenates
        new_cords = []
        new_cords.append(left + 110)
        new_cords.append(top + 11)
        new_cords.append(width - 45)
        new_cords.append(heigh - 20)
        return new_cords

import pyautogui
from PIL import Image, ImageEnhance
from time import sleep

import pytesseract

pyautogui.FAILSAFE = True


class PyAutoGuiGameInput:
    def __init__(self, image_storage):
        self._image_storage = image_storage
        self._optical_recognition = pytesseract

    def find_and_print_creature_health_points(self, creature_position: int) -> int:
        self._open_creature_summary(creature_position)

        new_cords = self._get_cordenates_from_health_points()
        health_points_screenshot = pyautogui.screenshot(region=new_cords)
        health_points_screenshot.save("creature_modal.png")

        self._close_creature_summary()

        hp_creature_data = self.enhance_image_to_string(Image.open("creature_modal.png"))
        hp_creature_int = int(hp_creature_data.split("/")[0])
        return hp_creature_int

    def moving_in_square(self, size: int):
        # self._autogui.keyDown(choice(self.moviment_keys))
        # self._autogui.keyUp(choice(self.moviment_keys))
        # self._autogui.press(self.moviment_keys)

        pyautogui.keyDown("a")
        sleep(0.3)
        pyautogui.keyUp("a")
        sleep(0.3)

        pyautogui.keyDown("w")
        sleep(0.3)
        pyautogui.keyUp("w")
        sleep(0.3)

        pyautogui.keyDown("d")
        sleep(0.3)
        pyautogui.keyUp("d")
        sleep(0.3)

        pyautogui.keyDown("s")
        sleep(0.3)
        pyautogui.keyUp("s")
        sleep(0.3)
        
    def enhance_image_to_string(self, image):
        bright = ImageEnhance.Brightness(image)
        image = bright.enhance(1.5)

        constraster = ImageEnhance.Contrast(image)
        image = constraster.enhance(1.5)

        sharpner = ImageEnhance.Sharpness(image)
        image = sharpner.enhance(1.5)
        txt = self._optical_recognition.image_to_string(image, config='--psm 3')
        return txt

    def _open_creature_summary(self, creature_position: int):
        pyautogui.press("k")
        for _ in range(4):
            pyautogui.press("z")
        pyautogui.press("d")
        pyautogui.press("d")
        pyautogui.press("d")

    def _close_creature_summary(self):
        pyautogui.press("x")
        pyautogui.press("x")
        pyautogui.press("x")

    def _get_cordenates_from_health_points(self):
        cordenates = pyautogui.locateOnScreen(self._image_storage.health_points_label_modal(), confidence=0.9)
        left, top, width, heigh = cordenates

        new_cords = []
        new_cords.append(left + 110)
        new_cords.append(top + 0)
        new_cords.append(width - 30)
        new_cords.append(heigh + 0)
        return new_cords

    def _set_character_default_position(self):
        pyautogui.press("s")

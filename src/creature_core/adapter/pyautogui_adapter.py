import pyautogui

from creature_core.domain.adapter import Autogui


class PyAutoGuiAdapter(Autogui):
    def press(self, *args):
        return pyautogui.press(*args)

    def screenshot(self, coordenates: list = None):
        return pyautogui.screenshot(region=coordenates)

    def locateOnScreen(self, *args, **kargs):
        return pyautogui.locateOnScreen(*args, **kargs)

    def locateHpDialog(self) -> list:
        return pyautogui.locateOnScreen()

    def locate(self, *args):
        return pyautogui.locate(*args)

    def keyDown(self, *args):
        return pyautogui.keyDown(*args)

    def keyUp(self, *args):
        return pyautogui.keyUp(*args)

    def locateAndClick(self, img, confidence: float):
        try:
            # USE REGION TO FIND THE IMAGE WITH BETTER PRESICION
            cordenates = pyautogui.locate(img, confidence)
            x, y = cordenates
        except Exception:
            raise Exception("Not Find Image")

        return pyautogui.click(x, y)

    def click(self, *args):
        return pyautogui.click(*args)

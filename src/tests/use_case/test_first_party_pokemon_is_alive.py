import pytest
from PIL import Image
import pyautogui

from creature_core.use_case import FirstPartyCreatureIsAlive
from creature_core.adapter import PyAutoGuiAdapter, PytesseractAdapter


@pytest.fixture
def use_case():
    return FirstPartyCreatureIsAlive(
        autogui=PyAutoGuiAdapter(), optical_recognition=PytesseractAdapter()
    )


@pytest.fixture
def cordenates():
    return [470, 301, 64, 15]


@pytest.fixture
def locate_on_print():
    return pyautogui.locate(
        Image.open("src/creature_core/repository/images/dialog_HP.png"),
        Image.open("src/tests/mock_prints/hp_creature_modal.png"),
    )


@pytest.fixture
def mock_image(mocker, cordenates, locate_on_print):
    modal_cordenates = mocker.patch(
        "creature_core.use_case.FirstPartyCreatureIsAlive._define_modal_cordenates"
    )
    modal_cordenates.return_value = cordenates

    locate_on_screen = mocker.patch("pyscreeze.locateOnScreen.screenshotIm")
    locate_on_screen.return_value = locate_on_print


def test_pytest_run(use_case):
    use_case.run()

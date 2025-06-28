import time
from creature_core.adapter import PyAutoGuiAdapter, PytesseractAdapter, PyAutoGuiGameInput
from creature_core.domain.exceptions import FirstPartyCreatureFaintedException
from creature_core.image_storage import PillowImageStorage
from creature_core.use_case import FirstPartyCreatureIsAlive


def instance_usecase():
    autogui_adapter = PyAutoGuiAdapter()
    optical_recognition_adapter = PytesseractAdapter()
    image_storage = PillowImageStorage()
    game_input = PyAutoGuiGameInput(image_storage)

    first_party_creature_is_alive_use_case = FirstPartyCreatureIsAlive(
        game_input, autogui_adapter, optical_recognition_adapter, image_storage
    )
    time.sleep(3)
    response: bool = first_party_creature_is_alive_use_case.run()
    print(response)


if __name__ == "__main__":
    instance_usecase()

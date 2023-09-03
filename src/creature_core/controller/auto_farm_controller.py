from time import sleep
from creature_core.domain.exceptions import (
    FirstPartyCreatureFaintedException
)
from creature_core.adapter import PyAutoGuiAdapter, PytesseractAdapter
from creature_core.use_case import FirstPartyCreatureIsAlive, FindBattle, BattleMode
from creature_core.image_storage import PillowImageStorage


class AutoFarmController:
    def __init__(self) -> None:
        pass

    def auto_farm_start():
        sleep(2)
        # TODO: find some linux lib to manipule xfce interface
        # find_window_use_case = FindAppWindow()
        # try:
        #     find_window_use_case.run()
        # except:
        #     raise WindowAppNotFind()
        autogui_adapter = PyAutoGuiAdapter()
        optical_recognition_adapter = PytesseractAdapter()
        image_storage = PillowImageStorage()

        first_party_creature_is_alive_use_case = FirstPartyCreatureIsAlive(
            autogui_adapter, optical_recognition_adapter, image_storage
        )
        find_battle = FindBattle(autogui_adapter)

        first_creature_defeated = first_party_creature_is_alive_use_case.run()
        battle_mode = BattleMode(autogui_adapter, image_storage)

        if not first_creature_defeated:
            raise FirstPartyCreatureFaintedException()

        while True:
            # first_party_creature_is_alive: bool = first_party_creature_is_alive_use_case.run()

            # if not first_party_creature_is_alive:
            #     raise FirstPartyCreatureFaintedException()
            find_battle.run()
            in_battle: bool = battle_mode.run()

            if in_battle:
                is_alive = first_party_creature_is_alive_use_case.run()
                print(f"Creature is alive{is_alive}")
                if not first_creature_defeated:
                    raise FirstPartyCreatureFaintedException()

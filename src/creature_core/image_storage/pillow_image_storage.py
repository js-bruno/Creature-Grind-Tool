from pathlib import Path

from PIL import Image

from creature_core.domain.file_storage import ImageStorage
from creature_core.settings import get_settings


class PillowImageStorage(ImageStorage):
    def __init__(self):
        self._settings = get_settings()
        self._image_storage_path = Path(self._settings.IMAGE_LOCAL_STORAGE)

    def health_points_label_modal(self) -> Image:
        hp_modal_image_path = self._image_storage_path / "dialog_HP.png"
        print(hp_modal_image_path)
        return Image.open(hp_modal_image_path)

    def load_close_modal_image(self) -> Image:
        close_modal_path = self._image_storage_path / "close_modal.png"
        return Image.open(close_modal_path)

    def hp_label_battle_image(self) -> Image:
        fight_button_path = self._image_storage_path / "hp_battle.png"
        # import pdb; pdb.set_trace()
        return Image.open(fight_button_path)

    def load_super_effetive_image(self) -> Image:
        super_effetive_path = self._image_storage_path / "super_effective_battle.png"
        return Image.open(super_effetive_path)

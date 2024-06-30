import os
from dataclasses import dataclass

from dotenv import load_dotenv


def get_settings():
    load_dotenv()
    # TODO: try a better way to get envs.
    IMAGE_LOCAL_STORAGE = os.getenv("IMAGE_LOCAL_STORAGE")
    settings = Settings(IMAGE_LOCAL_STORAGE)
    return settings


@dataclass
class Settings:
    IMAGE_LOCAL_STORAGE: str = "./src/creature_core/repository/images/"

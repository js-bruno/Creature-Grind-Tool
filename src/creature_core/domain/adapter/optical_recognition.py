from abc import ABC, abstractmethod


class OpticalRecognition(ABC):
    @abstractmethod
    def image_to_string(*args):
        ...

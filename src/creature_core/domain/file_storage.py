import abc


class ImageStorage(abc.ABC):
    @abc.abstractmethod
    def health_points_label_modal():
        ...

    @abc.abstractmethod
    def load_close_modal_image():
        ...

    @abc.abstractmethod
    def hp_label_battle_image():
        ...

    @abc.abstractmethod
    def load_super_effetive_image():
        ...

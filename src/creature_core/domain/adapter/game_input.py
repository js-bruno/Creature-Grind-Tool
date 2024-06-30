import abc


class GameInput(abc.ABC):
    @abc.abstractmethod
    def open_creature_summary(self, creature_position: int):
        pass

    @abc.abstractmethod
    def close_creature_summary(self):
        pass

    @abc.abstractmethod
    def find_and_print_creature_health_points(self, creature_position: int) -> int:
        pass

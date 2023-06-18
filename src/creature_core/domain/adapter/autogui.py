import abc


class Autogui(abc.ABC):
    @abc.abstractmethod
    def press(*args):
        ...

    @abc.abstractmethod
    def keyDown(*args):
        ...

    @abc.abstractmethod
    def keyUp(*args):
        ...

    @abc.abstractmethod
    def screenshot(*args):
        ...

    @abc.abstractmethod
    def locateOnScreen(*args):
        ...

    @abc.abstractmethod
    def locate(*args):
        ...

    @abc.abstractmethod
    def locateAndClick(img, *, confidence: float):
        ...

    @abc.abstractmethod
    def click(self, *args):
        ...

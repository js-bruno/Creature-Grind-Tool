class PokeCoreBaseException(Exception):
    message = None

    def __init__(self, message=None) -> None:
        self.message = message or self.message
        super().__init__(self.message)


class WindowAppNotFind(PokeCoreBaseException):
    message = "The running application was not find"


class FirstPartyCreatureFaintedException(PokeCoreBaseException):
    message = "First Creature of the party is unconscious"

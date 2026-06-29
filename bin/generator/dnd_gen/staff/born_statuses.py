from abc import ABC
from collections.abc import Callable

class BirthStatus(ABC):
    def __init__(self, name: str):
        self.__name = name

    @property
    def name(self) -> str:
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

class Outcast(BirthStatus):
    def __init__(self):
        super().__init__("Раб, изгой или беспризорник")

class Peasant(BirthStatus):
    def __init__(self):
        super().__init__("Холоп или крестьянин")

class Artisan(BirthStatus):
    def __init__(self):
        super().__init__("Ремесленник или горожанин")

class Wealthy(BirthStatus):
    def __init__(self):
        super().__init__("Богатая семья или чиновники")

class Noble(BirthStatus):
    def __init__(self):
        super().__init__("Дворянство")

BIRTH_STATUS_TABLE: dict[int, Callable[[], BirthStatus]] = {
    2: Outcast,
    3: Peasant,
    4: Peasant,
    5: Peasant,
    6: Peasant,
    7: Peasant,
    8: Artisan,
    9: Artisan,
    10: Wealthy,
    11: Wealthy,
    12: Noble,
}
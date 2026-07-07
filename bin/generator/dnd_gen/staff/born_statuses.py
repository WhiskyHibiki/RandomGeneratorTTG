from abc import ABC
from collections.abc import Callable
from generator.dnd_gen.staff.born_feats import BornFeat, ArcaneBornFeat

class BirthStatus(ABC):
    def __init__(self, name: str, result: int):
        self.__status_roll: int = result
        self.__status_name: str = name

        self.__birth_feats_result:          int = 0
        self.__birth_feats_list:   list[ BornFeat | ArcaneBornFeat] = []

    @property
    def status_name(self) -> str:
        return self.__status_name
    @status_name.setter
    def status_name(self, name: str):
        self.__status_name = name

    @property
    def birth_feats_list(self) -> list[ BornFeat | ArcaneBornFeat]:
        return self.__birth_feats_list

    @property
    def status_roll(self) -> int:
        return self.__status_roll
    @property
    def birth_feats_roll(self) -> int:
        return self.__birth_feats_result

    def birth_feats_result(self, result: int) -> None:
        self.__birth_feats_result = result

    def __repr__(self):
        return self.__status_name


class Outcast(BirthStatus):
    def __init__(self, result: int):
        super().__init__("Раб, изгой или беспризорник", result)

class Peasant(BirthStatus):
    def __init__(self, result: int):
        super().__init__("Холоп или крестьянин", result)

class Artisan(BirthStatus):
    def __init__(self, result: int):
        super().__init__("Ремесленник или горожанин", result)

class Wealthy(BirthStatus):
    def __init__(self, result: int):
        super().__init__("Богатая семья или чиновники", result)

class Noble(BirthStatus):
    def __init__(self, result: int):
        super().__init__("Дворянство", result)


BIRTH_STATUS_TABLE: dict[int, Callable[[int], BirthStatus]] = {
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

BIRTH_FEATS_TABLE: dict[int, tuple[int, int]] = {
    2:  (0, 3),
    3:  (1, 3),
    4:  (1, 2),
    5:  (1, 2),
    6:  (1, 1),
    7:  (1, 1),
    8:  (1, 1),
    9:  (2, 1),
    10: (2, 1),
    11: (3, 1),
    12: (3, 0),
}

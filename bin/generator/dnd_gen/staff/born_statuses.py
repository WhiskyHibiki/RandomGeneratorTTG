from abc import ABC
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


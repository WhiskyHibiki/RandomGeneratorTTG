import random
from staff.born_statuses import BIRTH_STATUS_TABLE as BIRTH_STATUS_TABLE
from staff.born_statuses import BirthStatus

class DndNpcGenerator:
    def __init__(self):
        self.__stage_birth_table = BIRTH_STATUS_TABLE

    @staticmethod
    def roll_dices() -> int:
       result = random.randint(1,6) + random.randint(1,6)
       return result

    @property
    def stage_birth_table(self):
        return self.__stage_birth_table

    @property
    def stage_birth_generate(self) -> dict[str, BirthStatus]:
        return {'birth' : self.__stage_birth_generate()}

    def __stage_birth_generate(self) -> BirthStatus:
        result = self.stage_birth_table[DndNpcGenerator.roll_dices()]()
        return result




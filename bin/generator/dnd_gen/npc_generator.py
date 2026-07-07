from generator.dnd_gen.stages.stage_birth.born_statuses import BirthStatus
from generator.dnd_gen.stages.stage_birth.birth_stage import BirthStageGenerator

class DndNpcGenerator:
    def __init__(self):
        self.__birth_stage = BirthStageGenerator()

    def stage_birth_generate(self) -> dict[str, BirthStatus]:
        return self.__birth_stage.generate()



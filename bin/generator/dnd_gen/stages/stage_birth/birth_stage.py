import random

from generator.dnd_gen.stages.stage_birth.born_statuses import (
    BIRTH_STATUS_TABLE,
    BIRTH_FEATS_TABLE,
    BirthStatus,
)
from generator.dnd_gen.stages.stage_birth.born_feats import (
    FEATS_TABLE,
    ARCANE_PROPERTIES_FEATS_KEY,
    CreatorBirthFeat,
)

class BirthStageGenerator:
    @staticmethod
    def roll_2d6() -> int:
        return random.randint(1, 6) + random.randint(1, 6)

    def generate(self) -> dict[str, BirthStatus]:
        return {
            "birth_obj": self.__generate_birth_status()
        }

    def __generate_birth_status(self) -> BirthStatus:
        status_roll = self.roll_2d6()
        birth_status = BIRTH_STATUS_TABLE[status_roll](status_roll)

        feats_roll = self.roll_2d6()
        birth_status.birth_feats_result(feats_roll)

        feats = BIRTH_FEATS_TABLE[feats_roll]
        bonus = 1

        for count_feat in feats:
            for _ in range(count_feat):
                if 10 <= self.roll_2d6() <= 12:
                    feats_dict = ARCANE_PROPERTIES_FEATS_KEY
                    feat_creator = CreatorBirthFeat.create_feat(feats_dict)
                else:
                    feats_dict = FEATS_TABLE[random.randint(1, len(FEATS_TABLE))]
                    feat_creator = CreatorBirthFeat.create_feat(feats_dict[1])

                feat = feat_creator(feats_dict, bonus)
                birth_status.birth_feats_list.append(feat)

            bonus = -bonus

        return birth_status
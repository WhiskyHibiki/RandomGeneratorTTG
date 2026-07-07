import random
from dataclasses import dataclass

from generator.dnd_gen.stages.stage_birth.birth_statuses import (
    BIRTH_STATUS_TABLE,
    BIRTH_FEATS_TABLE,
    BirthStatus,
)
from generator.dnd_gen.stages.stage_birth.birth_feats import CreatorBirthFeat, FeatSlotKind, GIFT_SLOT, CURSE_SLOT

@dataclass
class BirthFeatGroup:
    slot_kind: FeatSlotKind
    count_feat: int
    bonus_sign: int

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
        gift_count, curse_count = BIRTH_FEATS_TABLE[feats_roll]

        feat_groups: tuple[BirthFeatGroup, ...] = (
            BirthFeatGroup(slot_kind=GIFT_SLOT, count_feat=gift_count, bonus_sign=1),
            BirthFeatGroup(slot_kind=CURSE_SLOT, count_feat=curse_count, bonus_sign=-1),
        )

        for feat_group in feat_groups:
            for _ in range(feat_group.count_feat):
                feat_roll = self.roll_2d6()

                feat = CreatorBirthFeat.create_birth_feat(
                    slot_kind=feat_group.slot_kind,
                    feat_roll=feat_roll,
                    bonus=feat_group.bonus_sign,
                )

                birth_status.birth_feats_list.append(feat)

        return birth_status
import random

from dataclasses import dataclass
from typing import Literal
from collections.abc import Callable
from abc import ABC

from generator.dnd_gen.PARAMETRS import PHYSICAL_PROPERTIES_FEATS_BONUSES
from generator.dnd_gen.stages.stage_birth.staff.birth_parameters import (FeatType, STAT_FEATS, PHYSICAL_PROPERTIES_FEATS,
                                                                         ARCANE_PROPERTIES_FEATS_KEY,
                                                                         ARCANE_PROPERTIES_FEATS_FEATURE, SKILL_FEATS,
                                                                         LEGENDARY_BIRTH_FEATS_DATA,
                                                                         SUPER_CURSE_BIRTH_FEATS_DATA)

FeatSlotKind = Literal["gift", "curse"]
GIFT_SLOT: FeatSlotKind = "gift"
CURSE_SLOT: FeatSlotKind = "curse"

class BirthFeatBase(ABC):
    name: str
    description: str
    kind: str


@dataclass(frozen=True)
class BirthBaseFeatClass(BirthFeatBase):
    target: str
    bonus: int

    @property
    def effect_name(self) -> str:
        sign = "+" if self.bonus > 0 else ""
        return f"{self.target.replace('_', ' ').title()} {sign}{self.bonus}"

    @property
    def effect_description(self) -> str:
        return (
            f"Upon creation, the character receives "
            f"a {self.bonus:+} bonus to "
            f"{self.target.replace('_', ' ').title()}."
        )

@dataclass(frozen=True)
class ArcaneBirthFeat(BirthBaseFeatClass):
    name: str
    target_type: FeatType
    target: str
    bonus: int | None
    uses: int | None
    recharge: str | None
    description: str
    kind: str = "arcane"

    def __repr__(self) -> str:
        return f"ArcaneBirthFeat({self.name})"

@dataclass(frozen=True)
class BirthFeat(BirthBaseFeatClass):
    name: str
    target_type: FeatType
    description: str
    kind: str = "mechanical"

    def __repr__(self) -> str:
        return f"BirthFeat({self.name})"


class CreatorBirthFeat:

    @staticmethod
    def create_birth_feat(slot_kind: FeatSlotKind, feat_roll: int, bonus: int) -> BirthFeatBase:
        if slot_kind == "gift" and feat_roll == 12:
            feat_data = LEGENDARY_BIRTH_FEATS_DATA[
                random.randint(1, len(LEGENDARY_BIRTH_FEATS_DATA))
            ]
            return CreatorBirthFeat.create_special_feat(feat_data)

        if slot_kind == "curse" and feat_roll == 2:
            feat_data = SUPER_CURSE_BIRTH_FEATS_DATA[
                random.randint(1, len(SUPER_CURSE_BIRTH_FEATS_DATA))
            ]
            return CreatorBirthFeat.create_special_feat(feat_data)

        if 10 <= feat_roll <= 12:
            feats_dict = ARCANE_PROPERTIES_FEATS_KEY
            feat_creator = CreatorBirthFeat.create_feat(feats_dict)
            return feat_creator(feats_dict, bonus)

        feats_dict = FEATS_TABLE[random.randint(1, len(FEATS_TABLE))]
        feat_creator = CreatorBirthFeat.create_feat(feats_dict[1])
        return feat_creator(feats_dict, bonus)

    @staticmethod
    def calculate_bonus(target_type: str, target: str, bonus_sign: int) -> int:
        if target_type == "physical":
            return PHYSICAL_PROPERTIES_FEATS_BONUSES[target] * bonus_sign

        return bonus_sign

    @staticmethod
    def create_special_feat(feat_data: dict) -> SpecialBirthFeat:
        return SpecialBirthFeat(**feat_data)

    @staticmethod
    def create_feat(arg_dict: dict[int, str]) -> Callable[[str, int], BirthFeat | dict[str, str], ArcaneBirthFeat]:
        if arg_dict is STAT_FEATS or arg_dict is SKILL_FEATS or arg_dict is PHYSICAL_PROPERTIES_FEATS:
            return CreatorBirthFeat.create_feat_by_type
        if arg_dict is ARCANE_PROPERTIES_FEATS_KEY:
            return CreatorBirthFeat.create_arcana_feat

        raise ValueError(f"Unknown feat table: {arg_dict}")

    @staticmethod
    def create_feat_by_type(feat_table: tuple[FeatType, dict[int, str]], bonus: int) -> BirthFeat:
        feat_type, feat_dict = feat_table
        target = feat_dict[random.randint(1, len(feat_dict))]

        formatted_target = target.replace("_", " ").title()

        real_bonus = CreatorBirthFeat.calculate_bonus(target_type=feat_type, target=target, bonus_sign=bonus)

        return BirthFeat(
            name=(
                f"{'Gift' if real_bonus > 0 else 'Curse'} "
                f"of {formatted_target}"
            ),
            target_type=feat_type,
            target=target,
            bonus=real_bonus,
            description=(
                f"Upon creation, the character receives "
                f"a {real_bonus:+} bonus to {formatted_target}."
            )
        )

    @staticmethod
    def create_arcana_feat(arcana_name: dict[int, str], bonus: int) -> ArcaneBirthFeat:
        arcana_dict = ARCANE_PROPERTIES_FEATS_FEATURE[arcana_name[random.randint(1, len(arcana_name))]]
        return ArcaneBirthFeat(
            name=arcana_dict["arcana_name"],
            target_type="arcana",
            target= arcana_dict["arcana_name"],
            bonus= bonus,
            uses= None,
            recharge= None,
            description=arcana_dict["arcana_description"]
        )

@dataclass(frozen=True)
class SpecialBirthFeat(BirthFeatBase):
    tag: str
    name: str
    kind: str
    description: str
    influence_tags: tuple[str, ...] = ()

    def __repr__(self) -> str:
        return f"SpecialBirthFeat({self.name})"


SPECIAL_FEATS_TABLE: dict[int, tuple[FeatType, dict[int, str]]] = {
    1: ("arcana", ARCANE_PROPERTIES_FEATS_KEY),
}

FEATS_TABLE: dict[int, tuple[FeatType, dict[int, str]]] = {
    1: ("stat", STAT_FEATS),
    2: ("skill", SKILL_FEATS),
    3: ("physical", PHYSICAL_PROPERTIES_FEATS),
}
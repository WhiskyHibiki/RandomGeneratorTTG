from dataclasses import dataclass
import random
from collections.abc import Callable
from generator.dnd_gen.staff.BORN_PARAMETRS import (FeatType, STAT_FEATS, PHYSICAL_PROPERTIES_FEATS,
                                                    ARCANE_PROPERTIES_FEATS_KEY, ARCANE_PROPERTIES_FEATS_FEATURE,
                                                    SKILL_FEATS)

@dataclass(frozen=True)
class BirthBaseFeatClass:
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
class ArcaneBornFeat(BirthBaseFeatClass):
    name: str
    target_type: FeatType
    target: str
    bonus: int | None
    uses: int | None
    recharge: str | None
    description: str

    def __repr__(self) -> str:
        return f"ArcaneBornFeat({self.name})"

@dataclass(frozen=True)
class BornFeat(BirthBaseFeatClass):
    name: str
    target_type: FeatType
    description: str

    def __repr__(self) -> str:
        return f"BornFeat({self.name})"


class CreatorBirthFeat:

    @staticmethod
    def create_feat(arg_dict: dict[int, str]) -> Callable[[str, int], BornFeat | dict[str, str], ArcaneBornFeat]:
        if arg_dict is STAT_FEATS or arg_dict is SKILL_FEATS or arg_dict is PHYSICAL_PROPERTIES_FEATS:
            return CreatorBirthFeat.create_feat_by_type
        if arg_dict is ARCANE_PROPERTIES_FEATS_KEY:
            return CreatorBirthFeat.create_arcana_feat

        raise ValueError(f"Unknown feat table: {arg_dict}")

    @staticmethod
    def create_feat_by_type(feat_table: tuple[FeatType, dict[int, str]], multiplier: int) -> BornFeat:
        feat_type, feat_dict = feat_table
        target = feat_dict[random.randint(1, len(feat_dict))]

        formatted_target = target.replace("_", " ").title()

        return BornFeat(
            name=(
                f"{'Gift' if multiplier > 0 else 'Curse'} "
                f"of {formatted_target}"
            ),
            target_type=feat_type,
            target=target,
            bonus=multiplier,
            description=(
                f"Upon creation, the character receives "
                f"a {multiplier:+} bonus to {formatted_target}."
            )
        )

    @staticmethod
    def create_arcana_feat(arcana_name: dict[int, str], bonus: int) -> ArcaneBornFeat:
        arcana_dict = ARCANE_PROPERTIES_FEATS_FEATURE[arcana_name[random.randint(1, len(arcana_name))]]
        return ArcaneBornFeat(
            name=arcana_dict["arcana_name"],
            target_type="arcana",
            target= arcana_dict["arcana_name"],
            bonus= bonus,
            uses= None,
            recharge= None,
            description=arcana_dict["arcana_description"]
        )


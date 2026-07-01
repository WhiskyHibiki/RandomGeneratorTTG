from dataclasses import dataclass
import random
from typing import Literal
from collections.abc import Callable


FeatType = Literal["stat", "skill", "physical", "arcana"]

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
    def create_feat_by_type(stat: tuple[FeatType, dict[int, str]], multiplier: int) -> BornFeat:
        stat_name, stat_dict = stat[0], stat[1]
        stat = stat_dict[random.randint(1, len(stat_dict))]
        return BornFeat(
            name=(
                f"{'Gift' if multiplier > 0 else 'Curse'} "
                f"of {stat_name.title()}"
            ),
            target_type=stat_name,
            target=stat_name,
            bonus=multiplier,
            description= f"Upon creation, the character receives a {multiplier:+} bonus to {stat.replace('_', ' ').title()}."
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

STAT_FEATS: dict[int, str] = {
    1: "strength",
    2: "dexterity",
    3: "constitution",
    4: "intelligence",
    5: "wisdom",
    6: "charisma",
}

PHYSICAL_PROPERTIES_FEATS: dict[int, str] = {
    1: "speed",
    2: "AC",
    3: "power",
    4: "attention",
    5: "climb",
    6: "swim",
    7: "initiative",
    8: "HP"
}

ARCANE_PROPERTIES_FEATS_KEY: dict[int, str] = {
    1: "arcana_name"
}

ARCANE_PROPERTIES_FEATS_FEATURE : dict[str, dict[str, str]] = {
    "arcana_name": {"arcana_name": "arcana_name", "arcana_description": "arcana_description"}
}

SKILL_FEATS: dict[int, str] = {
    1: "acrobatics",
    2: "animal_handling",
    3: "arcana",
    4: "athletics",
    5: "deception",
    6: "history",
    7: "insight",
    8: "intimidation",
    9: "investigation",
    10: "medicine",
    11: "nature",
    12: "perception",
    13: "performance",
    14: "persuasion",
    15: "religion",
    16: "sleight_of_hand",
    17: "stealth",
    18: "survival",
}


FEATS_TABLE: dict[int, tuple[FeatType, dict[int, str]]] = {
    1: ("stat", STAT_FEATS),
    2: ("skill", SKILL_FEATS),
    3: ("physical", PHYSICAL_PROPERTIES_FEATS),
}

SPECIAL_FEATS_TABLE: dict[int, tuple[FeatType, dict[int, str]]] = {
    1: ("arcana", ARCANE_PROPERTIES_FEATS_KEY),
}
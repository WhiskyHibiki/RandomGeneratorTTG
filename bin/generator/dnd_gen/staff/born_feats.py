from dataclasses import dataclass
from typing import Literal
from collections.abc import Callable


FeatType = Literal["stat", "skill", "physical", "arcana"]

@dataclass(frozen=True)
class BirthBaseClass:
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
class ArcaneBornFeat(BirthBaseClass):
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
class BornFeat(BirthBaseClass):
    name: str
    target_type: FeatType
    description: str

    def __repr__(self) -> str:
        return f"BornFeat({self.name})"


class CreatorBirthFeat:

    @staticmethod
    def create_feat(arg_dict: dict) -> Callable[[str, int], BornFeat | dict[str, str], ArcaneBornFeat]:
        if arg_dict is STAT_FEATS:
            return CreatorBirthFeat.create_stat_feat
        elif arg_dict is SKILL_FEATS:
            return CreatorBirthFeat.create_skill_feat
        elif arg_dict is PHYSICAL_PROPERTIES_FEATS:
            return CreatorBirthFeat.create_skill_feat
        elif arg_dict is ARCANE_PROPERTIES_FEATS:
            return CreatorBirthFeat.create_arcana_feat
        else:
            raise ValueError(f"Unknown feat table: {arg_dict}")


    @staticmethod
    def create_stat_feat(stat: str, multiplier: int) -> BornFeat:
        return BornFeat(
            name=(
                f"{'Gift' if multiplier > 0 else 'Curse'} "
                f"of {stat.title()}"
            ),
            target_type="stat",
            target=stat,
            bonus=multiplier,
            description= f"Upon creation, the character receives a {multiplier:+} bonus to {stat.replace('_', ' ').title()}."
        )

    @staticmethod
    def create_skill_feat(skill: str, multiplier: int) -> BornFeat:
        bonus = 2 * multiplier
        formatted_skill = skill.replace("_", " ").title()

        return BornFeat(
            name=(
                f"{'Gift' if multiplier > 0 else 'Curse'} "
                f"of {formatted_skill}"
            ),
            target_type="skill",
            target=skill,
            bonus=bonus,
            description= f"Upon creation, the character receives a {bonus:+} bonus to {skill.replace('_', ' ').title()}."
        )

    @staticmethod
    def create_arcana_feat(arcana_dict: dict[str, str], bonus: int) -> ArcaneBornFeat:
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

ARCANE_PROPERTIES_FEATS: dict[int, dict[str, str]] = {
    1: {"arcana_name": "arcana_name", "arcana_description": "arcana_description"}
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


FEATS_TABLE: dict[int, dict[int, str]] = {
    1: STAT_FEATS,
    2: SKILL_FEATS,
    3: PHYSICAL_PROPERTIES_FEATS,
}

SPECIAL_FEATS_TABLE: dict[int, tuple[FeatType, dict[int, dict[str, str]]]] = {
    1: ("arcana", ARCANE_PROPERTIES_FEATS),
}
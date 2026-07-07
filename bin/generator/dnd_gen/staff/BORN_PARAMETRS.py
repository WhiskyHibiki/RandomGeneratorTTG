from typing import Literal

FeatType = Literal["stat", "skill", "physical", "arcana"]

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


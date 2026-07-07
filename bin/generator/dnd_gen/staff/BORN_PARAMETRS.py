from typing import Literal
from collections.abc import Callable
from generator.dnd_gen.staff.born_statuses import (BirthStatus, Outcast, Peasant,
                                                   Artisan, Wealthy, Noble)

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

FEATS_TABLE: dict[int, tuple[FeatType, dict[int, str]]] = {
    1: ("stat", STAT_FEATS),
    2: ("skill", SKILL_FEATS),
    3: ("physical", PHYSICAL_PROPERTIES_FEATS),
}

SPECIAL_FEATS_TABLE: dict[int, tuple[FeatType, dict[int, str]]] = {
    1: ("arcana", ARCANE_PROPERTIES_FEATS_KEY),
}

BIRTH_STATUS_TABLE: dict[int, Callable[[int], BirthStatus]] = {
    2: Outcast,
    3: Peasant,
    4: Peasant,
    5: Peasant,
    6: Peasant,
    7: Peasant,
    8: Artisan,
    9: Artisan,
    10: Wealthy,
    11: Wealthy,
    12: Noble,
}

BIRTH_FEATS_TABLE: dict[int, tuple[int, int]] = {
    2:  (0, 3),
    3:  (1, 3),
    4:  (1, 2),
    5:  (1, 2),
    6:  (1, 1),
    7:  (1, 1),
    8:  (1, 1),
    9:  (2, 1),
    10: (2, 1),
    11: (3, 1),
    12: (3, 0),
}
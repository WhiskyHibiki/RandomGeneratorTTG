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

LEGENDARY_BIRTH_FEATS_DATA: dict[int, dict] = {
    1: {
        "tag": "legendary_blood",
        "name": "Legendary Blood",
        "kind": "legendary",
        "description": "The character was born with signs of a powerful destiny.",
        "influence_tags": ("noble_attention", "magic_interest", "dangerous_fate"),
    },
    2: {
        "tag": "child_of_prophecy",
        "name": "Child of Prophecy",
        "kind": "legendary",
        "description": "The character's birth was connected to an old prophecy.",
        "influence_tags": ("prophecy", "religious_attention", "dangerous_fate"),
    },
}


SUPER_CURSE_BIRTH_FEATS_DATA: dict[int, dict] = {
    1: {
        "tag": "marked_by_curse",
        "name": "Marked by Curse",
        "kind": "super_curse",
        "description": "The character was marked by a dark curse from birth.",
        "influence_tags": ("family_fear", "social_rejection", "dark_omens"),
    },
    2: {
        "tag": "born_under_dead_star",
        "name": "Born Under Dead Star",
        "kind": "super_curse",
        "description": "The character was born under a terrible omen.",
        "influence_tags": ("dark_omens", "social_rejection", "dangerous_fate"),
    },
}


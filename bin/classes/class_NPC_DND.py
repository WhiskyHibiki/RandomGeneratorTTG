from staff.born_statuses import BirthStatus

class DndNpc:
    def __init__(self):
        self.__name:    str | None  = None
        self.__family:  str | None  = None
        self.__age:     int | None  = None

        self.__health:      int | None      = None
        self.__background:  object | None   = None
        self.__class:       object | None   = None

        self.__character_traits: dict[str, BirthStatus] = {}

        self.__stats: dict[str, int | None] = {
            "STR": 0,
            "DEX": 0,
            "CON": 0,
            "INT": 0,
            "WIS": 0,
            "CHA": 0
        }

        self.skills: dict[str, int] = {
            "acrobatics": 0,
            "animal_handling": 0,
            "arcana": 0,
            "athletics": 0,
            "deception": 0,
            "history": 0,
            "insight": 0,
            "intimidation": 0,
            "investigation": 0,
            "medicine": 0,
            "nature": 0,
            "perception": 0,
            "performance": 0,
            "persuasion": 0,
            "religion": 0,
            "sleight_of_hand": 0,
            "stealth": 0,
            "survival": 0,
        }


    @property
    def name(self) -> str | None:
        return self.__name
    @name.setter
    def name(self, name: str) -> None:
        self.__name = name

    @property
    def family(self) -> str | None:
        return self.__family
    @family.setter
    def family(self, family: str) -> None:
        self.__family = family

    @property
    def age(self) -> int | None:
        return self.__age
    @age.setter
    def age(self, age: int) -> None:
        self.__age = age

    @property
    def character_traits(self) -> dict[str, BirthStatus]:
        return self.__character_traits

    @character_traits.setter
    def character_traits(self, character_traits: dict[str, BirthStatus]) -> None:
        if character_traits is None:
            raise ValueError("character_traits is >>> None")
        self.__character_traits.update(character_traits)


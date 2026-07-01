import random
from staff.born_statuses import BIRTH_STATUS_TABLE, BirthStatus, BIRTH_FEATS_TABLE
from staff.born_feats import FEATS_TABLE, ARCANE_PROPERTIES_FEATS_KEY, CreatorBirthFeat

class DndNpcGenerator:
    def __init__(self):
        pass

    @staticmethod
    def roll_dices() -> int:
       result = random.randint(1,6) + random.randint(1,6)
       return result

    def stage_birth_generate(self) -> dict[str, BirthStatus]:
        return {'birth_obj' : self.__stage_birth_generate()}

    def __stage_birth_generate(self) -> BirthStatus:
        status_roll = self.roll_dices()
        birth_status = BIRTH_STATUS_TABLE[status_roll](status_roll)

        feats_roll = self.roll_dices()
        birth_status.birth_feats_result(feats_roll)

        feats = BIRTH_FEATS_TABLE[feats_roll]
        bonus = 1

        for count_feat in feats:
            for each_feat in range(count_feat):
                if 10 <= self.roll_dices() <= 12:
                    feats_dict = ARCANE_PROPERTIES_FEATS_KEY
                    foo = CreatorBirthFeat.create_feat(feats_dict)

                else:
                    feats_dict = FEATS_TABLE[random.randint(1, len(FEATS_TABLE))]
                    foo = CreatorBirthFeat.create_feat(feats_dict[1])

                feat = foo(feats_dict, bonus)


                birth_status.birth_feats_list.append(feat)

            bonus = -bonus

        return birth_status




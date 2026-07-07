from generator.dnd_gen.npc_generator import DndNpcGenerator
from classes.class_NPC_DND import DndNpc


arbiter = DndNpcGenerator()
char = DndNpc()

char.character_traits = arbiter.stage_birth_generate()

for trait_name, birth_status in char.character_traits.items():
    print(f"Trait: {trait_name}")
    print(f"Birth status: {birth_status.status_name}")
    print(f"Status roll: {birth_status.status_roll}")
    print(f"Birth feats roll: {birth_status.birth_feats_roll}")

    print("Birth feats:")

    for feat in birth_status.birth_feats_list:
        print(f"- {feat.name}: {feat.description}")
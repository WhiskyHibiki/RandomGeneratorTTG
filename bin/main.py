from generator.dnd_gen.npc_generator import DndNpcGenerator
from classes.class_NPC_DND import DndNpc

arbiter = DndNpcGenerator()
char = DndNpc()

char.character_traits = arbiter.stage_birth_generate
for key in char.character_traits:
    print(char.character_traits[key].__dict__)
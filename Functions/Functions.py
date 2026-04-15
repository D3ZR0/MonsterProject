import os
import shutil

def create_new_monster(Name, Lethality, Health, Mana, AC, 
                       Movement, Size, Strength, Dexterity, Constitution, 
                       Intelligence, Wisdom, Charisma, Initiative, 
                       Draconic_actions = None, Resistances = None, Weaknesses = None):
    lines = [f"Name: {Name}\n",
             f"Lethality: {Lethality}\n\n", 
             f"Health: {Health}\n",
             "Temp Health:\n",
             f"Mana: {Mana}\n",
             f"AC: {AC}\n",
             f"Movement: {Movement}\n",
             f"Draconic Actions: {Draconic_actions}\n",
             f"Size: {Size}\n\n",
             f"Strength: {Strength} / +{Strength//2}\n", 
             f"Dexterity: {Dexterity} / +{Dexterity//2}\n", 
             f"Constitution: {Constitution} / +{Constitution//2}\n", 
             f"Intelligence: {Intelligence} / + {Intelligence//2}\n", 
             f"Wisdom: {Wisdom} / +{Wisdom//2}\n",
             f"Charisma: {Charisma} / +{Charisma//2}\n", 
             f"Initiative: {Initiative}\n\n",
             f"Strength Save: {Strength//2 + (Wisdom//2)}\n", 
             f"Dexterity Save: {Dexterity//2 + (Wisdom//2)}\n", 
             f"Constitution Save: {Constitution//2 + (Wisdom//2)}\n", 
             f"Intelligence Save: {Intelligence//2 + (Wisdom//2)}\n", 
             f"Wisdom Save: {Wisdom//2 + Wisdom//2}\n",
             f"Charisma Save: {Charisma//2 + Wisdom//2}\n\n",
             f"Resistances: {Resistances}\n", 
             f"Weaknesses: {Weaknesses}\n"
             ]
            
    try:
        with open(f"Monsters/{Name}.txt", "x", encoding="utf-8") as f:
            f.writelines(lines)
    except FileExistsError:
        print(f"{Name}.txt already exists, Monster creation aborted.")

def create_custom_hp(monster_name, player_count):
    shutil.copy(f"Monsters/{monster_name}.txt", "temp_monster.txt")
    with open("temp_monster.txt", "r") as f:
        content = f.read()
    lines = content.split('\n')
    for i, line in enumerate(lines):
        if line.startswith("Health: "):
            hp_value = line.split("Health: ")[1]
            hp_value = hp_value * .5 * player_count
            lines[i] = f"Health: {hp_value}"
            break
    
    with open("temp_monster.txt", "w") as f:
        f.write('\n'.join(lines))
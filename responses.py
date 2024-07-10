from random import choice, randint
import random

def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    if lowered == '':
        return 'Well you seem awfully silent'
    elif 'hello' in lowered:
        return 'Hello there!'
    elif 'hi' in lowered:
        return 'Hello there!'
    elif 'ohayo' in lowered:
        return 'Hai, Ohayo Guzaimasu'
    elif 'how are you' in lowered:
        return 'Good, thanks!'
    elif 'how you doing' in lowered:
        return 'Good, thanks!'
    elif 'bye' in lowered:
        return 'See you!'
    elif 'fuck' in lowered or 'idiot' in lowered or 'bitch' in lowered or 'dumbass' in lowered:
        return 'fuck you'
    elif 'roll dice' in lowered or 'roll a dice' in lowered:
        return f'''
you rolled: {randint(1, 6)}
'''
    elif 'generate a dnd character sheet' in lowered:
        return f'''
Race: {generate_character_sheet()['Race']}
Class: {generate_character_sheet()['Class']}
Strength: {generate_character_sheet()['Strength']}
Dexterity: {generate_character_sheet()['Dexterity']}
Constitution: {generate_character_sheet()['Constitution']}
Intelligence: {generate_character_sheet()['Intelligence']}
Wisdom: {generate_character_sheet()['Wisdom']}
Charisma: {generate_character_sheet()['Charisma']}
'''
    else:
        return choice([
            'I did not understand what you said, could you please rephrase that',
            'Do you mind rephrasing that',
            'Sorry I have yet to be programmed with an AI algorithm for chat responses',
            'What are you reffering to?'
        ])

def generate_character_sheet():
    race = random.choice(['Human', 'Elf', 'Dragonborn', 'Tiefling', 'Dwarf', 'Half-elf', 'Halfling', 'Half-Orc', 'Gnome', 'Aasimar'])
    character_sheet = {
        'Race': race,
        'Class': random.choice(['Barbarian', 'Bard', 'Cleric', 'Druid', 'Fighter', 'Monk', 'Paladin', 'Ranger', 'Rogue', 'Sorcerer', 'Warlock', 'Wizard']),
        'Strength': random.randint(1, 20),
        'Dexterity': random.randint(1, 20),
        'Constitution': random.randint(1, 20),
        'Intelligence': random.randint(1, 20),
        'Wisdom': random.randint(1, 20),
        'Charisma': random.randint(1, 20),
        # Add more fields as needed
    }
    return character_sheet
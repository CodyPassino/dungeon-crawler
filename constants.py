# Change to adjust editfiles.indent_obj()
FLOOR = 15 # Line in notpad, top two lines are name and hp, adds 1 in notepad
INDENT = 50 # Multipy by " " to get indentations, how far right the image goes

# indexes for File
TEXT_FILE = 0
FOLDERS = 1

# Path
PATH = "docs/"

# Player -> folders
PLAYER_FOLDER = "player" # The folder the player images are in

PLAYER_FILES = ["player.txt", PLAYER_FOLDER]
    # Holding
PLAYER_R_HAND_FILES = ["playerholdingright.txt", PLAYER_FOLDER]
PLAYER_L_HAND_FILES = ["playerholdingleft.txt", PLAYER_FOLDER]
PLAYER_B_HAND_FILES = ["playerholdingboth.txt", PLAYER_FOLDER]
    # Attacking
PLAYER_R_HAND_OUT_FILES = ["playeroutright.txt", PLAYER_FOLDER]
    
# Items -> folders
ITEMS_FOLDER = "items" # The folder the item images are in

    # Weapons
WEAPONS_FOLDER = ITEMS_FOLDER + "/weapons" # The folder the weapon images are in

FIST_FILES = ["fist.txt", WEAPONS_FOLDER]
CLUB_FILES = ["club.txt", WEAPONS_FOLDER]
SWORD_FILES = ["sword.txt", WEAPONS_FOLDER]
LONG_SWORD_FILES = ["longsword.txt", WEAPONS_FOLDER]

SHEILD_FILES = ["sheild.txt", WEAPONS_FOLDER]

    # Consumables
CONSUMABLES_FOLDER = ITEMS_FOLDER + "/consumables" # The folder consumables are in

SMALL_HEAL_FILES = ["smallheal.txt", CONSUMABLES_FOLDER]
LARGE_HEAL_FILES = ["largeheal.txt", CONSUMABLES_FOLDER]
# Characters -> folders
CHARACTERS_FOLDER = "CHARACTERS" # The folder the character images are in

    # Enemies
ENEMIES_FOLDER = CHARACTERS_FOLDER + "/enemies"

        # Goblin
GOBLIN_FOLDER = ENEMIES_FOLDER + "/goblin"

GOBLIN_FILES = ["goblin.txt", GOBLIN_FOLDER]
GOBLIN_L_HAND_FILES = ["goblinholdingleft.txt", GOBLIN_FOLDER]

        # Slime
SLIME_FOLDER = ENEMIES_FOLDER + "/slime"

SLIME_FILES = ["slime.txt", SLIME_FOLDER]

    # NPCs
NPC_FOLDER = CHARACTERS_FOLDER + "/npc"
        # No NPC yet
        
    # Entities -> interactable objects
ENTITIES_FOLDER = CHARACTERS_FOLDER + "/entities"

        #chest
CHEST_FILES = ["chest.txt", ENTITIES_FOLDER + "/chest"]
CHEST_OPEN_FILES = ["chestopen.txt", ENTITIES_FOLDER + "/chest"]

# Map -> folders
    # Size
MAP_WIDTH = 25
MAP_HEIGHT = 10

    # Files
MAP_FOLDER = "map/"

    # Terrian
TERRAIN_FOLDER = MAP_FOLDER + "terrain"

        # vertical
VERTICAL_FOLDER = TERRAIN_FOLDER + "vertical"

OPEN_VERTICAL_FILES = ["openvertical.txt", VERTICAL_FOLDER]
OPEN_TOP_VERTICAL_FILES = ["opentopvertical.txt", VERTICAL_FOLDER]
OPEN_BOTTOM_VERTICAL_FILES = ["openbottomvertical.txt", VERTICAL_FOLDER]

    # horizontal
HORIZONTAL_FOLDER = TERRAIN_FOLDER + "horizontal"

OPEN_HORIZONTAL_FILES = ["openhorizontal.txt", HORIZONTAL_FOLDER]
OPEN_RIGHT_HORIZONTAL_FILES = ["openrighthorizontal.txt", HORIZONTAL_FOLDER]
OPEN_LEFT_HORIZONTAL_FILES = ["openlefthorizontal.txt", HORIZONTAL_FOLDER]

    # Entities
MAP_ENTITIES_FOLDER = MAP_FOLDER + "entities" 

MAP_PLAYER = ["player.txt", MAP_ENTITIES_FOLDER]
MAP_PLAYER_ON = ["playeron.txt", MAP_ENTITIES_FOLDER]
MAP_ENEMY = ["enemy.txt", MAP_ENTITIES_FOLDER]
MAP_DEAD_CHARACTER = ["deadcharacter.txt", MAP_ENTITIES_FOLDER]

# MetaData -> from first line of text files

    # Items
META_ITEMS = {
    "HANDLE_WIDTH": 0,
    "HANDLE_HEIGHT": 1
}

    # Characters
META_CHARACTERS ={
    "HAND_HEIGHT": 0
}

    # Maps
META_MAPS = {
    "OBJ_WIDTH": 0,
    "OBJ_HEIGHT": 1
}
# Items

    # Weapons
FIST = {
    "TYPE": "weapon",
    "NAME": "hand",
    "DAMAGE": 5,
    "BLOCK": 0,
    "FILES": FIST_FILES
}
CLUB = {
    "TYPE": "weapon",
    "NAME":"club",
    "DAMAGE": 10,
    "BLOCK": 5,
    "FILES": CLUB_FILES
}
SWORD = {
    "TYPE": "weapon",
    "NAME":"sword",
    "DAMAGE": 20,
    "BLOCK": 10,
    "FILES": SWORD_FILES
}
LONG_SWORD = {
    "TYPE": "weapon",
    "NAME":"long sword",
    "DAMAGE": 40,
    "BLOCK": 20,
    "FILES": LONG_SWORD_FILES
}
SHEILD = {
    "TYPE": "weapon",
    "NAME":"sheild",
    "DAMAGE": 0,
    "BLOCK": 10,
    "FILES": SHEILD_FILES 
}

    # Consumables
SMALL_HEAL = {
    "TYPE": "consumable",
    "NAME":"small heal",
    "EFFECT_STRENGTH": .25,
    "USES": 1,
    "FILES": SMALL_HEAL_FILES 
}
LARGE_HEAL = {
    "TYPE": "consumable",
    "NAME":"large heal",
    "EFFECT_STRENGTH": .5,
    "USES": 1,
    "FILES": LARGE_HEAL_FILES 
}

# Chest

    # Chances
WEAPONS_CHANCE = 50         # %
CONSUMABLES_CHANCE = 50     # %

    # Items
CHEST_WEAPONS = [CLUB, SWORD, LONG_SWORD, SHEILD]
CHEST_CONSUMABLES = [SMALL_HEAL, LARGE_HEAL]

    # No chest nearby txt
NO_CHEST_NEARBY = {
    "NO_CHEST_TEXT": "No chest in sight, need to be on chest to open it"
}

import constants
import my_input
from .entity_handler import EntityHandler
from .map_creation_handler import MapCreationHandler
from player import Player
from enemy_classes import *

class InputHandler:
    def __init__(self, username):
        self.entityhandler = EntityHandler() # Instance of Entity_Handler
        self.player = self.entityhandler.spawn_instance(Player, constants.CLUB, constants.FIST, username)
        self.map = None # Redeclared later, here to prevent declaration error

    def start_game(self):
        self.enemy = self.entityhandler.spawn_instance(Slime, constants.FIST, constants.FIST)
        
    def enter_dungeon(self):
        self.map = MapCreationHandler() # Makes the map

    def q_attack(self, request):
        if request == "y":
            self.entityhandler.attack(self.player, self.enemy)
        elif request == "n":
            self.entityhandler.attack(self.enemy, self.player)

    def kill_enemy(self):
        self.entityhandler.delete_instance(self.enemy)

    def move(self):
        direction = input("Where to move?").strip().lower()
        match direction:
            case "w":
                self.map.move_up()
            case "s":
                self.map.move_down()
            case _:
                print("not moving")

    def chest_open(self):
        if self.map == None:
            print("You're not in the dungeon")
        else:
            item_found = self.map.chest_open()

            if "NAME" in item_found: # Confirms the returned item is an item
                question = f"You have found {item_found["NAME"]} do you wish to store it?"
                yes = my_input.y_n(question)

                if yes:
                    print(f'{item_found["NAME"]} has been "stored"')
                else:
                    print(f"{item_found["NAME"]} has been left near the chest")
            else:
                print(item_found["NO_CHEST_TEXT"])
        

        

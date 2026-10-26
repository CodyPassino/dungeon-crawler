import constants
from .entity_handler import EntityHandler
from .chest_handler import ChestHandler


# spawning enemies
# spawning chests
class MapEventHandler:
    # Local constants
    POS_X = 0
    POS_Y = 1

    def __init__(self):
        self.floor = 1
        self.pos = [0, 0] # Will track players position throughout expedition
        self.chests = {} # Makes a dict to store chest instances
        self.chest_spawn()

    def chest_spawn(self):
        chest = ChestHandler(self.floor, tuple(self.pos))
        self.chests[chest.POS] = chest # Stores the chest instance in a dict 
        print(chest.POS, " is the chest")

    def chest_open(self):
        item_found = None # so declaration error is not thrown if no chest found
        tuple_pos = tuple(self.pos) # Used in the dict, list are mutable so must be tuple

        if tuple_pos in self.chests:
            item_found = self.chests[tuple_pos].item
            self.chests[tuple_pos].opened = True

        # Makes sure a chest is at pos
        if item_found == None:
            return constants.NO_CHEST_NEARBY
        else:
            return item_found
        
    def move_up(self):
        self.pos[self.POS_Y] += 1
        print(f"Moved up to {self.pos}")

    def move_down(self):
        self.pos[self.POS_Y] -= 1
        print(f"Moved down to {self.pos}")
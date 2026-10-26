from .entity_handler import EntityHandler
from .chest_handler import ChestHandler


# spawning enemies
# spawning chests
class MapEventHandler:
    def __init__(self):
        self.floor = 1
        self.pos = [0, 0] # Will track players position throughout expedition
        self.chests = list() # Makes a list to store chest instances
        self.chest_spawn()

    def chest_spawn(self):
        chest = ChestHandler(self.floor, self.pos)
        self.chests.append(chest)

    def chest_open(self):
        item_found = None # so declaration error is not thrown if no chest found

        for chest in self.chests:
            if chest.pos == self.pos:
                item_found = chest.item
                chest.opened = True

        # Makes sure a chest is at pos
        if item_found == None:
            return False
        else:
            return item_found
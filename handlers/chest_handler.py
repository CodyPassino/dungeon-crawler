import constants
import random

class ChestHandler():
    def __init__(self, floor, pos):
        self.floor = floor
        self.pos = pos
        self.opened = False
        self.item = self.set_item()

    def set_item(self):
        item_found = None
        largest_chance = constants.WEAPONS_CHANCE + constants.CONSUMABLES_CHANCE

        type_rng = random.randint(0,largest_chance)
        # Chance to get a weapon
        if type_rng > abs(largest_chance - constants.WEAPONS_CHANCE):
            select_rng = random.randint(0, len(constants.CHEST_WEAPONS)-1)     
            item_found = constants.CHEST_WEAPONS[select_rng]

        # Chance to get a consumable
        elif type_rng <= abs(largest_chance - constants.CONSUMABLES_CHANCE):   
            select_rng = random.randint(0,len(constants.CHEST_CONSUMABLES)-1)
            item_found = constants.CHEST_CONSUMABLES[select_rng]

        return item_found
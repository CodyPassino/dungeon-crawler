import constants
from enemies import Enemy

class Goblin(Enemy):

    def __init__(self, main_hand = constants.FIST, off_hand = constants.FIST, name = None):

        self.max_health = 50
        self.health = self.max_health
        self.RACE = "goblin"

        super().__init__(main_hand, off_hand, name)
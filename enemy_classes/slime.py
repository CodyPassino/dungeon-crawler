from enemies import Enemy
import constants

class Slime(Enemy):

    def __init__(self, main_hand = constants.FIST, off_hand = constants.FIST, name = None):
    
            self.max_health = 25
            self.health = self.max_health
            self.RACE = "slime"

            # Slime overides the main and off hand -> only fist, still takes parameters for enity_handler
            main_hand = constants.FIST
            off_hand = constants.FIST

            super().__init__(main_hand, off_hand, name)
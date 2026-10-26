from entities import Entity

class Player(Entity):

    def __init__(self, main_hand, off_hand, name):

        self.max_health = 100
        self.health = self.max_health
        
        super().__init__(main_hand, off_hand, name)
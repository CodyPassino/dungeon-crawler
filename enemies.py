from entities import Entity

class Enemy(Entity):
    def __init__(self, main_hand, off_hand, name):
        # Enemy name = None? this makes, enemy_name = enemy_race
        if name == None:
            name = self.RACE

        super().__init__(main_hand, off_hand, name)

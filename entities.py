class Entity:

    def __init__(self, main_hand, off_hand, name):
        self.name = name

        self.equipped = [main_hand, off_hand] # Stores what items are equipped
        self.damage = self.get_damage()
        self.block = self.get_block()

    def get_damage(self): # returns int of damage value
        MAIN_HAND_DAMAGE = self.equipped[0]["DAMAGE"]
        OFF_HAND_DAMAGE = self.equipped[1]["DAMAGE"]

        return MAIN_HAND_DAMAGE + OFF_HAND_DAMAGE//2 

    def get_block(self): # returns int of block value
        MAIN_HAND_BLOCK = self.equipped[0]["BLOCK"] 
        OFF_HAND_BLOCK = self.equipped[1]["BLOCK"]

        return MAIN_HAND_BLOCK//2 + OFF_HAND_BLOCK 

    def attack(self, target):
        print(f"{self.name} has attacked {target.name} for {self.damage} damage")
        target.hit(self.damage)

    def hit(self, damage_taken):

        if self.block != 0:
            if (damage_taken - self.block) >= 0:
                self.health -= (damage_taken - self.block)
                print(f"{self.name} has blocked {self.block} damage")
        else:
             self.health -= damage_taken

        if self.is_alive():
            print(f"{self.name} has {self.health} hp remaining")

    def check_endure_hit(self, damage_taken):
        if self.block != 0:
            if (damage_taken - self.block) >= 0:
                return self.health - (damage_taken - self.block) # returns boolean of if health positve
    
        return self.health - damage_taken > 0 # returns boolean of if health positive

    def is_alive(self):
        return self.health > 0
            
    def print_name(self):
        print(self.name)
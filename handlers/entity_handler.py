class EntityHandler:

    def __init__(self):
        self.active_instance = list()

    def spawn_instance(self, object, main_hand, off_hand, name = None): # Returns instance
        instance = object(main_hand, off_hand, name) # Makes instance
        self.active_instance.append(instance) # Adds to a list, used when instance dead

        return instance

    def delete_instance(self, instance): # Deletes an instance
        if instance in self.active_instance:
            print(f"{instance.name=} was removed")
            self.active_instance.remove(instance)
        else:
            print("Instance does not exist")

    def attack(self, attacker, target):
        target_alive = target.check_endure_hit(attacker.damage)

        if target in self.active_instance and target_alive: # If targets in active_instance and hp > 0
            attacker.attack(target)
        else: # Targets not alive or in active_instance
            if not target_alive: # If target hp < 0
                self.delete_instance(target)
            else:
                print(f"{target.name} has already been killed")

    
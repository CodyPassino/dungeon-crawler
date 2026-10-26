from .map_event_handler import MapEventHandler
import file_manager

# Map creation 
class MapHandler():
    def __init__(self):
        self.events = MapEventHandler()

    def chest_open(self):
        item_found = self.events.chest_open()
        return item_found

    def move_up(self): # temp
        self.events.move_up()

    def move_down(self):
        self.events.move_down()

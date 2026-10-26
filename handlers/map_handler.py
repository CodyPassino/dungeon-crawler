from .map_event_handler import MapEventHandler
import file_manager

# Map creation 
class MapHandler():
    def __init__(self):
        self.map = MapEventHandler()

    def chest_open(self):
        item_found = self.map.chest_open()
        return item_found

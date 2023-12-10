from objectbox.model import *
import OBOXShip

print("__________________BEG")
@Entity(id=12, uid=12)
class Galaxy:
    identifier = Id(id=1, uid=12001)
    name = Property(str, id=2, uid=12002)
    universe = Property(str, id=3, uid=12003)
    ships = Property(dict, type=PropertyType.long, id=4, uid=12004)

    def __init__(self, identifier, name, universe, string: str = ""):
        self.str = string
        self.identifier = identifier
        self.name = name
        self.universe = universe
        self.ships = {}
        print("__________________HERE")
        
    def getIdentifier(self):
        return self.identifier

    def getName(self):
        return self.name

    def getUniverse(self):
        return self.universe

    def addShip(self, ship):  # Add a ship based on it's affiliation
        affiliation = ship.getAffiliation()
        if not (affiliation in self.ships.keys()):  # If the affiliation is new create a new persistent Map
            self.ships[affiliation] = {ship}
        self.ships[affiliation][ship.getSerialNumber()] = ship

    def getShips(self, affiliation):
        return list(self.ships[affiliation].values())
print("__________________END")
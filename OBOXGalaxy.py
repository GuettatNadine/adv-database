import persistent
import persistent.mapping
from objectbox.model import *

@Entity(id=4, uid=4)
class Galaxy(persistent.Persistent):
    def __init__(self, identifier, name, universe):
        self.identifier = Property(identifier, id = 1, uid 1007)
        self.name = Property(name, id = 2, uid 1008)
        self.universe = Property(universe, id = 3, uid 1009)
        self.ships = persistent.mapping.PersistentMapping()

    def getIdentifier(self):
        return self.identifier

    def getName(self):
        return self.name

    def getUniverse(self):
        return self.universe

    def addShip(self, ship):  # Add a ship based on it's affiliation
        affiliation = ship.getAffiliation()
        if not (affiliation in self.ships.keys()):  # If the affiliation is new create a new persistent Map
            self.ships[affiliation] = persistent.mapping.PersistentMapping()
        self.ships[affiliation][ship.getSerialNumber()] = ship

    def getShips(self, affiliation):
        return list(self.ships[affiliation].values())

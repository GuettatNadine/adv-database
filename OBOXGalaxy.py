import persistent
import persistent.mapping
from objectbox.model import *
import OBOXShip


@Entity(id=4, uid=4)
class Galaxy:
    def __init__(self, identifier, name, universe):
        self.identifier = Property(id=1, uid=4001)
        self.name = Property(str, id=2, uid=4002)
        self.universe = Property(str, id=3, uid=4003)
        self.ships = Property(dict, type=OBOXShip.Ship, id=4, uid=4004)

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

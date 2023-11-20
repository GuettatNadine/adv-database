import persistent
import persistent.mapping


class Galaxy(persistent.Persistent):
    def __init__(self, identifier, name, universe):
        self.identifier = identifier
        self.name = name
        self.universe = universe
        self.ships = persistent.mapping.PersistentMapping()

    def getIdentifier(self):
        return self.identifier

    def getName(self):
        return self.name

    def getUniverse(self):
        return self.universe

    def addShip(self, ship):
        affiliation = ship.getAffiliation()
        if not (affiliation in self.ships.keys()):
            self.ships[affiliation] = persistent.mapping.PersistentMapping()
        self.ships[affiliation][ship.getSerialNumber()] = ship

    def getShips(self, affiliation):
        return list(self.ships[affiliation].values())

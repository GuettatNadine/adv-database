from objectbox.model import *

@Entity(id=5, uid=5)
class Ship:
    def __init__(self, serialNumber, affiliation):
        self.serialNumber = Property(int, id = 1, uid = 5001)
        self.affiliation = Property(str, id = 2, uid = 5002)
        # persistant 
        self.crew = persistent.mapping.PersistentMapping()
        self.modules = persistent.mapping.PersistentMapping()
        self.modules["weapon"] = persistent.mapping.PersistentMapping()
        self.modules["energy"] = persistent.mapping.PersistentMapping()
        self.modules["shield"] = persistent.mapping.PersistentMapping()

    def getSerialNumber(self):
        return self.serialNumber

    def getAffiliation(self):
        return self.affiliation

    def getCrew(self):
        return list(self.crew.values())

    def getModules(self, moduleType):
        return list(self.modules[moduleType].values())

    def setAffiliation(self, affiliation):
        self.affiliation = affiliation

    def addCrew(self, crew):  # Add Crew member by id
        for member in crew:
            self.crew[member.getIdentifier()] = member

    def addModules(self, moduleType, modules):  # Add Module by type and id
        for module in modules:
            self.modules[moduleType][module.getSerialNumber()] = module

@Entity(id=6, uid=6)
class MotherShip(Ship):
    def __init__(self, serialNumber, affiliation):
        super().__init__(serialNumber, affiliation)
        # persistant
        self.passengers = persistent.mapping.PersistentMapping()

    def getPassengers(self):
        return list(self.passengers.values())

    def addPassengers(self, passengers):  # Add passenger by id
        for member in passengers:
            self.passengers[member.getIdentifier()] = member

@Entity(id=7, uid=7)
class OtherShip(Ship):
    def __init__(self, serialNumber, affiliation, shipType):
        super().__init__(serialNumber, affiliation)
        self.shipType = Property(str, id = 7, uid = 7001)

    def getShipType(self):
        return self.shipType

    def setShipType(self, shipType):
        self.shipType = shipType

@Entity(id=8, uid=8)
class TransportShip(Ship):
    def __init__(self, serialNumber, affiliation):
        super().__init__(serialNumber, affiliation)
        # persistant
        self.cargo = persistent.mapping.PersistentMapping()

    def getCargo(self):
        return list(self.cargo.keys())

    def getCargoValues(self, itemType):
        return self.cargo[itemType]

    def setCargo(self, cargo):
        self.cargo = cargo

    def addCargo(self, itemType, number):  # Add cargo item by name
        if not (itemType in self.cargo.keys()):
            self.cargo[itemType] = 0
        self.cargo[itemType] += number

    def removeCargo(self, itemType, number):  # Remove Cargo Item by name and only removes the input value
        self.cargo[itemType] -= number
        if self.cargo[itemType] < 0:  # the min is an empty cargo
            self.cargo[itemType] = 0

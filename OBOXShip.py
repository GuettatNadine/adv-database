from objectbox.model import *

import OBOXPerson
import OBOXModule

@Entity(id=8, uid=8)
class Ship:
    serialNumber = Id(id=1, uid=8001)
    affiliation = Property(str, id=2, uid=8002)
    crew = Property(dict, type=PropertyType.long, id=3, uid=8003)
    modules = Property(dict, type=PropertyType.long, id=4, uid=8004)

    def __init__(self, serialNumber, affiliation, string: str = ""):
        self.str = string
        serialNumber = self.serialNumber
        affiliation = self.affiliation
        crew = {}
        cargo = {}

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


@Entity(id=9, uid=9)
class MotherShip:
    serialNumber = Id(id=1, uid=9001)
    affiliation = Property(str, id=2, uid=9002)
    crew = Property(dict, type=PropertyType.long, id=3, uid=9003)
    modules = Property(dict, type=PropertyType.long, id=4, uid=9004)
    passengers = Property(dict, type=PropertyType.long, id=5, uid=9005)
    
    def __init__(self, serialNumber, affiliation, string: str = ""):
        self.str = string
        serialNumber = self.serialNumber
        affiliation = self.affiliation
        crew = {}
        modules = {"weapon": {}, "energy": {}, "shield": {}}
        passenger = {}
        
    def getPassengers(self):
        return list(self.passengers.values())

    def addPassengers(self, passengers):  # Add passenger by id
        for member in passengers:
            self.passengers[member.getIdentifier()] = member

@Entity(id=10, uid=10)
class OtherShip:
    serialNumber = Id(id=1, uid=10001)
    affiliation = Property(str, id=2, uid=10002)
    crew = Property(dict, type=PropertyType.long, id=3, uid=10003)
    modules = Property(dict, type=PropertyType.long, id=4, uid=10004)
    shiptype = Property(int, id=5, uid=10005)
    
    def __init__(self, serialNumber, affiliation, shipType, string: str = ""):
        self.str = string
        serialNumber = self.serialNumber
        affiliation = self.affiliation
        crew = {}
        modules = {"weapon": {}, "energy": {}, "shield": {}}
        shiptype = self.shiptype
        
    def getShipType(self):
        return self.shipType

    def setShipType(self, shipType):
        self.shipType = shipType

@Entity(id=11, uid=11)
class TransportShip:
    serialNumber = Id(id=1, uid=11001)
    affiliation = Property(str, id=2, uid=11002)
    crew = Property(dict, type=PropertyType.long, id=3, uid=11003)
    modules = Property(dict, type=PropertyType.long, id=4, uid=11004)
    cargo = Property(dict, type=PropertyType.long, id=5, uid=11005)

    def __init__(self, serialNumber, affiliation, string: str = ""):
        self.str = string
        serialNumber = self.serialNumber
        affiliation = self.affiliation
        crew = {}
        modules = {"weapon": {}, "energy": {}, "shield": {}}
        cargo = {}
         
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

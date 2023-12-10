from objectbox.model import *

@Entity(id=4, uid=4)
class Module:
    serialNumber = Id(id=1, uid=4001)
    brand = Property(str, id=2, uid=4002)
    year = Property(int, id=3, uid=4003)
    model = Property(str, id=4, uid=4004)
    energy = Property(int, id=5, uid=4005)
    maxEnergy = Property(int, id=6, uid=4006)
    
    def __init__(self, serialNumber, brand, year, model, energy, maxEnergy, string: str = ""):
        self.str = string
        self.serialNumber = serialNumber
        self.brand = brand
        self.year = year
        self.model = model
        self.energy = energy
        self.maxEnergy = maxEnergy
    
    def getSerialNumber(self):
        return self.serialNumber

    def getBrand(self):
        return self.brand

    def getYear(self):
        return self.year

    def getModel(self):
        return self.model

    def getEnergy(self):
        return self.energy

    def getMaxEnergy(self):
        return self.maxEnergy

    def setEnergy(self, energy):
        self.energy = energy

@Entity(id=5, uid=5)
class EnergyModule:
    serialNumber = Id(id=1, uid=5001)
    brand = Property(str, id=2, uid=5002)
    year = Property(int, id=3, uid=5003)
    model = Property(str, id=4, uid=5004)
    energy = Property(int, id=5, uid=5005)
    maxEnergy = Property(int, id=6, uid=5006)
    output = Property(int, id=7, uid=5007)
    rechargeRate = Property(int, id=8, uid=5008)

    def __init__(self, serialNumber, brand, year, model, energy, maxEnergy, output, rechargeRate, string: str = ""):
        self.str = string
        self.serialNumber = serialNumber
        self.brand = brand
        self.year = year
        self.model = model
        self.energy = energy
        self.maxEnergy = maxEnergy
        self.output = output
        self.rechargeRate = rechargeRate
        
    def getOutput(self):
        return self.output

    def getRechargeRate(self):
        return self.rechargeRate

    def setOutput(self, output):
        self.output = output

    def setRechargeRate(self, rechargeRate):
        self.rechargeRate = rechargeRate

@Entity(id=6, uid=6)
class WeaponModule:
    serialNumber = Id(id=1, uid=6001)
    brand = Property(str, id=2, uid=6002)
    year = Property(int, id=3, uid=6003)
    model = Property(str, id=4, uid=6004)
    energy = Property(int, id=5, uid=6005)
    maxEnergy = Property(int, id=6, uid=6006)
    weaponType = Property(str, id=7, uid=6007)
    caliber = Property(int, id=8, uid=6008)

    def __init__(self, serialNumber, brand, year, model, energy, maxEnergy, weaponType, caliber, string: str = ""):
        self.str = string
        self.serialNumber = serialNumber
        self.brand = brand
        self.year = year
        self.model = model
        self.energy = energy
        self.maxEnergy = maxEnergy
        self.weaponType = weaponType
        self.caliber = caliber

    def getType(self):
        return self.weaponType

    def getCaliber(self):
        return self.caliber


@Entity(id=7, uid=7)
class ShieldModule:
    serialNumber = Id(id=1, uid=7001)
    brand = Property(str, id=2, uid=7002)
    year = Property(int, id=3, uid=7003)
    model = Property(str, id=4, uid=7004)
    energy = Property(int, id=5, uid=7005)
    maxEnergy = Property(int, id=6, uid=7006)
    size = Property(int, id=7, uid=7007)

    def __init__(self, serialNumber, brand, year, model, energy, maxEnergy, size, string: str = ""):
        self.str = string
        self.serialNumber = serialNumber
        self.brand = brand
        self.year = year
        self.model = model
        self.energy = energy
        self.maxEnergy = maxEnergy
        self.size = size

    def getSize(self):
        return self.size
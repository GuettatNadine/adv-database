import persistent
from objectbox.model import *


@Entity(id=9, uid=9)
class Module:
    def __init__(self, serialNumber, brand, year, model, energy, maxEnergy):
        self.serialNumber = Property(int, id=1, uid=9001)
        self.brand = Property(str, id=2, uid=9002)
        self.year = Property(int, id=3, uid=9003)
        self.model = Property(str, id=4, uid=9004)
        self.energy = Property(int, id=5, uid=9005)
        self.maxEnergy = Property(int, id=6, uid=9006)

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


@Entity(id=10, uid=10)
class EnergyModule(Module):
    def __init__(self, serialNumber, brand, year, model, energy, maxEnergy, output, rechargeRate):
        super().__init__(serialNumber, brand, year, model, energy, maxEnergy)
        self.output = Property(int, id=1, uid=10001)
        self.rechargeRate = Property(int, id=2, uid=10002)

    def getOutput(self):
        return self.output

    def getRechargeRate(self):
        return self.rechargeRate

    def setOutput(self, output):
        self.output = output

    def setRechargeRate(self, rechargeRate):
        self.rechargeRate = rechargeRate


@Entity(id=11, uid=11)
class WeaponModule(Module):
    def __init__(self, serialNumber, brand, year, model, energy, maxEnergy, weaponType, caliber):
        super().__init__(serialNumber, brand, year, model, energy, maxEnergy)
        self.weaponType = Property(str, id=1, uid=1101)
        self.caliber = Property(int, id=2, uid=1102)

    def getType(self):
        return self.weaponType

    def getCaliber(self):
        return self.caliber


@Entity(id=12, uid=12)
class ShieldModule(Module):
    def __init__(self, serialNumber, brand, year, model, energy, maxEnergy, size):
        super().__init__(serialNumber, brand, year, model, energy, maxEnergy)
        self.size = Property(int, id=1, uid=1201)

    def getSize(self):
        return self.size

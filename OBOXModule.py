import persistent
from objectbox.model import *


@Entity(id=9, uid=9)
class Module:
    def __init__(self, serialNumber, brand, year, model, energy, maxEnergy):
        self.serialNumber = Property(serialNumber, id=1, uid=1013)
        self.brand = Property(brand, id=2, uid=1014)
        self.year = Property(year, id=3, uid=1015)
        self.model = Property(model, id=4, uid=1016)
        self.energy = Property(energy, id=5, uid=1017)
        self.maxEnergy = Property(maxEnergy, id=6, uid=1018)

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
        self.output = Property(output, id=1, uid=1019)
        self.rechargeRate = Property(rechargeRate, id=2, uid=1020)

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
        self.weaponType = Property(weaponType, id=1, uid=1021)
        self.caliber = Property(caliber, id=2, uid=1022)

    def getType(self):
        return self.weaponType

    def getCaliber(self):
        return self.caliber


@Entity(id=12, uid=12)
class ShieldModule(Module):
    def __init__(self, serialNumber, brand, year, model, energy, maxEnergy, size):
        super().__init__(serialNumber, brand, year, model, energy, maxEnergy)
        self.size = Property(int, id=1, uid=1023)

    def getSize(self):
        return self.size

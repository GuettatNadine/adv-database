from objectbox.model import *

@Entity(id=4, uid=4)
class Module:
    def __init__(self, serialNumber, brand, year, model, energy, maxEnergy):
        self.serialNumber = Property(int, id=1, uid=4001)
        self.brand = Property(str, id=2, uid=4002)
        self.year = Property(int, id=3, uid=4003)
        self.model = Property(str, id=4, uid=4004)
        self.energy = Property(int, id=5, uid=4005)
        self.maxEnergy = Property(int, id=6, uid=4006)

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
class EnergyModule(Module):
    def __init__(self, serialNumber, brand, year, model, energy, maxEnergy, output, rechargeRate):
        super().__init__(serialNumber, brand, year, model, energy, maxEnergy)
        self.output = Property(int, id=1, uid=5001)
        self.rechargeRate = Property(int, id=2, uid=5002)

    def getOutput(self):
        return self.output

    def getRechargeRate(self):
        return self.rechargeRate

    def setOutput(self, output):
        self.output = output

    def setRechargeRate(self, rechargeRate):
        self.rechargeRate = rechargeRate


@Entity(id=6, uid=6)
class WeaponModule(Module):
    def __init__(self, serialNumber, brand, year, model, energy, maxEnergy, weaponType, caliber):
        super().__init__(serialNumber, brand, year, model, energy, maxEnergy)
        self.weaponType = Property(str, id=1, uid=6001)
        self.caliber = Property(int, id=2, uid=6002)

    def getType(self):
        return self.weaponType

    def getCaliber(self):
        return self.caliber


@Entity(id=7, uid=7)
class ShieldModule(Module):
    def __init__(self, serialNumber, brand, year, model, energy, maxEnergy, size):
        super().__init__(serialNumber, brand, year, model, energy, maxEnergy)
        self.size = Property(int, id=1, uid=7001)

    def getSize(self):
        return self.size

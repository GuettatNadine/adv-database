import persistent


class Module(persistent.Persistent):
    def __init__(self, serialNumber, brand, year, model, energy, maxEnergy):
        self.serialNumber = int(serialNumber)
        self.brand = brand
        self.year = int(year)
        self.model = model
        self.energy = int(energy)
        self.maxEnergy = int(maxEnergy)

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


class EnergyModule(Module):
    def __init__(self, serialNumber, brand, year, model, energy, maxEnergy, output, rechargeRate):
        super().__init__(serialNumber, brand, year, model, energy, maxEnergy)
        self.output = int(output)
        self.rechargeRate = float(rechargeRate)

    def getOutput(self):
        return self.output

    def getRechargeRate(self):
        return self.rechargeRate

    def setOutput(self, output):
        self.output = output

    def setRechargeRate(self, rechargeRate):
        self.rechargeRate = rechargeRate


class WeaponModule(Module):
    def __init__(self, serialNumber, brand, year, model, energy, maxEnergy, weaponType, caliber):
        super().__init__(serialNumber, brand, year, model, energy, maxEnergy)
        self.weaponType = weaponType
        self.caliber = int(caliber)

    def getType(self):
        return self.weaponType

    def getCaliber(self):
        return self.caliber


class ShieldModule(Module):
    def __init__(self, serialNumber, brand, year, model, energy, maxEnergy, size):
        super().__init__(serialNumber, brand, year, model, energy, maxEnergy)
        self.size = int(size)

    def getSize(self):
        return self.size

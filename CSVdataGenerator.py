import faker
import numpy as np
import csv


def getTestData(n, filename):
    filename += ".csv"
    galxiesFile = "Galaxies" + filename
    ShipsFile = "Ships" + filename
    militaryPersonsFile = "MilitaryPersons" + filename
    civilianPersonsFile = "CivilianPersons" + filename
    energyModulesFile = "EnergyModules" + filename
    weaponModulesFile = "WeaponModules" + filename
    shieldModulesFile = "ShieldModules" + filename
    cargoItemsFile = "CargoItems" + filename

    numberOfObjects = 0
    fake = faker.Faker()

    with open(galxiesFile, 'w', newline='') as Gfile, open(ShipsFile, 'w', newline='') as Sfile, \
            open(militaryPersonsFile, 'w', newline='') as MPfile, open(civilianPersonsFile, 'w', newline='') as CPfile, \
            open(energyModulesFile, 'w', newline='') as EMfile, open(weaponModulesFile, 'w', newline='') as WMfile, \
            open(shieldModulesFile, 'w', newline='') as SMfile, open(cargoItemsFile, 'w', newline='') as CIfile:

        Gwriter = csv.writer(Gfile)
        Gwriter.writerow(["galaxy_id", "name", "universe"])

        Swriter = csv.writer(Sfile)
        Swriter.writerow(["ship_id", "affiliation", "type", "galaxy_id"])

        MPwriter = csv.writer(MPfile)
        MPwriter.writerow(["military_id", "name", "age", "rank", "specialization", "ship_id"])

        CPwriter = csv.writer(CPfile)
        CPwriter.writerow(["civilian_id", "name", "age", "occupation", "ship_id"])

        EMwriter = csv.writer(EMfile)
        EMwriter.writerow(
            ["module_id", "brand", "year", "model", "energy", "maxEnergy", "output", "recharge_rate",
             "ship_id"])

        WMwriter = csv.writer(WMfile)
        WMwriter.writerow(
            ["module_id", "brand", "year", "model", "energy", "maxEnergy", "type", "caliber", "ship_id"])

        CIwriter = csv.writer(CIfile)
        CIwriter.writerow(["item_id", "name", "quantity", "ship_id"])

        SMwriter = csv.writer(SMfile)
        SMwriter.writerow(
            ["module_id", "brand", "year", "model", "energy", "maxEnergy", "size", "ship_id"])

        # generate between 3 to 10 galaxies
        num_galaxies = np.random.randint(3, 11)
        num_universes = np.random.randint(1, num_galaxies + 1)
        galaxy_names = [fake.word() + " galaxy" for _ in range(num_galaxies)]
        universe_names = [fake.word() + " universe" for _ in range(num_universes)]
        military_id = 0
        civilian_id = 0
        weapons_id = 0
        energy_id = 0
        shields_id = 0
        cargo_item_id = 0
        for galaxy in range(len(galaxy_names)):
            numberOfObjects += 1
            Gwriter.writerow([galaxy, galaxy_names[galaxy], np.random.choice(universe_names)])

        num_ships = n
        affiliations_list = ["amarr", "caldari", "gallente", "ammatar", "khanid kingdom"]
        ship_type_list = ["transport", "mother", "scout", "combat", "private", "stealth"]
        mother_ship_specializations = ["communication", "weapons", "navigation"]
        military_specializations = ["fighter pilot", "pilot", "engineer", "medic", "scout"]
        manufacturers = ["behring", "klaus & werner", "associated sciences & development", "joker Engineering"]
        weapon_type = ["plasma", "laser"]
        cargo_items_list = [
            "iron", "copper", "sand", "titanium", "aluminum", "gold", "plastic",
            "diamond", "wood", "silver", "rubber", "glass", "coal", "paper",
            "meat", "vegetable", "fruit", "cheese", "bread", "fish", "chocolate"
        ]
        for ship in range(0, num_ships):
            numberOfObjects += 1
            galaxy_location = np.random.randint(0, len(galaxy_names))
            affiliation = np.random.choice(affiliations_list)
            ship_type = np.random.choice(ship_type_list)
            Swriter.writerow([ship, affiliation, ship_type, galaxy_location])
            if ship_type in ["mother", "scout", "combat", "stealth"]:
                if ship_type == "mother":
                    MPwriter.writerow([military_id, fake.name(), np.random.randint(40, 81), 5, "commander", ship])
                    military_id += 1

                    for _ in range(5):
                        numberOfObjects += 1
                        MPwriter.writerow([military_id, fake.name(), np.random.randint(30, 81), np.random.randint(3, 5),
                                           np.random.choice(mother_ship_specializations), ship])
                        military_id += 1

                    for _ in range(np.random.randint(10, 101)):
                        numberOfObjects += 2
                        MPwriter.writerow([military_id, fake.name(), np.random.randint(18, 81), np.random.randint(0, 3),
                                           np.random.choice(military_specializations), ship])
                        military_id += 1
                        CPwriter.writerow([civilian_id, fake.name(), np.random.randint(18, 81), fake.job(), ship])
                        civilian_id += 1

                elif ship_type == "stealth":
                    numberOfObjects += 1
                    MPwriter.writerow(
                        [military_id, fake.name(), np.random.randint(18, 81), np.random.randint(0, 3), "pilot", ship])
                    military_id += 1

                elif ship_type == "scout":
                    numberOfObjects += 1
                    MPwriter.writerow(
                        [military_id, fake.name(), np.random.randint(18, 81), np.random.randint(0, 3), "scout", ship])
                    military_id += 1

                elif ship_type == "combat":
                    numberOfObjects += 1
                    MPwriter.writerow(
                        [military_id, fake.name(), np.random.randint(18, 81), np.random.randint(0, 3), "fighter pilot",
                         ship])
                    military_id += 1

            elif ship_type == "transport":
                numberOfObjects += 1
                CPwriter.writerow([civilian_id, fake.name(), np.random.randint(18, 80), "pilot", ship])
                civilian_id += 1
                num_items_in_cargo = np.random.randint(1, 6)
                for item in range(num_items_in_cargo):
                    item_id = np.random.randint(0, len(cargo_items_list))
                    CIwriter.writerow([cargo_item_id, cargo_items_list[item_id], np.random.randint(1, 10), ship])
                    cargo_item_id += 1

            elif ship_type == "private":
                numberOfObjects += 1
                CPwriter.writerow([civilian_id, fake.name(), np.random.randint(18, 80), fake.job(), ship])
                civilian_id += 1

            if ship_type == "mother":
                for _ in range(0, np.random.randint(15, 21)):
                    numberOfObjects += 1
                    EMwriter.writerow(
                        [energy_id, np.random.choice(manufacturers), np.random.randint(3000, 5432),
                         np.random.randint(1, 6), np.random.randint(0, 101), np.random.randint(100, 151),
                         np.random.randint(5, 11),
                         np.round(np.random.uniform(0, 10), 1),
                         ship])
                    energy_id += 1
                for _ in range(0, np.random.randint(15, 21)):
                    numberOfObjects += 1
                    WMwriter.writerow(
                        [weapons_id, np.random.choice(manufacturers), np.random.randint(3000, 5432),
                         np.random.randint(1, 6), np.random.randint(0, 101), np.random.randint(100, 151),
                         np.random.choice(weapon_type), np.random.randint(3, 6),
                         ship])
                    weapons_id += 1
                for _ in range(0, np.random.randint(15, 21)):
                    numberOfObjects += 1
                    SMwriter.writerow([shields_id, np.random.choice(manufacturers), np.random.randint(3000, 5432),
                                       np.random.randint(1, 6), np.random.randint(0, 101), np.random.randint(100, 151),
                                       np.random.randint(3, 6),
                                       ship])
                    shields_id += 1
            else:
                EMwriter.writerow(
                    [energy_id, np.random.choice(manufacturers), np.random.randint(3000, 5432),
                     np.random.randint(1, 6), np.random.randint(0, 101), np.random.randint(100, 151),
                     np.random.randint(5, 11),
                     np.round(np.random.uniform(0, 10), 1),
                     ship])
                WMwriter.writerow(
                    [weapons_id, np.random.choice(manufacturers), np.random.randint(3000, 5432),
                     np.random.randint(1, 6), np.random.randint(0, 101), np.random.randint(100, 151),
                     np.random.choice(weapon_type), np.random.randint(1, 3),
                     ship])
                SMwriter.writerow([shields_id, np.random.choice(manufacturers), np.random.randint(3000, 5432),
                                   np.random.randint(1, 5), np.random.randint(0, 101), np.random.randint(100, 151),
                                   np.random.randint(1, 3),
                                   ship])
                weapons_id += 1
                energy_id += 1
                shields_id += 1
                numberOfObjects += 3

    return numberOfObjects


sampleSize = input("sample size (number of objects) : ")
fileName = input("file name : ")
fileName += sampleSize
print(getTestData(int(sampleSize), fileName))

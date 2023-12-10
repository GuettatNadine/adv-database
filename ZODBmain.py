import persistent
import ZODB
import ZODB.FileStorage
import transaction
import BTrees.OOBTree
import ZODBGalaxy as Galaxy
import ZODBShip as Ship
import ZODBModule as Module
import ZODBPerson as Person
import csv
import time


def insertGalaxy(csvFilePath, tree):
    # Open the CSV file
    with open(csvFilePath, 'r') as file:
        # Contains the rows of the csv as dictionaries
        csvReader = csv.DictReader(file)

        # Iterate through each row in the CSV file
        for row in csvReader:
            tree["galaxy_num"] = int(row["galaxy_id"])
            tree["galaxy"].insert(row["galaxy_id"], Galaxy.Galaxy(row["galaxy_id"], row["name"], row["universe"]))
            transaction.commit()  # Register the modification (transaction) into the database
    return tree


def insertShips(csvFilePath, dictShipObj, tree):
    # Open the CSV file
    with open(csvFilePath, 'r') as file:
        # Contains the rows of the csv as dictionaries
        csvReader = csv.DictReader(file)

        # Iterate through each row in the CSV file
        for row in csvReader:
            tree["ship_num"] = int(row["ship_id"])
            shipType = row["type"]
            # We create the ship
            if shipType == "mother":
                ship = Ship.MotherShip(row["ship_id"], row["affiliation"])
            elif shipType == "transport":
                ship = Ship.TransportShip(row["ship_id"], row["affiliation"])
                if row["ship_id"] in dictShipObj["CA"].keys():
                    for item in dictShipObj["CA"][row["ship_id"]]:
                        ship.addCargo(item[1], item[2])
            else:
                ship = Ship.OtherShip(row["ship_id"], row["affiliation"], row["type"])

            # We add the crew and the passengers
            if shipType in ["transport", "private"]:
                ship.addCrew(dictShipObj["C"][row["ship_id"]])
            else:
                ship.addCrew(dictShipObj["M"][row["ship_id"]])
                if shipType == "mother":
                    ship.addPassengers(dictShipObj["C"][row["ship_id"]])

            # We add the Modules
            if row["ship_id"] in dictShipObj["S"].keys():
                ship.addModules("shield", dictShipObj["S"][row["ship_id"]])
            if row["ship_id"] in dictShipObj["E"].keys():
                ship.addModules("energy", dictShipObj["E"][row["ship_id"]])
            if row["ship_id"] in dictShipObj["W"].keys():
                ship.addModules("weapon", dictShipObj["W"][row["ship_id"]])

            # We add the ship
            tree["galaxy"][row["galaxy_id"]].addShip(ship)
            transaction.commit()  # Register the modification (transaction) into the database
    return tree


def createMilitaryPerson(csvFilePath, tree):
    dictMilitary = {}
    # Open the CSV file
    with open(csvFilePath, 'r') as file:
        # Contains the rows of the csv as dictionaries
        csvReader = csv.DictReader(file)

        # Iterate through each row in the CSV file
        for row in csvReader:
            tree["military_num"] = int(row["military_id"])
            if row["ship_id"] not in dictMilitary.keys():
                dictMilitary[row["ship_id"]] = []
            dictMilitary[row["ship_id"]].append(
                Person.MilitaryPerson(row["military_id"], row["name"], row["age"], row["rank"], row["specialization"]))
    return dictMilitary, tree


def createCivilianPerson(csvFilePath, tree):
    dictCivilian = {}
    # Open the CSV file
    with open(csvFilePath, 'r') as file:
        # Contains the rows of the csv as dictionaries
        csvReader = csv.DictReader(file)

        # Iterate through each row in the CSV file
        for row in csvReader:
            tree["civilian_num"] = int(row["civilian_id"])
            if row["ship_id"] not in dictCivilian.keys():
                dictCivilian[row["ship_id"]] = []
            dictCivilian[row["ship_id"]].append(
                Person.CivilianPerson(row["civilian_id"], row["name"], row["age"], row["occupation"]))
    return dictCivilian, tree


def createCargo(csvFilePath, tree):
    dictCargo = {}
    # Open the CSV file
    with open(csvFilePath, 'r') as file:
        # Contains the rows of the csv as dictionaries
        csvReader = csv.DictReader(file)

        # Iterate through each row in the CSV file
        for row in csvReader:
            tree["item_num"] = int(row["item_id"])
            if row["ship_id"] not in dictCargo.keys():
                dictCargo[row["ship_id"]] = []
            dictCargo[row["ship_id"]].append([row["item_id"], row["name"], row["quantity"]])
    return dictCargo, tree


def createShieldModule(csvFilePath, tree):
    dictShield = {}
    # Open the CSV file
    with open(csvFilePath, 'r') as file:
        # Contains the rows of the csv as dictionaries
        csvReader = csv.DictReader(file)

        # Iterate through each row in the CSV file
        for row in csvReader:
            tree["module_num"] = int(row["module_id"])
            if row["ship_id"] not in dictShield.keys():
                dictShield[row["ship_id"]] = []
            dictShield[row["ship_id"]].append(
                Module.ShieldModule(row["module_id"], row["brand"], row["year"], row["model"], row["energy"],
                                    row["maxEnergy"], row["size"]))
    return dictShield, tree


def createEnergyModule(csvFilePath, tree):
    dictEnergy = {}
    # Open the CSV file
    with open(csvFilePath, 'r') as file:
        # Contains the rows of the csv as dictionaries
        csvReader = csv.DictReader(file)

        # Iterate through each row in the CSV file
        for row in csvReader:
            tree["module_num"] = int(row["module_id"])
            if row["ship_id"] not in dictEnergy.keys():
                dictEnergy[row["ship_id"]] = []
            dictEnergy[row["ship_id"]].append(
                Module.EnergyModule(row["module_id"], row["brand"], row["year"], row["model"], row["energy"],
                                    row["maxEnergy"], row["output"], row["recharge_rate"]))
    return dictEnergy, tree


def createWeaponModule(csvFilePath, tree):
    dictWeapon = {}
    # Open the CSV file
    with open(csvFilePath, 'r') as file:
        # Contains the rows of the csv as dictionaries
        csvReader = csv.DictReader(file)

        # Iterate through each row in the CSV file
        for row in csvReader:
            tree["module_num"] = int(row["module_id"])
            if row["ship_id"] not in dictWeapon.keys():
                dictWeapon[row["ship_id"]] = []
            dictWeapon[row["ship_id"]].append(
                Module.WeaponModule(row["module_id"], row["brand"], row["year"], row["model"], row["energy"],
                                    row["maxEnergy"], row["type"], row["caliber"]))
    return dictWeapon, tree


def insertIntoShips(militaryCsv, civilianCsv, shieldCsv, energyCsv, weaponCsv, cargoCsv, tree):
    """Create dict for the objects of a ship in order to add them easily"""
    dictMilitary, tree = createMilitaryPerson(militaryCsv, tree)
    dictCivilian, tree = createCivilianPerson(civilianCsv, tree)
    dictShield, tree = createShieldModule(shieldCsv, tree)
    dictEnergy, tree = createEnergyModule(energyCsv, tree)
    dictWeapon, tree = createWeaponModule(weaponCsv, tree)
    dictCargo, tree = createCargo(cargoCsv, tree)

    dictShipObj = {"M": dictMilitary, "C": dictCivilian, "S": dictShield, "E": dictEnergy, "W": dictWeapon,
                   "CA": dictCargo}
    return dictShipObj, tree


def createZODB(fileName):
    """Creation of the Zope Object Database"""
    storage = ZODB.FileStorage.FileStorage(fileName)
    db = ZODB.DB(storage)
    return db


def main():
    choice = input("\"start\" to create the db and inserting an object\n"
                   "\'load\" to load the database and see the object\nInput : ")

    # Start the database for the fist time and create the Objects from the CSV files
    if choice == "start":
        # Record start time
        start_time = time.time()

        # Creating the database
        db = createZODB("MyZopeOODB.fs")

        # Connecting to the database
        connection = db.open()
        root = connection.root()

        # creating a binary tree in order to store the galaxies
        root['galaxy'] = BTrees.OOBTree.BTree()

        # Creating and inserting the galaxies into the database from the CSV file
        root = insertGalaxy("Galaxies.csv", root)

        # Creating the Objects composing a ship
        dictShipObj, root = insertIntoShips("MilitaryPersons.csv", "CivilianPersons.csv", "ShieldModules.csv",
                                            "EnergyModules.csv", "WeaponModules.csv", "CargoItems.csv", root)

        # Creating ships and adding modules and persons in them and inserting the ships in the database
        root = insertShips("Ships.csv", dictShipObj, root)

        # Close the connection to the database
        connection.close()

        # Record end time
        end_time = time.time()
        # Calculate elapsed time
        elapsed_seconds = end_time - start_time
        print(f"Elapsed time for the creation of the database: {elapsed_seconds:.6f} seconds\n")

    # Load the objects from the Zope object Database
    if choice == "load":
        # Load the database
        storage = ZODB.FileStorage.FileStorage('MyZopeOODB.fs')
        db = ZODB.DB(storage)

        # Start a connection
        connection = db.open()
        root = connection.root()

        # Queries :
        """First Query Select : """

        count = 0
        affiliation = str("khanid kingdom")
        found = False
        result = []
        # Record start time
        start_time = time.time()
        for g in root["galaxy"]:
            if affiliation in root["galaxy"].get(g).ships.keys():
                for ship in root["galaxy"].get(g).getShips(affiliation):
                    for member in ship.getCrew():
                        if type(member) == Person.CivilianPerson:
                            break
                        if member.getSpecialization() == "weapons":
                            found = True
                            break
                    if found:
                        found = False
                        for weapon in ship.getModules("weapon"):
                            if weapon.getCaliber() >= 3:
                                count += 1
                                break
        # Record end time
        end_time = time.time()
        # Calculate elapsed time
        elapsed_seconds = end_time - start_time
        print("number of results found : ", count)
        print(f"Elapsed time for the first query: {elapsed_seconds:.6f} seconds\n")

        """Second Query Select : """
        count = 0
        engCounter = 0
        # Record start time
        start_time = time.time()
        affiliation = str("caldari")
        for g in root["galaxy"]:
            if affiliation in root["galaxy"].get(g).ships.keys():
                for ship in root["galaxy"].get(g).getShips(affiliation):
                    found = 0
                    for member in ship.getCrew():
                        if type(member) == Person.CivilianPerson:
                            break
                        if member.getSpecialization() == "engineer":
                            found = 1
                            engCounter += 1
                            if engCounter >= 3:
                                break
                    if found == 1 and engCounter >= 3:
                        engCounter = 0
                        for weapon in ship.getModules("weapon"):
                            if weapon.getCaliber() >= 2:
                                found = 2
                                break
                        if found == 2:
                            for shield in ship.getModules("shield"):
                                if shield.getSize() >= 2:
                                    found = 3
                                    break
                        if found == 3:
                            for energy in ship.getModules("energy"):
                                if energy.getOutput() < 80:
                                    found = 4
                                    break
                    if found == 4:
                        if type(ship) == Ship.MotherShip:
                            tempType = "mother"
                        elif type(ship) == Ship.TransportShip:
                            tempType = "transport"
                        else:
                            tempType = ship.getShipType()
                        result.append([ship.getSerialNumber(), tempType, root["galaxy"].get(g)])
                        count += 1

        # Record end time
        end_time = time.time()

        # Calculate elapsed time
        elapsed_seconds = end_time - start_time
        print("number of results found : ", count)
        print("results found : ")
        print("id   |   ship type   |   location")
        for res in result:
            print(res[0], "     ", res[1], "     ", res[2].getName())
        print(f"Elapsed time for the second query: {elapsed_seconds:.6f} seconds\n")

        """Third Query Add : """
        for g in root["galaxy"]:
            if affiliation in root["galaxy"].get(g).ships.keys():
                for ship in root["galaxy"].get(g).getShips(affiliation):  # print last crew member added
                    if ship.getSerialNumber() == 0:
                        print("last crew member added before insert : ", ship.getCrew()[-1], "\n")
                        break

        # Record start time
        start_time = time.time()
        for g in root["galaxy"]:
            if affiliation in root["galaxy"].get(g).ships.keys():
                for ship in root["galaxy"].get(g).getShips(affiliation):
                    if ship.getSerialNumber() == 0:
                        root["military_num"] += 1
                        tempMilitaryPerson = Person.MilitaryPerson(root["military_num"], "Query McGuyer", 25, 3, "engineer")
                        ship.addCrew([tempMilitaryPerson])
                        break
        transaction.commit()  # Register the modification (transaction) into the database
        # Record end time
        end_time = time.time()
        print(f"Elapsed time for the third query: {elapsed_seconds:.6f} seconds\n")
        # Calculate elapsed time
        elapsed_seconds = end_time - start_time

        for g in root["galaxy"]:
            if affiliation in root["galaxy"].get(g).ships.keys():
                for ship in root["galaxy"].get(g).getShips(affiliation):  # print last crew member added
                    if ship.getSerialNumber() == 0:
                        print("last crew member added after insert : ", ship.getCrew()[-1], "\n")
                        break

        """Fourth Query Delete : """
        # Record start time
        start_time = time.time()
        for g in root["galaxy"]:
            if affiliation in root["galaxy"].get(g).ships.keys():
                for ship in root["galaxy"].get(g).getShips(affiliation):
                    if ship.getSerialNumber() == 0:
                        del ship.crew[root["military_num"]]
                        break
        transaction.commit()  # Register the modification (transaction) into the database
        # Record end time
        end_time = time.time()

        # Calculate elapsed time
        elapsed_seconds = end_time - start_time
        print(f"Elapsed time for the fourth query: {elapsed_seconds:.6f} seconds\n")

        for g in root["galaxy"]:
            if affiliation in root["galaxy"].get(g).ships.keys():
                for ship in root["galaxy"].get(g).getShips(affiliation):  # print last crew member added
                    if ship.getSerialNumber() == 0:
                        print("last crew member added after delete : ", ship.getCrew()[-1], "\n")
                        break

        # Close the connection to the database
        connection.close()
    return 0


main()

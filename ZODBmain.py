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


def insertGalaxy(csvFilePath, tree):
    # Open the CSV file
    with open(csvFilePath, 'r') as file:
        # Contains the rows of the csv as dictionaries
        csvReader = csv.DictReader(file)

        # Iterate through each row in the CSV file
        for row in csvReader:
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


def createMilitaryPerson(csvFilePath):
    dictMilitary = {}
    # Open the CSV file
    with open(csvFilePath, 'r') as file:
        # Contains the rows of the csv as dictionaries
        csvReader = csv.DictReader(file)

        # Iterate through each row in the CSV file
        for row in csvReader:
            if row["ship_id"] not in dictMilitary.keys():
                dictMilitary[row["ship_id"]] = []
            dictMilitary[row["ship_id"]].append(
                Person.MilitaryPerson(row["military_id"], row["name"], row["age"], row["rank"], row["specialization"]))
    return dictMilitary


def createCivilianPerson(csvFilePath):
    dictCivilian = {}
    # Open the CSV file
    with open(csvFilePath, 'r') as file:
        # Contains the rows of the csv as dictionaries
        csvReader = csv.DictReader(file)

        # Iterate through each row in the CSV file
        for row in csvReader:
            if row["ship_id"] not in dictCivilian.keys():
                dictCivilian[row["ship_id"]] = []
            dictCivilian[row["ship_id"]].append(
                Person.CivilianPerson(row["civilian_id"], row["name"], row["age"], row["occupation"]))
    return dictCivilian


def createCargo(csvFilePath):
    dictCargo = {}
    # Open the CSV file
    with open(csvFilePath, 'r') as file:
        # Contains the rows of the csv as dictionaries
        csvReader = csv.DictReader(file)

        # Iterate through each row in the CSV file
        for row in csvReader:
            if row["ship_id"] not in dictCargo.keys():
                dictCargo[row["ship_id"]] = []
            dictCargo[row["ship_id"]].append([row["item_id"], row["name"], row["quantity"]])
    return dictCargo


def createShieldModule(csvFilePath):
    dictShield = {}
    # Open the CSV file
    with open(csvFilePath, 'r') as file:
        # Contains the rows of the csv as dictionaries
        csvReader = csv.DictReader(file)

        # Iterate through each row in the CSV file
        for row in csvReader:
            if row["ship_id"] not in dictShield.keys():
                dictShield[row["ship_id"]] = []
            dictShield[row["ship_id"]].append(
                Module.ShieldModule(row["module_id"], row["brand"], row["year"], row["model"], row["energy"],
                                    row["maxEnergy"], row["size"]))
    return dictShield


def createEnergyModule(csvFilePath):
    dictEnergy = {}
    # Open the CSV file
    with open(csvFilePath, 'r') as file:
        # Contains the rows of the csv as dictionaries
        csvReader = csv.DictReader(file)

        # Iterate through each row in the CSV file
        for row in csvReader:
            if row["ship_id"] not in dictEnergy.keys():
                dictEnergy[row["ship_id"]] = []
            dictEnergy[row["ship_id"]].append(
                Module.EnergyModule(row["module_id"], row["brand"], row["year"], row["model"], row["energy"],
                                    row["maxEnergy"], row["output"], row["recharge_rate"]))
    return dictEnergy


def createWeaponModule(csvFilePath):
    dictWeapon = {}
    # Open the CSV file
    with open(csvFilePath, 'r') as file:
        # Contains the rows of the csv as dictionaries
        csvReader = csv.DictReader(file)

        # Iterate through each row in the CSV file
        for row in csvReader:
            if row["ship_id"] not in dictWeapon.keys():
                dictWeapon[row["ship_id"]] = []
            dictWeapon[row["ship_id"]].append(
                Module.WeaponModule(row["module_id"], row["brand"], row["year"], row["model"], row["energy"],
                                    row["maxEnergy"], row["type"], row["caliber"]))
    return dictWeapon


def insertIntoShips(militaryCsv, civilianCsv, shieldCsv, energyCsv, weaponCsv, cargoCsv):
    """Create dict for the objects of a ship in order to add them easily"""
    dictMilitary = createMilitaryPerson(militaryCsv)
    dictCivilian = createCivilianPerson(civilianCsv)
    dictShield = createShieldModule(shieldCsv)
    dictEnergy = createEnergyModule(energyCsv)
    dictWeapon = createWeaponModule(weaponCsv)
    dictCargo = createCargo(cargoCsv)

    dictShipObj = {"M": dictMilitary, "C": dictCivilian, "S": dictShield, "E": dictEnergy, "W": dictWeapon,
                   "CA": dictCargo}
    return dictShipObj


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
        # Creating the database
        db = createZODB("MyZopeOODB.fs")

        # Connecting to the database
        connection = db.open()
        root = connection.root()

        # creating a binary tree in order to store the galaxies
        root['galaxy'] = BTrees.OOBTree.BTree()

        # Creating and inserting the galaxies into the database from the CSV file
        root = insertGalaxy("Galaxies10.csv", root)

        # Creating the Objects composing a ship
        dictShipObj = insertIntoShips("MilitaryPersons10.csv", "CivilianPersons10.csv", "ShieldModules10.csv",
                                      "EnergyModules10.csv", "WeaponModules10.csv", "CargoItems10.csv")

        # Creating ships and adding modules and persons in them and inserting the ships in the database
        root = insertShips("Ships10.csv", dictShipObj, root)

        # Close the connection to the database
        connection.close()

    # Load the objects from the Zope object Database
    if choice == "load":
        # Load the database
        storage = ZODB.FileStorage.FileStorage('MyZopeOODB.fs')
        db = ZODB.DB(storage)

        # Start a connection
        connection = db.open()
        root = connection.root()

        # Queries :
        for member in root["galaxy"].get("0").getShips("khanid kingdom")[0].getCrew():
            print("crew member : ", end="")
            print(member)
        """
        for member in root["galaxy"].get("0").getShips("khanid kingdom")[0].getPassengers():
            print("passenger : ", end="")
            print(member)
        """

        # Close the connection to the database
        connection.close()
    return 0


main()
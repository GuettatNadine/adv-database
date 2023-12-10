import objectbox

import OBOXGalaxy as Galaxy
import OBOXShip as Ship
import OBOXModule as Module
import OBOXPerson as Person

import csv


def insertGalaxy(csvFilePath, box):
    # Open the CSV file
    with open(csvFilePath, 'r') as file:
        # Contains the rows of the csv as dictionaries
        csvReader = csv.DictReader(file)

        # Iterate through each row in the CSV file
        for row in csvReader:
            # Create a Galaxy object
            galaxy = Galaxy.Galaxy(row["galaxy_id"], row["name"], row["universe"])
            
            # Put the Galaxy object into the ObjectBox database
            box.put(galaxy)


def insertShips(csvFilePath, dictShipObj, box):
    # Open the CSV file
    with open(csvFilePath, 'r') as file:
        # Contains the rows of the csv as dictionaries
        csvReader = csv.DictReader(file)

        # Iterate through each row in the CSV file
        for row in csvReader:
            # Determine the ship type
            shipType = row["type"]
            
            # Create the corresponding ship object based on the ship type
            if shipType == "mother":
                ship = Ship.MotherShip(row["ship_id"], row["affiliation"])
            elif shipType == "transport":
                ship = Ship.TransportShip(row["ship_id"], row["affiliation"])
                if row["ship_id"] in dictShipObj["CA"].keys():
                    for item in dictShipObj["CA"][row["ship_id"]]:
                        ship.addCargo(item[1], item[2])
            else:
                ship = Ship.OtherShip(row["ship_id"], row["affiliation"], row["type"])

            # Add crew and passengers based on ship type
            if shipType in ["transport", "private"]:
                ship.addCrew(dictShipObj["C"][row["ship_id"]])
            else:
                ship.addCrew(dictShipObj["M"][row["ship_id"]])
                if shipType == "mother":
                    ship.addPassengers(dictShipObj["C"][row["ship_id"]])

            # Add modules based on ship ID
            if row["ship_id"] in dictShipObj["S"].keys():
                ship.addModules("shield", dictShipObj["S"][row["ship_id"]])
            if row["ship_id"] in dictShipObj["E"].keys():
                ship.addModules("energy", dictShipObj["E"][row["ship_id"]])
            if row["ship_id"] in dictShipObj["W"].keys():
                ship.addModules("weapon", dictShipObj["W"][row["ship_id"]])

            # Put the ship object into the ObjectBox database
            box.put(ship)


def createMilitaryPerson(csvFilePath):
    # Dictionary to store military persons based on ship ID
    dictMilitary = {}
    
    # Open the CSV file
    with open(csvFilePath, 'r') as file:
        # Contains the rows of the csv as dictionaries
        csvReader = csv.DictReader(file)

        # Iterate through each row in the CSV file
        for row in csvReader:
            # Check if ship ID is not in the dictionary, add an empty list
            if row["ship_id"] not in dictMilitary.keys():
                dictMilitary[row["ship_id"]] = []
            
            # Create a MilitaryPerson object
            military_person = Person.MilitaryPerson(row["military_id"], row["name"], row["age"],
                                                    row["rank"], row["specialization"])
            
            # Append the MilitaryPerson object to the list based on ship ID
            dictMilitary[row["ship_id"]].append(military_person)
    
    return dictMilitary


def createCivilianPerson(csvFilePath):
    # Dictionary to store civilian persons based on ship ID
    dictCivilian = {}
    
    # Open the CSV file
    with open(csvFilePath, 'r') as file:
        # Contains the rows of the csv as dictionaries
        csvReader = csv.DictReader(file)

        # Iterate through each row in the CSV file
        for row in csvReader:
            # Check if ship ID is not in the dictionary, add an empty list
            if row["ship_id"] not in dictCivilian.keys():
                dictCivilian[row["ship_id"]] = []
            
            # Create a CivilianPerson object
            civilian_person = Person.CivilianPerson(row["civilian_id"], row["name"], row["age"],
                                                    row["occupation"])
            
            # Append the CivilianPerson object to the list based on ship ID
            dictCivilian[row["ship_id"]].append(civilian_person)
    
    return dictCivilian


def createCargo(csvFilePath):
    # Dictionary to store cargo items based on ship ID
    dictCargo = {}
    
    # Open the CSV file
    with open(csvFilePath, 'r') as file:
        # Contains the rows of the csv as dictionaries
        csvReader = csv.DictReader(file)

        # Iterate through each row in the CSV file
        for row in csvReader:
            # Check if ship ID is not in the dictionary, add an empty list
            if row["ship_id"] not in dictCargo.keys():
                dictCargo[row["ship_id"]] = []
            
            # Append the cargo item details to the list based on ship ID
            dictCargo[row["ship_id"]].append([row["item_id"], row["name"], row["quantity"]])
    
    return dictCargo


def createShieldModule(csvFilePath):
    # Dictionary to store shield modules based on ship ID
    dictShield = {}
    
    # Open the CSV file
    with open(csvFilePath, 'r') as file:
        # Contains the rows of the csv as dictionaries
        csvReader = csv.DictReader(file)

        # Iterate through each row in the CSV file
        for row in csvReader:
            # Check if ship ID is not in the dictionary, add an empty list
            if row["ship_id"] not in dictShield.keys():
                dictShield[row["ship_id"]] = []
            
            # Create a ShieldModule object
            shield_module = Module.ShieldModule(row["module_id"], row["brand"], row["year"],
                                                row["model"], row["energy"], row["maxEnergy"], row["size"])
            
            # Append the ShieldModule object to the list based on ship ID
            dictShield[row["ship_id"]].append(shield_module)
    
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


def insertIntoShips(militaryCsv, civilianCsv, shieldCsv, energyCsv, weaponCsv, cargoCsv, box):
    # Create dict for the objects of a ship in order to add them easily
    dictMilitary = createMilitaryPerson(militaryCsv)
    dictCivilian = createCivilianPerson(civilianCsv)
    dictShield = createShieldModule(shieldCsv)
    dictEnergy = createEnergyModule(energyCsv)
    dictWeapon = createWeaponModule(weaponCsv)
    dictCargo = createCargo(cargoCsv)

    dictShipObj = {"M": dictMilitary, "C": dictCivilian, "S": dictShield, "E": dictEnergy, "W": dictWeapon,
                   "CA": dictCargo}

    # Insert galaxies into ObjectBox database
    insertGalaxy("Galaxies10.csv", box)

    # Insert ships into ObjectBox database
    insertShips("Ships10.csv", dictShipObj, box)


def createOBOX(fileName):
    # Configure ObjectBox db
    model = objectbox.Model()
    model.entity(Person.Person, last_property_id=objectbox.model.IdUid(3, 1003))
    model.entity(Person.MilitaryPerson, last_property_id=objectbox.model.IdUid(5, 2005))
    model.entity(Person.CivilianPerson, last_property_id=objectbox.model.IdUid(4, 3004))

    model.entity(Module.Module, last_property_id=objectbox.model.IdUid(6, 4006))
    model.entity(Module.EnergyModule, last_property_id=objectbox.model.IdUid(8, 5008))
    model.entity(Module.WeaponModule, last_property_id=objectbox.model.IdUid(8, 6008))
    model.entity(Module.ShieldModule, last_property_id=objectbox.model.IdUid(7, 7007))

    model.entity(Ship.Ship, last_property_id=objectbox.model.IdUid(4, 8004))
    model.entity(Ship.MotherShip, last_property_id=objectbox.model.IdUid(5, 9005))
    model.entity(Ship.OtherShip, last_property_id=objectbox.model.IdUid(4, 10004))
    model.entity(Ship.TransportShip, last_property_id=objectbox.model.IdUid(5, 11005))

    model.entity(Galaxy.Galaxy, last_property_id=objectbox.model.IdUid(4, 12004))

    model.last_entity_id = objectbox.model.IdUid(12, 12)
    db = objectbox.Builder().model(model).directory(fileName).build()

    return db

def main():
    choice = input("\"start\" to create the db and inserting an object\n"
                   "\"load\" to load the database and see the object\nInput : ")

    if choice == "start":
        # Creating the database
        db = createOBOX("MyOboxOODB")

        # Connecting to the database
        with db.write_tx() as box:  # Use write_tx() for write transactions
            # Creating and inserting the galaxies into the database from the CSV file
            insertIntoShips("MilitaryPersons10.csv", "CivilianPersons10.csv", "ShieldModules10.csv",
                            "EnergyModules10.csv", "WeaponModules10.csv", "CargoItems10.csv", box)

    if choice == "load":
        # Load the database
        model = objectbox.Model()
        db = objectbox.Builder().model(model).directory("MyOboxOODB").build()

        # Start a connection
        with db.read_tx() as box:  # Use read_tx() for read transactions
            # Queries:
            for member in box.get(0).getShips("khanid kingdom")[0].getCrew():
                print("crew member: ", end="")
                print(member)
    return 0

main()


import objectbox

import OBOXGalaxy as Galaxy
import OBOXShip as Ship
import OBOXModule as Module
import OBOXPerson as Person

import csv

def insertGalaxy(csvFilePath, box):
    if box is None:
        print("Error: 'box' is None. Cannot insert Galaxy objects.")
        return

    # Open the CSV file
    with open(csvFilePath, 'r') as file:
        # Contains the rows of the csv as dictionaries
        csvReader = csv.DictReader(file)

        # Iterate through each row in the CSV file
        for row in csvReader:
            # Create a Galaxy object
            galaxy = Galaxy.Galaxy(int(row["galaxy_id"]), row["name"], row["universe"])
            print("BEFORE__________________")
            print(type(galaxy))
            box.put(galaxy)
            print("AFTER__________________")

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



# ___________________

def create_boxes(db):
    # Create boxes for different entity types
    galaxies_box = objectbox.Box(db, Galaxy.Galaxy)
    persons_box = objectbox.Box(db, Person.Person)
    military_persons_box = objectbox.Box(db, Person.MilitaryPerson)
    civilian_persons_box = objectbox.Box(db, Person.CivilianPerson)
    modules_box = objectbox.Box(db, Module.Module)
    energy_modules_box = objectbox.Box(db, Module.EnergyModule)
    weapon_modules_box = objectbox.Box(db, Module.WeaponModule)
    shield_modules_box = objectbox.Box(db, Module.ShieldModule)
    ships_box = objectbox.Box(db, Ship.Ship)
    mother_ships_box = objectbox.Box(db, Ship.MotherShip)
    other_ships_box = objectbox.Box(db, Ship.OtherShip)
    transport_ships_box = objectbox.Box(db, Ship.TransportShip)

    return {
        'galaxies': galaxies_box,
        'persons': persons_box,
        'military_persons': military_persons_box,
        'civilian_persons': civilian_persons_box,
        'modules': modules_box,
        'energy_modules': energy_modules_box,
        'weapon_modules': weapon_modules_box,
        'shield_modules': shield_modules_box,
        'ships': ships_box,
        'mother_ships': mother_ships_box,
        'other_ships': other_ships_box,
        'transport_ships': transport_ships_box,
    }
# ___________________


def insertIntoShips(militaryCsv, civilianCsv, shieldCsv, energyCsv, weaponCsv, cargoCsv, db):
    myBox = create_boxes(db)
    # Create dict for the objects of a ship in order to add them easily
    dictMilitary = createMilitaryPerson(militaryCsv)
    dictCivilian = createCivilianPerson(civilianCsv)
    dictShield = createShieldModule(shieldCsv)
    dictEnergy = createEnergyModule(energyCsv)
    dictWeapon = createWeaponModule(weaponCsv)
    dictCargo = createCargo(cargoCsv)
    
    dictShipObj = {"M": dictMilitary, "C": dictCivilian, "S": dictShield, "E": dictEnergy, "W": dictWeapon,
                   "CA": dictCargo}

    # Obtain the box object from the db instance
    with db.write_tx():
        # Insert galaxies into ObjectBox database
        insertGalaxy("Galaxies10.csv", myBox['galaxies'])

        # Insert ships into ObjectBox database
        insertShips("Ships10.csv", dictShipObj, myBox['ships'])
        print("Ships inserted successfully!")
        
            
def createOBOX(fileName):
    try:
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
        model.entity(Ship.OtherShip, last_property_id=objectbox.model.IdUid(5, 10005))
        model.entity(Ship.TransportShip, last_property_id=objectbox.model.IdUid(5, 11005))

        model.entity(Galaxy.Galaxy, last_property_id=objectbox.model.IdUid(4, 12004))

        model.last_entity_id = objectbox.model.IdUid(12, 12)
        
        # Build the database
#         db = objectbox.Builder().model(model).directory(fileName).build()
        
        builder = objectbox.Builder()
        builder.model(model).directory(fileName)
        db = builder.build()

        if db is not None:
            print("ObjectBox instance created successfully!")
        else:
            print("Error creating ObjectBox database: 'db' is None.")

        return db
    
    except Exception as e:
        print(f"Error creating ObjectBox database: {e}")
        import traceback
        traceback.print_exc()
        
        return None
def main():
    # Prompt the user for input
    choice = input("\"start\" to create the db and inserting an object\n"
                   "\"load\" to load the database and see the object\nInput : ")

    # If the user chooses to start
    if choice == "start":
        # Create ObjectBox database
        db = createOBOX("MyOboxOODB")

        # Check if the database creation was successful
        if db is not None:
            # Insert ships into the database
            insertIntoShips("MilitaryPersons10.csv", "CivilianPersons10.csv", "ShieldModules10.csv",
                            "EnergyModules10.csv", "WeaponModules10.csv", "CargoItems10.csv", db)
            print("Ships inserted successfully!")

    # If the user chooses to load
    if choice == "load":
        # Load the database
        model = objectbox.Model()
        db = objectbox.Builder().model(model).directory("MyOboxOODB").build()

        # Check if the database load was successful
        if db is not None:
            # Start a connection
            with db.read_tx() as box:
                # Queries:
                for member in box.get(0).getShips("khanid kingdom")[0].getCrew():
                    print("crew member: ", end="")
                    print(member)

    return 0

# Run the main function
main()
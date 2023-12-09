-- Create Galaxies Table if not exists
CREATE TABLE IF NOT EXISTS Galaxies (
    galaxy_id INT PRIMARY KEY,
    name VARCHAR(255),
    universe VARCHAR(255)
);

-- Create Ships Table if not exists
CREATE TABLE IF NOT EXISTS Ships (
    ship_id INT PRIMARY KEY,
    affiliation VARCHAR(255),
    type VARCHAR(255),
    galaxy_id INT,
    FOREIGN KEY (galaxy_id) REFERENCES Galaxies(galaxy_id)
);

-- Create CargoItems Table if not exists
CREATE TABLE IF NOT EXISTS CargoItems (
    cargo_item_id INT PRIMARY KEY,
    name VARCHAR(255),
    quantity INT,
    ship_id INT,
    FOREIGN KEY (ship_id) REFERENCES Ships(ship_id)
);

-- Create CivilianPersons Table if not exists
CREATE TABLE IF NOT EXISTS CivilianPersons (
    civilian_id INT PRIMARY KEY,
    name VARCHAR(255),
    age INT,
    occupation VARCHAR(255),
    ship_id INT,
    FOREIGN KEY (ship_id) REFERENCES Ships(ship_id)
);

-- Create EnergyModules Table if not exists
CREATE TABLE IF NOT EXISTS EnergyModules (
    module_id INT PRIMARY KEY,
    brand VARCHAR(255),
    year INT,
    model VARCHAR(255),
    energy INT,
    maxEnergy INT,
    output INT,
    recharge_rate FLOAT,
    ship_id INT,
    FOREIGN KEY (ship_id) REFERENCES Ships(ship_id)
);

-- Create MilitaryPersons Table if not exists
CREATE TABLE IF NOT EXISTS MilitaryPersons (
    military_id INT PRIMARY KEY,
    name VARCHAR(255),
    age INT,
    rank VARCHAR(255),
    specialization VARCHAR(255),
    ship_id INT,
    FOREIGN KEY (ship_id) REFERENCES Ships(ship_id)
);

-- Create ShieldModules Table if not exists
CREATE TABLE IF NOT EXISTS ShieldModules (
    module_id INT PRIMARY KEY,
    brand VARCHAR(255),
    year INT,
    model VARCHAR(255),
    energy INT,
    maxEnergy INT,
    size INT,
    ship_id INT,
    FOREIGN KEY (ship_id) REFERENCES Ships(ship_id)
);

-- Create WeaponModules Table if not exists
CREATE TABLE IF NOT EXISTS WeaponModules (
    module_id INT PRIMARY KEY,
    brand VARCHAR(255),
    year INT,
    model VARCHAR(255),
    energy INT,
    maxEnergy INT,
    type VARCHAR(255),
    caliber INT,
    ship_id INT,
    FOREIGN KEY (ship_id) REFERENCES Ships(ship_id)
);

-- Load data from CSV files into respective tables using INSERT ... ON DUPLICATE KEY UPDATE
COPY Galaxies
FROM 'C:\Users\bluenot\PycharmProjects\adv-database\Galaxies10.csv' HEADER CSV DELIMITER ',';

COPY Ships
FROM 'C:\Users\bluenot\PycharmProjects\adv-database\Ships10.csv' HEADER CSV DELIMITER ',';

COPY CargoItems
FROM 'C:\Users\bluenot\PycharmProjects\adv-database\CargoItems10.csv' HEADER CSV DELIMITER ',';

COPY ShieldModules
FROM 'C:\Users\bluenot\PycharmProjects\adv-database\ShieldModules10.csv' HEADER CSV DELIMITER ',';

COPY MilitaryPersons
FROM 'C:\Users\bluenot\PycharmProjects\adv-database\MilitaryPersons10.csv' HEADER CSV DELIMITER ',';

COPY EnergyModules
FROM 'C:\Users\bluenot\PycharmProjects\adv-database\EnergyModules10.csv' HEADER CSV DELIMITER ',';

COPY CivilianPersons
FROM 'C:\Users\bluenot\PycharmProjects\adv-database\CivilianPersons10.csv' HEADER CSV DELIMITER ',';

COPY WeaponModules
FROM 'C:\Users\bluenot\PycharmProjects\adv-database\WeaponModules10.csv' HEADER CSV DELIMITER ',';